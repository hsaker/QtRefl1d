__author__ = "Helmy Saker"
__date__ = "6/14/2021"
__copyright__ = "AccuStrata, Inc. 2021"
__project__ = "QtRefl1D"
__license__ = "Released under MIT License"

from enum import Enum
from typing import Optional

from PySide6.QtCore import Signal, Qt, Slot
from PySide6.QtGui import QFocusEvent, QTextCharFormat
from PySide6.QtWidgets import QWidget, QDoubleSpinBox, QComboBox, QPushButton, QCheckBox, QPlainTextEdit, QApplication
from pyparsing import ParseException
from refl1d.material import Material

from app.res.qss.styleSheet import styleSheetsDict
from app.src.guiCore.AcuPeriodicTableWidgetController import AcuPeriodicTableWidgetController
from app.src.guiUtils.AcuGuiGlobal import add_dock_widget
from app.src.guiUtils.AcuStaticConsts import FIT_BY_TYPES, FIT_BY_UNITS
from app.src.utils.acuUtils import load_qt_ui


class MaterialValueType(Enum):
    Density = 0
    Natural_Density = 1
    Starting_Value = 2


class AcuMaterialWidgetController(QWidget):
    parametersChangedSignal: Signal = Signal()

    def __init__(self, name: str):
        super(AcuMaterialWidgetController, self).__init__()
        load_qt_ui(self, 'materialWidget')
        self.setStyleSheet(styleSheetsDict['widgets'])

        self.name: str = name
        self.valueType = MaterialValueType.Density

        self.densitySpinBox: QDoubleSpinBox = self.densitySpinBox
        self.naturalDensitySpinBox: QDoubleSpinBox = self.naturalDensitySpinBox
        self.startingValueSpinBox: QDoubleSpinBox = self.startingValueSpinBox
        self.fitByComboBox: QComboBox = self.fitByComboBox
        self.formulaTextEdit: QPlainTextEdit = self.formulaTextEdit
        self.periodicTableButton: QPushButton = self.periodicTableButton
        self.formulaSaveButton: QPushButton = self.formulaSaveButton
        self.formulaLoadButton: QPushButton = self.formulaLoadButton
        self.editLimitsButton: QPushButton = self.editLimitsButton
        self.useIncoherentCheckBox: QCheckBox = self.useIncoherentCheckBox
        self.formulaLoadButton: QPushButton = self.formulaLoadButton
        self.formulaSaveButton: QPushButton = self.formulaSaveButton

        self.useIncoherentCheckBox.setVisible(False)
        self.formulaLoadButton.setVisible(False)
        self.formulaSaveButton.setVisible(False)

        self.periodicTableButton.clicked.connect(self.periodic_table_button_clicked_slot)
        self.densitySpinBox.valueChanged.connect(self.density_spinbox_value_changed_slot)
        self.naturalDensitySpinBox.valueChanged.connect(self.natural_density_spinbox_value_changed_slot)
        self.startingValueSpinBox.valueChanged.connect(self.starting_value_spinbox_value_changed_slot)
        self.fitByComboBox.currentIndexChanged.connect(self.fitby_combobox_current_selection_changed_slot)
        self.useIncoherentCheckBox.stateChanged.connect(self.use_incoherent_checkbox_state_changed_slot)
        self.formulaTextEdit.textChanged.connect(self.formula_textedit_text_changed_slot)

        self.formulaTextEdit.focusInEvent = self.formula_line_edit_focus_in_listener
        self.formulaTextEdit.focusOutEvent = self.formula_line_edit_focus_out_listener

        self._init_fitby_combobox()

    def _init_fitby_combobox(self):
        for i in range(len(FIT_BY_TYPES)):
            self.fitByComboBox.addItem(f'{FIT_BY_TYPES[i].replace("_", " ")}')

    def periodic_table_button_clicked_slot(self):
        from app.src.guiUtils.AcuWidgetsCreator import AcuWidgetsCreator
        add_dock_widget(AcuWidgetsCreator.make_or_get_widget(AcuPeriodicTableWidgetController.__name__),
                        AcuPeriodicTableWidgetController.__name__, Qt.BottomDockWidgetArea)
        self.formulaTextEdit.setFocus()

    def density_spinbox_value_changed_slot(self):
        self.valueType = MaterialValueType.Density
        self.parametersChangedSignal.emit()

    def natural_density_spinbox_value_changed_slot(self):
        self.valueType = MaterialValueType.Natural_Density
        self.parametersChangedSignal.emit()

    def starting_value_spinbox_value_changed_slot(self):
        self.valueType = MaterialValueType.Starting_Value
        self.parametersChangedSignal.emit()

    def fitby_combobox_current_selection_changed_slot(self):
        self.parametersChangedSignal.emit()

    def use_incoherent_checkbox_state_changed_slot(self):
        self.parametersChangedSignal.emit()

    def formula_textedit_text_changed_slot(self):
        if self.formulaTextEdit.toPlainText().endswith('\n'):
            self.formulaTextEdit.undo()
        self.parametersChangedSignal.emit()

    def formula_line_edit_focus_in_listener(self, event: QFocusEvent):
        from app.src.guiUtils.AcuGuiGlobal import AcuGuiGlobal
        AcuGuiGlobal.periodicTableSignal.connect(self.periodic_table_input_slot)

    def formula_line_edit_focus_out_listener(self, event: QFocusEvent):
        from app.src.guiUtils.AcuGuiGlobal import AcuGuiGlobal
        AcuGuiGlobal.periodicTableSignal.disconnect(self.periodic_table_input_slot)

    @Slot(str)
    def periodic_table_input_slot(self, element: str):
        subScript = False

        try:
            int(element)

            if QApplication.queryKeyboardModifiers() != Qt.KeyboardModifier.ShiftModifier:
                subScript = True
        except ValueError:
            pass

        if subScript:
            f = self.formulaTextEdit.textCursor().charFormat()
            f.setVerticalAlignment(QTextCharFormat.AlignSubScript)
            self.formulaTextEdit.setCurrentCharFormat(f)
        else:
            f = self.formulaTextEdit.textCursor().charFormat()
            f.setVerticalAlignment(QTextCharFormat.AlignNormal)
            self.formulaTextEdit.setCurrentCharFormat(f)

        self.formulaTextEdit.insertPlainText(element)

    def get_material_obj(self) -> Optional[Material]:
        m = None
        try:
            if self.valueType == MaterialValueType.Density:
                m = Material(name=self.name,
                             formula=self.formulaTextEdit.toPlainText(),
                             density=self.densitySpinBox.value(),
                             use_incoherent=self.useIncoherentCheckBox.isChecked(),
                             fitby=FIT_BY_TYPES[self.fitByComboBox.currentIndex()])
            elif self.valueType == MaterialValueType.Natural_Density:
                m = Material(name=self.name,
                             formula=self.formulaTextEdit.toPlainText(),
                             natural_density=self.naturalDensitySpinBox.value(),
                             use_incoherent=self.useIncoherentCheckBox.isChecked(),
                             fitby=FIT_BY_TYPES[self.fitByComboBox.currentIndex()])
            elif self.valueType == MaterialValueType.Starting_Value:
                m = Material(name=self.name,
                             formula=self.formulaTextEdit.toPlainText(),
                             value=self.startingValueSpinBox.value(),
                             use_incoherent=self.useIncoherentCheckBox.isChecked(),
                             fitby=FIT_BY_TYPES[self.fitByComboBox.currentIndex()])
        except (ValueError, ParseException, ZeroDivisionError):
            pass
        return m
