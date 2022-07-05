from cmath import log

import pyqtgraph as pg
import numpy as np
from PySide6.QtCore import Slot
from PySide6.QtGui import QPen
from PySide6.QtWidgets import QWidget, QHBoxLayout
from pyqtgraph import PlotItem, PlotDataItem, GraphicsScene, ViewBox, GraphicsLayoutWidget


class AcuReflectivityPlot(QWidget):
    def __init__(self):
        super(AcuReflectivityPlot, self).__init__()

        self.mainLayout: QHBoxLayout = QHBoxLayout()
        self.graphicsWidget: GraphicsLayoutWidget = GraphicsLayoutWidget()
        self.plot: PlotItem = self.graphicsWidget.addPlot()
        self.sceneObj: GraphicsScene = self.graphicsWidget.sceneObj
        self.viewBox: ViewBox = self.graphicsWidget.addViewBox(col=0, row=0)

        self.plotPen: QPen = pg.mkPen((221, 231, 232, 255), width=1.2)
        self.pen1: QPen = pg.mkPen((0, 0, 0, 255), width=1.0)
        self.pen2: QPen = pg.mkPen((255, 255, 255, 255), width=1.0)
        self.pen3: QPen = pg.mkPen((255, 0, 0, 255), width=1.0)
        self.pen4: QPen = pg.mkPen((0, 255, 0, 255), width=1.0)
        self.pen5: QPen = pg.mkPen((0, 0, 255, 255), width=1.0)

        self.dataset: PlotDataItem = self.plot.plot()

        self._config()

    @Slot(list, list)
    def plot_slot(self, x: list, y: list):
        self.dataset.setData(x, y)
        self.dataset.update()
        self.viewBox.update()

    def _config(self):
        self.graphicsWidget.setBackground((255, 255, 255, 0))
        self.graphicsWidget.setAntialiasing(True)
        self.graphicsWidget.useOpenGL(True)
        self.dataset.setPen(self.plotPen)
        self.plot.showGrid(True, True, 0.5)
        # self.plot.setMouseEnabled(False, False)
        self.plot.setLabel('left', text='Reflectivity')
        self.plot.setLabel('bottom', text='Q')
        # self.viewBox.disableAutoRange()

        from app.src.guiUtils.AcuGuiGlobal import AcuGuiGlobal
        AcuGuiGlobal.reflectivityDataUpdateSignal.connect(self.plot_slot)

        self.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.graphicsWidget)
