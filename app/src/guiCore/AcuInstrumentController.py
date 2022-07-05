from PySide6.QtWidgets import QComboBox, QHBoxLayout, QWidget

from app.res.AComboBoxDict import comboBoxDict
from app.res.qss.styleSheet import styleSheetsDict
from app.src.guiCore.AcuProbeParametersWidgetController import AcuProbeParametersWidgetController
from app.src.utils.acuUtils import load_qt_ui


class AcuInstrumentController(QWidget):
    def __init__(self):
        super(AcuInstrumentController, self).__init__()
        load_qt_ui(self, "instrumentWidget")
        self.setStyleSheet(styleSheetsDict['widgets'])

        self.instrumentComboBox: QComboBox = self.instrumentComboBox
        self.instrumentPramHBox: QHBoxLayout = self.instrumentPramHBox

        self.instrumentComboBox.addItems(comboBoxDict['instrumentComboBox'])
        self.instrumentPramHBox.addWidget(AcuProbeParametersWidgetController())
