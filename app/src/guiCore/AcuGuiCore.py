__author__ = "Helmy Saker"
__date__ = "5/17/2021"
__copyright__ = "AccuStrata, Inc. 2021"
__project__ = "QtRefl1D"
__license__ = "Released under MIT License"

import traceback
from typing import Dict


from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QDockWidget

from app.src.guiCore.AcuConsoleWidgetController import AcuConsoleWidgetController
from app.src.guiCore.AcuInstrumentController import AcuInstrumentController
from app.src.guiCore.AcuLayerBuilderWidgetController import AcuLayerBuilderWidgetController
from app.src.guiCore.AcuMainWindowController import AcuMainWindowController
from app.src.guiCore.AcuPeriodicTableWidgetController import AcuPeriodicTableWidgetController
from app.src.guiCore.AcuReflectivityPlot import AcuReflectivityPlot
from app.src.guiCore.AcuSldPlot import AcuSldPlot

from app.src.guiUtils.AcuEventMapper import AcuEventMapper
from app.src.guiUtils.AcuGuiGlobal import add_dock_widget, close_dock_widget
from app.src.guiUtils.AcuGuiUtils import connect_all_signals
from app.src.guiUtils.AcuWidgetsCreator import AcuWidgetsCreator


class AcuGuiCore:
    def __init__(self):
        self.mainWindow = AcuMainWindowController()
        self.plotWidget = AcuReflectivityPlot()
        self.sldPlotWidget = AcuSldPlot()

        self.eventMapper = AcuEventMapper({
            'windowActionListener': self.window_action_listener,
            'dockWidgetVisibilityChanged': self.dock_widget_on_visibility_changed
        })

        self.actionWidgetMap: Dict[str, str] = {
            'periodicTableWindowAction': AcuPeriodicTableWidgetController.__name__,
            'layerBuilderWindowAction': AcuLayerBuilderWidgetController.__name__,
            'consoleWindowAction': AcuConsoleWidgetController.__name__,
            'instrumentsWindowAction': AcuInstrumentController.__name__,
        }

        self.widgetActionMap: Dict[str, str] = {
            AcuPeriodicTableWidgetController.__name__: 'periodicTableWindowAction',
            AcuLayerBuilderWidgetController.__name__: 'layerBuilderWindowAction',
            AcuConsoleWidgetController.__name__: 'consoleWindowAction',
            AcuInstrumentController.__name__: 'instrumentsWindowAction',
        }

        self.mainWindow.mainVBox.addWidget(self.plotWidget)
        self.mainWindow.mainVBox.addWidget(self.sldPlotWidget)

        connect_all_signals(self.mainWindow, QAction, 'toggled', self.eventMapper.slot_interface)
        self.mainWindow.show()

        from app.src.guiUtils.AcuGuiGlobal import AcuGuiGlobal
        AcuGuiGlobal.mainWindow = self.mainWindow
        AcuGuiGlobal.eventMapper = self.eventMapper

    def window_action_listener(self, actionObj: QAction):
        actionName = actionObj.objectName()
        if actionName in self.actionWidgetMap.keys():
            from app.src.guiUtils.AcuGuiGlobal import AcuGuiGlobal
            if self.actionWidgetMap[actionName] not in AcuGuiGlobal.currentDockWidgetsMap.keys():
                add_dock_widget(AcuWidgetsCreator.make_or_get_widget(self.actionWidgetMap[actionName]),
                                self.actionWidgetMap[actionName], Qt.RightDockWidgetArea, actionObj.text())
            else:
                close_dock_widget(self.actionWidgetMap[actionName])

    def dock_widget_on_visibility_changed(self, dockWidget: QDockWidget):
        if not dockWidget.isVisible():
            close_dock_widget(dockWidget.objectName())

        if dockWidget.objectName() in self.widgetActionMap.keys():
            action: QAction = getattr(self.mainWindow, self.widgetActionMap[dockWidget.objectName()])

            if not dockWidget.isVisible():
                action.toggled.disconnect(self.eventMapper.slot_interface)
                action.setChecked(False)
                action.toggled.connect(self.eventMapper.slot_interface)
            else:
                action.toggled.disconnect(self.eventMapper.slot_interface)
                action.setChecked(True)
                action.toggled.connect(self.eventMapper.slot_interface)







