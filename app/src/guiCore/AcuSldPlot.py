__author__ = "Helmy Saker"
__date__ = "8/15/2021"
__copyright__ = "AccuStrata, Inc. 2021"
__project__ = "QtRefl1D"
__license__ = "Released under MIT License"

from PySide6.QtCore import Slot
from PySide6.QtGui import QPen
from PySide6.QtWidgets import QWidget, QHBoxLayout
import pyqtgraph as pg
from pyqtgraph import GraphicsLayoutWidget, PlotItem, GraphicsScene, ViewBox, PlotDataItem


class AcuSldPlot(QWidget):
    def __init__(self):
        super(AcuSldPlot, self).__init__()

        self.mainLayout: QHBoxLayout = QHBoxLayout()
        self.graphicsWidget: GraphicsLayoutWidget = GraphicsLayoutWidget()
        self.rhoPlot: PlotItem = self.graphicsWidget.addPlot()
        self.irhoPlot: PlotItem = self.graphicsWidget.addPlot()
        self.sceneObj: GraphicsScene = self.graphicsWidget.sceneObj
        self.viewBox: ViewBox = self.graphicsWidget.addViewBox(col=0, row=0)

        self.plotPen: QPen = pg.mkPen((221, 231, 232, 255), width=1.2)
        self.pen1: QPen = pg.mkPen((0, 0, 0, 255), width=1.0)
        self.pen2: QPen = pg.mkPen((255, 255, 255, 255), width=1.0)
        self.pen3: QPen = pg.mkPen((255, 0, 0, 255), width=1.0)
        self.pen4: QPen = pg.mkPen((0, 255, 0, 255), width=1.0)
        self.pen5: QPen = pg.mkPen((0, 0, 255, 255), width=1.0)

        self.rhoDataset: PlotDataItem = self.rhoPlot.plot()
        self.irhoDataset: PlotDataItem = self.irhoPlot.plot()

        self._config()

    @Slot(list, list, list)
    def plot_slot(self, rho: list, irho: list, depth: list):
        self.rhoDataset.setData(depth, rho)
        self.irhoDataset.setData(depth, irho)
        self.rhoDataset.update()
        self.irhoDataset.update()
        self.viewBox.update()

    def _config(self):
        self.graphicsWidget.setBackground((255, 255, 255, 0))
        self.graphicsWidget.setAntialiasing(True)
        self.graphicsWidget.useOpenGL(True)
        self.rhoDataset.setPen(self.plotPen)
        self.irhoDataset.setPen(self.plotPen)
        self.rhoPlot.showGrid(True, True, 0.5)
        self.rhoPlot.setLabel('left', text='rho')
        self.rhoPlot.setLabel('bottom', text='depth')
        self.irhoPlot.showGrid(True, True, 0.5)
        self.irhoPlot.setLabel('left', text='irho')
        self.irhoPlot.setLabel('bottom', text='depth')
        # self.plot.setMouseEnabled(False, False)
        # self.viewBox.disableAutoRange()

        from app.src.guiUtils.AcuGuiGlobal import AcuGuiGlobal
        AcuGuiGlobal.sldDataUpdateSignal.connect(self.plot_slot)

        self.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.graphicsWidget)