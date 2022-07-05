__author__ = "Helmy Saker"
__date__ = "5/31/2021"
__copyright__ = "AccuStrata, Inc. 2021"
__project__ = "QtRefl1D"
__license__ = "Released under MIT License"

from typing import Dict, Callable
from PySide6.QtCore import QObject, QEvent


class AcuEventMapper(QObject):
    def __init__(self, callBacks: Dict[str, Callable]):
        super(self.__class__, self).__init__()

        self.toggledSignalMap: Dict[str, Callable] = {
            'periodicTableWindowAction': callBacks['windowActionListener'],
            'layerParametersWindowAction': callBacks['windowActionListener'],
            'layerBuilderWindowAction': callBacks['windowActionListener'],
            'consoleWindowAction': callBacks['windowActionListener'],
            'instrumentsWindowAction': callBacks['windowActionListener'],
        }

        from app.src.guiCore.AcuPeriodicTableWidgetController import AcuPeriodicTableWidgetController
        from app.src.guiCore.AcuLayerBuilderWidgetController import AcuLayerBuilderWidgetController
        self.visibilityChangedSignalMap: Dict[str, Callable] = {
            AcuPeriodicTableWidgetController.__name__: callBacks['dockWidgetVisibilityChanged'],
            AcuLayerBuilderWidgetController.__name__: callBacks['dockWidgetVisibilityChanged'],
        }

        self.signalIndexMap: Dict[int, Dict[str, Callable]] = {
            12: self.toggledSignalMap,
            37: self.visibilityChangedSignalMap,
        }

    def slot_interface(self, *args, **kwargs):
        signalIndex = self.senderSignalIndex()
        if signalIndex in self.signalIndexMap.keys():
            senderName: str = self.sender().objectName()
            if senderName in self.signalIndexMap[signalIndex].keys():
                self.signalIndexMap[signalIndex][senderName](self.sender())

    def event_interface(self, event: QEvent):
        d = dir(event)
        sender = self.sender()
        pass
