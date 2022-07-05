__author__ = "Helmy Saker"
__date__ = "7/16/2021"
__copyright__ = "AccuStrata, Inc. 2021"
__project__ = "QtRefl1D"
__license__ = "Released under MIT License"

from typing import Dict

from PySide6.QtCore import Qt, Signal, QObject
from PySide6.QtWidgets import QDockWidget, QWidget

from app.src.guiCore.AcuMainWindowController import AcuMainWindowController
from app.src.guiUtils.AcuEventMapper import AcuEventMapper
from app.src.utils.acuUtils import singleton


@singleton
class AcuGuiGlobal(QObject):
    mainWindow: AcuMainWindowController = None
    eventMapper: AcuEventMapper = None
    currentDockWidgetsMap: Dict[str, QDockWidget] = {}

    guiLayersCount: int = 0

    consoleTextSignal: Signal = Signal(str)
    periodicTableSignal: Signal = Signal(str)

    layerUpdateSignal: Signal = Signal()

    reflectivityDataUpdateSignal: Signal = Signal(list, list)
    sldDataUpdateSignal: Signal = Signal(list, list, list)

    currentLayers: list = []

    def __init__(self):
        super(self.__class__, self).__init__()


def add_dock_widget(widget: QWidget, name: str, dockArea: Qt.DockWidgetArea, title: str = ""):
    if name not in AcuGuiGlobal.currentDockWidgetsMap.keys():
        newDockWidget = QDockWidget()
        newDockWidget.setWindowTitle(title)
        newDockWidget.setWidget(widget)
        newDockWidget.visibilityChanged.connect(AcuGuiGlobal.eventMapper.slot_interface)
        newDockWidget.setObjectName(name)
        AcuGuiGlobal.currentDockWidgetsMap.update({name: newDockWidget})
        AcuGuiGlobal.mainWindow.addDockWidget(dockArea, AcuGuiGlobal.currentDockWidgetsMap[name])
    else:
        close_dock_widget(name)


def close_dock_widget(name: str):
    if name in AcuGuiGlobal.currentDockWidgetsMap.keys():
        if not AcuGuiGlobal.currentDockWidgetsMap[name].isHidden():
            AcuGuiGlobal.currentDockWidgetsMap[name].close()
        if name in AcuGuiGlobal.currentDockWidgetsMap.keys():
            AcuGuiGlobal.currentDockWidgetsMap.pop(name)

