__author__ = "Helmy Saker"
__date__ = "7/15/2021"
__copyright__ = "AccuStrata, Inc. 2021"
__project__ = "QtRefl1D"
__license__ = "Released under MIT License"

import os
import sys
import traceback
from typing import List

import numpy as np
from PySide6.QtCore import Slot
from bumps.cli import beep, initial_model, make_store, preview, resynth, run_command, run_profiler, run_timer, save_best, start_remote_fit, \
    store_overwrite_query
from bumps.fitters import CheckpointMonitor, ConsoleMonitor, FitDriver, StepMonitor
from bumps.mapper import AMQPMapper, MPIMapper, MPMapper, SerialMapper
from bumps.options import BumpsOpts
from numpy import loadtxt
from refl1d.experiment import Experiment
from refl1d.instrument import Monochromatic
from refl1d.material import Material, SLD, Mixture
from refl1d.model import Stack
from refl1d.probe import NeutronProbe
from refl1d.support import sample_data

from app.src.utils.acuUtils import app_path, singleton


@singleton
class AcuReflProxy:
    def __init__(self):
        self.layerStack: Stack = Stack()

        self.steps = np.linspace(0, 5, 100)
        self.dStep = 0.01
        self.length = 4.75
        self.dLength = 0.0475

        self.prob = NeutronProbe(T=self.steps, dT=self.dStep, L=self.length, dL=self.dLength)

        from app.src.guiUtils.AcuGuiGlobal import AcuGuiGlobal
        AcuGuiGlobal.layerUpdateSignal.connect(self.layer_update_slot)

    def run_refl1d(self, options: List[str]):
        opts = BumpsOpts(options)
        opts.resynth = int(opts.resynth)
        # Set a random seed if none is given; want to know the seed so we can
        # reproduce the run.  The seed needs to be saved to the monitor file.
        opts.seed = int(opts.seed) if opts.seed else np.random.randint(1000000)
        opts.fit_config.set_from_cli(opts)

        problem = initial_model(opts)
        if problem is None:
            print("\n!!! Model file missing from command line --- abort !!!.")
            return

        # TODO: AMQP mapper as implemented requires workers started up with
        # the particular problem; need to be able to transport the problem
        # to the worker instead.  Until that happens, the GUI shouldn't use
        # the AMQP mapper.
        if opts.mpi:
            MPIMapper.start_worker(problem)
            mapper = MPIMapper
        elif opts.parallel != "" or opts.worker:
            if opts.transport == 'amqp':
                mapper = AMQPMapper
            elif opts.transport == 'mp':
                mapper = MPMapper
            else:
                raise ValueError("unknown mapper")
        else:
            mapper = SerialMapper
        if opts.worker:
            mapper.start_worker(problem)
            return

        if np.isfinite(float(opts.time)):
            import time
            start_time = time.time()
            stop_time = start_time + float(opts.time) * 3600
            abort_test = lambda: time.time() >= stop_time
        else:
            abort_test = lambda: False

        fitdriver = FitDriver(
            opts.fit_config.selected_fitter, problem=problem, abort_test=abort_test,
            **opts.fit_config.selected_values)

        # Start fitter within the domain so that constraints are valid
        clipped = fitdriver.clip()
        if clipped:
            print("Start value clipped to range for parameter", ", ".join(clipped))

        if opts.time_model:
            run_timer(mapper.start_mapper(problem, opts.args),
                      problem, steps=int(opts.steps))
        elif opts.profile:
            run_profiler(problem, steps=int(opts.steps))
        elif opts.chisq:
            if opts.cov:
                fitdriver.show_cov()
            print("chisq", problem.chisq_str())
            # import pprint; pprint.pprint(problem.to_dict(), indent=2, width=272)
        elif opts.preview:
            if opts.cov:
                fitdriver.show_cov()
            preview(problem, view=opts.view)
        elif opts.resynth > 0:
            resynth(fitdriver, problem, mapper, opts)

        elif opts.remote:
            # Check that problem runs before submitting it remotely
            # TODO: this may fail if problem requires remote resources such as GPU
            print("initial chisq:", problem.chisq_str())
            job = start_remote_fit(problem, opts,
                                   queue=opts.queue, notify=opts.notify)
            print("remote job:", job['id'])

        else:
            # Show command line arguments and initial model
            print("#", " ".join(options), "--seed=%d" % opts.seed)
            problem.show()

            # Check that there are parameters to be fitted.
            if not len(problem.getp()):
                print("\n!!! No parameters selected for fitting---abort !!!\n")
                return

            # Run the fit
            if opts.resume == '-':
                opts.resume = opts.store if os.path.exists(opts.store) else None
            if opts.resume:
                resume_path = os.path.join(opts.resume, problem.name)
            else:
                resume_path = None

            make_store(problem, opts, exists_handler=store_overwrite_query)

            # Redirect sys.stdout to capture progress
            if opts.batch:
                sys.stdout = open(problem.output_path + ".mon", "w")

            # TODO: fix techical debt with checkpoint monitor implementation
            # * The current checkpoint implementation is self-referential:
            #     checkpoint = lambda: save_best(fitdriver, ...)
            #     fitdriver.monitors = [..., CheckpointMonitor(checkpoint), ...]
            #   It is done this way because the checkpoint monitor needs the fitter
            #   so it can ask it to save state, but the fitter needs the list of
            #   monitors, including the checkpoint monitor, before it is run.
            # * Figures are cumulative, with each checkpoint adding a new set
            # * Figures are slow! Can they go into a separate thread?  Can we
            #   have the problem cache the best value?
            checkpoint_time = float(opts.checkpoint) * 3600

            def checkpoint(history):
                problem = fitdriver.problem
                ## Use the following to save only the fitter state
                fitdriver.fitter.save(problem.output_path)
                ## Use the following to save the fitter state plus all other
                ## plots and other output files.  This won't work yet since
                ## plots are generated sequentially, with each checkpoint producing
                ## a completely new set of plots.
                # best = history.point[0]
                # save_best(fitdriver, problem, best, view=opts.view)

            monitors = [ConsoleMonitor(problem)]
            if checkpoint_time > 0 and np.isfinite(checkpoint_time):
                mon = CheckpointMonitor(checkpoint, progress=checkpoint_time)
                monitors.append(mon)
            if opts.stepmon:
                fid = open(problem.output_path + '.log', 'w')
                mon = StepMonitor(problem, fid, fields=['step', 'value'])
                monitors.append(mon)
            fitdriver.monitors = monitors

            # import time; t0=time.clock()
            cpus = int(opts.parallel) if opts.parallel != "" else 0
            fitdriver.mapper = mapper.start_mapper(problem, opts.args, cpus=cpus)
            best, fbest = fitdriver.fit(resume=resume_path)
            # print("time=%g"%(time.clock()-t0),file=sys.__stdout__)
            # Note: keep this in sync with the checkpoint function above
            save_best(fitdriver, problem, best, view=opts.view)
            if opts.err or opts.cov:
                fitdriver.show_err()
            if opts.cov:
                fitdriver.show_cov()
            if opts.entropy:
                fitdriver.show_entropy(opts.entropy)
            mapper.stop_mapper(fitdriver.mapper)

            # If in batch mode then explicitly close the monitor file on completion
            if opts.batch:
                sys.stderr.close()
                sys.stderr = sys.__stderr__

    @Slot(int, object, int, int)
    def layer_update_slot(self):
        tempStack: Stack = Stack()
        from app.src.guiUtils.AcuGuiGlobal import AcuGuiGlobal
        i = 0
        for layer in AcuGuiGlobal.currentLayers:
            obj = layer[0]
            thickness = layer[1]
            roughness = layer[2]
            if obj is not None:
                if not (isinstance(obj, Material) or isinstance(obj, SLD) or isinstance(obj, Mixture)):
                    continue

                tempStack.insert(i, obj(thickness, roughness))
                self.layerStack = tempStack
            i += 1
            self._update_reflectivity_plot()
            self._update_sld_plot()

    def _update_reflectivity_plot(self):
        try:
            experiment = Experiment(sample=self.layerStack, probe=self.prob)
            from app.src.guiUtils.AcuGuiGlobal import AcuGuiGlobal
            AcuGuiGlobal.reflectivityDataUpdateSignal.emit(experiment.reflectivity()[0].tolist(), np.log10(experiment.reflectivity()[1].tolist()))
            return
        except (TypeError, ValueError, ZeroDivisionError):
            pass
        except:
            traceback.print_exc()

        from app.src.guiUtils.AcuGuiGlobal import AcuGuiGlobal
        AcuGuiGlobal.reflectivityDataUpdateSignal.emit([], [])

    def _update_sld_plot(self):
        rho = []
        irho = []
        depth = []
        totalThickness = 0

        for i in range(1, len(self.layerStack) - 1):
            layer = self.layerStack[i]
            tempRho = 0
            tempIRho = 0

            try:
                if isinstance(layer.material, SLD):
                    tempRho = layer.material.rho.value
                    tempIRho = layer.material.irho.value
                elif isinstance(layer.material, Material):
                    if layer.material.density > 0:
                        tempRho = layer.material.sld(self.prob)[0][0]
                        tempIRho = layer.material.sld(self.prob)[1]
            except:
                pass

            depth.append(totalThickness)
            totalThickness += layer.thickness.value
            depth.append(totalThickness)
            rho.append(tempRho)
            rho.append(tempRho)
            irho.append(tempIRho)
            irho.append(tempIRho)

        from app.src.guiUtils.AcuGuiGlobal import AcuGuiGlobal
        AcuGuiGlobal.sldDataUpdateSignal.emit(rho, irho, depth)
