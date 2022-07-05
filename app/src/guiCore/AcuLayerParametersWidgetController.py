__author__ = "Helmy Saker"
__date__ = "6/14/2021"
__copyright__ = "AccuStrata, Inc. 2021"
__project__ = "QtRefl1D"
__license__ = "Released under MIT License"

from typing import Optional, Union, Tuple

from PySide6.QtCore import QEvent, Signal, QSize, Slot
from PySide6.QtGui import QColor, QResizeEvent
from PySide6.QtWidgets import QWidget, QComboBox, QVBoxLayout, QHBoxLayout, QColorDialog, QPushButton, QListWidgetItem, \
    QLineEdit, QSpinBox, QLabel
from refl1d.material import Material, SLD, Mixture

from app.res.qss.styleSheet import styleSheetsDict
from app.src.guiCore.AcuMaterialWidgetController import AcuMaterialWidgetController
from app.src.guiCore.AcuSldWidgetController import AcuSldWidgetController
from app.src.utils.acuUtils import load_qt_ui
from app.src.guiUtils import AcuStaticConsts as Consts


class AcuLayerParametersWidgetController(QWidget):
    removeSignal: Signal = Signal(QListWidgetItem)
    sizeChangedSignal: Signal = Signal(QListWidgetItem, QSize)
    layerTypeChangedSignal: Signal = Signal(QListWidgetItem)
    layerParametersChangedSignal: Signal = Signal()

    def __init__(self, layerItem: QListWidgetItem):
        super(AcuLayerParametersWidgetController, self).__init__()
        load_qt_ui(self, 'layerParameters')
        self.setStyleSheet(styleSheetsDict['widgets'])

        self.layerItem = layerItem
        self.currentLayerTypeIndex = -1
        self.currentEditorWidget: Optional[QWidget] = None
        self.colorDialog: Optional[QColorDialog] = None

        self.mainVBox: QVBoxLayout = self.mainVBox
        self.editorHBox: QHBoxLayout = self.editorHBox
        self.colorButton: QPushButton = self.colorButton
        self.nameLineEdit: QLineEdit = self.nameLineEdit
        self.typeComboBox: QComboBox = self.typeComboBox
        self.removeButton: QPushButton = self.removeButton
        self.thicknessSpinBox: QSpinBox = self.thicknessSpinBox
        self.roughnessSpinBox: QSpinBox = self.roughnessSpinBox
        self.colorLabel: QLabel = self.colorLabel
        self.nameLabel: QLabel = self.nameLabel
        self.thicknessLabel: QLabel = self.thicknessLabel
        self.roughnessLabel: QLabel = self.roughnessLabel
        self.typeLabel: QLabel = self.typeLabel

        self.resizeEvent = self.resize_event_handler

        self.typeComboBox.addItem('')
        self.typeComboBox.addItems(Consts.LAYER_TYPES)
        self.typeComboBox.currentIndexChanged.connect(self.type_combo_box_index_changed_slot)
        self.typeComboBox.adjustSize()

        self.colorButton.setStyleSheet("background-color: #FFFFFF;")

        self.colorButton.clicked.connect(self.color_button_clicked_slot)
        self.removeButton.clicked.connect(self.remove_button_clicked_slot)
        self.nameLineEdit.textChanged.connect(self.name_line_edit_text_changed_slot)
        self.nameLineEdit.editingFinished.connect(self.layer_changed_slot)
        self.thicknessSpinBox.valueChanged.connect(self.layer_changed_slot)
        self.roughnessSpinBox.valueChanged.connect(self.layer_changed_slot)

    def type_combo_box_index_changed_slot(self):
        if self.typeComboBox.currentIndex() != self.currentLayerTypeIndex:
            self.currentLayerTypeIndex = self.typeComboBox.currentIndex()
            if self.editorHBox.itemAt(0) is not None:
                self.currentEditorWidget.parametersChangedSignal.disconnect(self.layer_changed_slot)
                self.currentEditorWidget.close()
                self.editorHBox.removeWidget(self.currentEditorWidget)

            if self.typeComboBox.currentText() == Consts.LAYER_TYPES[0]:
                self.currentEditorWidget = AcuMaterialWidgetController(self.nameLineEdit.text())
                self.currentEditorWidget.setStyleSheet(styleSheetsDict['mainWidget'])
                self.editorHBox.addWidget(self.currentEditorWidget)
                self.currentEditorWidget.parametersChangedSignal.connect(self.layer_changed_slot)
            elif self.typeComboBox.currentText() == Consts.LAYER_TYPES[1]:
                self.currentEditorWidget = AcuSldWidgetController(self.nameLineEdit.text())
                self.currentEditorWidget.setStyleSheet(styleSheetsDict['mainWidget'])
                self.editorHBox.addWidget(self.currentEditorWidget)
                self.currentEditorWidget.parametersChangedSignal.connect(self.layer_changed_slot)

            self.layerTypeChangedSignal.emit(self.layerItem)
            self.layer_changed_slot()

    def color_button_clicked_slot(self):
        self.colorButton.clicked.disconnect(self.color_button_clicked_slot)
        self.colorDialog = QColorDialog(self)
        self.colorDialog.setCurrentColor(QColor(255, 255, 255))
        self.colorDialog.colorSelected.connect(self.color_dialog_color_selected_slot)
        self.colorDialog.currentColorChanged.connect(self.color_dialog_color_changed_slot)
        self.colorDialog.closeEvent = self.color_dialog_close_event_handler
        self.colorDialog.show()

    def color_dialog_color_selected_slot(self):
        self.colorButton.clicked.connect(self.color_button_clicked_slot)
        self._set_color_button_color(self.colorDialog.currentColor().name())
        self.colorDialog = None

    def color_dialog_color_changed_slot(self):
        self._set_color_button_color(self.colorDialog.currentColor().name())

    def color_dialog_close_event_handler(self, event: QEvent):
        self.colorButton.clicked.connect(self.color_button_clicked_slot)
        self._set_color_button_color(self.colorDialog.currentColor().name())
        event.accept()
        self.colorDialog = None

    def name_line_edit_text_changed_slot(self):
        if self.currentEditorWidget is not None:
            if hasattr(self.currentEditorWidget, 'name'):
                self.currentEditorWidget.name = self.nameLineEdit.text()

    def remove_button_clicked_slot(self):
        self.removeSignal.emit(self.layerItem)

    def resize_event_handler(self, event: QResizeEvent):
        self.sizeChangedSignal.emit(self.layerItem, self.size())

    @Slot()
    def layer_changed_slot(self):
        self.layerParametersChangedSignal.emit()

    def get_current_representation(self) -> Tuple[Optional[Union[Material, SLD, Mixture]], int, int]:
        rObj = None
        if isinstance(self.currentEditorWidget, AcuMaterialWidgetController):
            rObj = self.currentEditorWidget.get_material_obj()
        elif isinstance(self.currentEditorWidget, AcuSldWidgetController):
            rObj = self.currentEditorWidget.get_sld_obj()

        return rObj, self.thicknessSpinBox.value(), self.roughnessSpinBox.value()

    def _set_color_button_color(self, color: str):
        self.colorButton.setStyleSheet(f"background-color: {color};")
        self.colorButton.update()


