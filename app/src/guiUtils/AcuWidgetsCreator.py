__author__ = "Helmy Saker"
__date__ = "6/14/2021"
__copyright__ = "AccuStrata, Inc. 2021"
__project__ = "QtRefl1D"
__license__ = "Released under MIT License"

import sys
from typing import Dict, Optional, Callable

from PySide6.QtWidgets import QWidget

from app.src.guiCore.AcuConsoleWidgetController import AcuConsoleWidgetController
from app.src.guiCore.AcuInstrumentController import AcuInstrumentController
from app.src.guiCore.AcuLayerBuilderWidgetController import AcuLayerBuilderWidgetController
from app.src.guiCore.AcuLayerParametersWidgetController import AcuLayerParametersWidgetController
from app.src.guiCore.AcuPeriodicTableWidgetController import AcuPeriodicTableWidgetController


class AcuWidgetsCreator:
    SingletonControllers: Dict[str, Optional[QWidget]] = {
        AcuPeriodicTableWidgetController.__name__: None,
        AcuLayerBuilderWidgetController.__name__: None,
        AcuConsoleWidgetController.__name__: None,
        AcuInstrumentController.__name__: None,
    }

    WidgetControllers: Dict[str, Callable] = {
        AcuPeriodicTableWidgetController.__name__: AcuPeriodicTableWidgetController,
        AcuLayerBuilderWidgetController.__name__: AcuLayerBuilderWidgetController,
        AcuLayerParametersWidgetController.__name__: AcuLayerParametersWidgetController,
        AcuConsoleWidgetController.__name__: AcuConsoleWidgetController,
        AcuInstrumentController.__name__: AcuInstrumentController,
    }

    @classmethod
    def make_or_get_widget(cls, widgetName: str, *args) -> Optional[QWidget]:
        if widgetName in cls.SingletonControllers.keys():
            if cls.SingletonControllers[widgetName] is not None:
                return cls.SingletonControllers[widgetName]
            else:
                try:
                    cls.SingletonControllers[widgetName] = cls.WidgetControllers[widgetName](*args)
                    return cls.SingletonControllers[widgetName]
                except:
                    pass
        elif widgetName in cls.WidgetControllers.keys():
            return cls.WidgetControllers[widgetName](*args)
        else:
            return None
