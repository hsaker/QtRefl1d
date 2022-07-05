__author__ = "Helmy Saker"
__date__ = "6/14/2021"
__copyright__ = "AccuStrata, Inc. 2021"
__project__ = "QtRefl1D"
__license__ = "Released under MIT License"

import traceback
from typing import Optional

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QSlider, QLineEdit
from refl1d.material import SLD

from app.res.qss.styleSheet import styleSheetsDict
from app.src.utils.acuUtils import load_qt_ui


class AcuSldWidgetController(QWidget):
    parametersChangedSignal: Signal = Signal()

    def __init__(self, name: str):
        super(AcuSldWidgetController, self).__init__()
        load_qt_ui(self, 'sldWidget')
        self.setStyleSheet(styleSheetsDict['dialog'])

        self.name: str = name

        self.rhoSlider: QSlider = self.rhoSlider
        self.irhoSlider: QSlider = self.irhoSlider
        self.rhoLineEdit: QLineEdit = self.rhoLineEdit
        self.irhoLineEdit: QLineEdit = self.irhoLineEdit

        self.rhoLineEdit.setText(str(float(self.rhoSlider.value()) / 100))
        self.irhoLineEdit.setText(str(float(self.irhoSlider.value()) / 100))

        self.rhoSlider.valueChanged.connect(self.rho_slider_value_changed_slot)
        self.irhoSlider.valueChanged.connect(self.irho_slider_value_changed_slot)

    def rho_slider_value_changed_slot(self):
        self.rhoLineEdit.setText(str(float(self.rhoSlider.value()) / 100))
        self.parametersChangedSignal.emit()

    def irho_slider_value_changed_slot(self):
        self.irhoLineEdit.setText(str(float(self.irhoSlider.value())/100))
        self.parametersChangedSignal.emit()

    def rho_line_edit_text_changed_slot(self):
        self.parametersChangedSignal.emit()

    def irho_line_edit_text_changed_slot(self):
        self.parametersChangedSignal.emit()

    def get_sld_obj(self) -> Optional[SLD]:
        try:
            obj = SLD(name=self.name,
                      rho=float(self.rhoLineEdit.text()),
                      irho=float(self.irhoLineEdit.text()))
            return obj
        except:
            traceback.print_exc()

        return None
