__author__ = "Helmy Saker"
__date__ = "6/14/2021"
__copyright__ = "AccuStrata, Inc. 2021"
__project__ = "QtRefl1D"
__license__ = "Released under MIT License"

from typing import List, Optional

from PySide6.QtCore import Slot, QSize, QPoint
from PySide6.QtGui import QDropEvent
from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QListWidgetItem, QSpinBox

from app.res.qss.styleSheet import styleSheetsDict
from app.src.guiCore.AcuLayerParametersWidgetController import AcuLayerParametersWidgetController
from app.src.guiCore.AcuMaterialWidgetController import AcuMaterialWidgetController
from app.src.guiUtils.AcuStaticConsts import MIN_DRAG_ENABLE, DRAG_SAFE_MARGIN
from app.src.utils.acuUtils import load_qt_ui


class AcuLayerBuilderWidgetController(QWidget):

    def __init__(self):
        super(AcuLayerBuilderWidgetController, self).__init__()
        load_qt_ui(self, "layerBuilderWidget")
        self.setStyleSheet(styleSheetsDict['widgets'])

        self.activeLayers: List[AcuLayerParametersWidgetController] = []

        self.layersListWidget: QListWidget = self.layersListWidget
        self.addLayerButton: QPushButton = self.addLayerButton

        self.initialized: bool = False
        self.selectedItem: Optional[QListWidgetItem] = None

        self.layersListWidget.currentItemChanged.connect(self.layer_item_selected_slot)
        self.defaultDropEventHandler = self.layersListWidget.dropEvent
        self.layersListWidget.dropEvent = self.drop_event_handler
        self.init_layers_list()

        self.addLayerButton.clicked.connect(self.add_layer_button_clicked_slot)

    def init_layers_list(self):
        self.add_layer_button_clicked_slot()
        self.add_layer_button_clicked_slot()

        firstWidget: AcuLayerParametersWidgetController = self.layersListWidget.itemWidget(self.layersListWidget.item(0))
        firstWidget.removeButton.setDisabled(True)
        firstWidget.removeButton.setVisible(False)
        firstWidget.thicknessSpinBox.setDisabled(True)
        firstWidget.thicknessSpinBox.setVisible(False)
        firstWidget.thicknessLabel.setVisible(False)
        firstWidget.setAcceptDrops(False)
        firstWidget.nameLineEdit.setText("Atmosphere")
        firstWidget.typeComboBox.setCurrentIndex(firstWidget.typeComboBox.findText('SLD'))

        lastWidget: AcuLayerParametersWidgetController = self.layersListWidget.itemWidget(self.layersListWidget.item(1))
        lastWidget.removeButton.setDisabled(True)
        lastWidget.removeButton.setVisible(False)
        lastWidget.thicknessSpinBox.setDisabled(True)
        lastWidget.thicknessSpinBox.setVisible(False)
        lastWidget.thicknessLabel.setVisible(False)
        lastWidget.roughnessSpinBox.setDisabled(True)
        lastWidget.roughnessSpinBox.setVisible(False)
        lastWidget.roughnessLabel.setVisible(False)
        lastWidget.setAcceptDrops(False)
        lastWidget.nameLineEdit.setText("Substrate")
        lastWidget.typeComboBox.setCurrentIndex(lastWidget.typeComboBox.findText('Material'))

        if isinstance(lastWidget.currentEditorWidget, AcuMaterialWidgetController):
            lastWidget.currentEditorWidget.formulaTextEdit.setPlainText('Si')

        self.initialized = True

    def drop_event_handler(self, event: QDropEvent):
        if self.selectedItem is None:
            return

        pos: QPoint = event.pos()

        if (self.selectedItem is self.layersListWidget.item(0) or
                self.selectedItem is self.layersListWidget.item(self.layersListWidget.count() - 1)):
            return

        if self.layersListWidget.itemWidget(self.selectedItem) is None:
            return

        if (self.layersListWidget.itemAt(pos) is not None and
                abs(pos.y() - self.layersListWidget.itemWidget(self.selectedItem).pos().y()) > MIN_DRAG_ENABLE):
            if self.layersListWidget.itemAt(pos) is self.layersListWidget.item(0):
                if (pos.y() < self.layersListWidget.itemWidget(self.layersListWidget.itemAt(pos)).pos().y() +
                        self.layersListWidget.itemWidget(
                            self.layersListWidget.itemAt(pos)).height() - DRAG_SAFE_MARGIN):
                    return
            elif self.layersListWidget.itemAt(pos) is self.layersListWidget.item(self.layersListWidget.count() - 1):
                if pos.y() > self.layersListWidget.itemWidget(
                        self.layersListWidget.itemAt(pos)).pos().y() + DRAG_SAFE_MARGIN:
                    return

            self.defaultDropEventHandler(event)

            if self.initialized:
                self.layer_changed_slot()
            return

        event.ignore()

    def add_layer_button_clicked_slot(self):
        print("Add Layer")
        layerItem = QListWidgetItem()
        layerWidget = AcuLayerParametersWidgetController(layerItem)
        layerWidget.layerParametersChangedSignal.connect(self.layer_changed_slot)
        layerWidget.adjustSize()
        layerItem.setSizeHint(layerWidget.size())
        layerWidget.removeSignal.connect(self.layer_parameters_remove_slot)
        layerWidget.layerTypeChangedSignal.connect(self.layer_type_changed_slot)
        self.layersListWidget.insertItem(self.layersListWidget.count() - 1, layerItem)
        self.layersListWidget.setItemWidget(layerItem, layerWidget)

        from app.src.guiUtils.AcuGuiGlobal import AcuGuiGlobal
        AcuGuiGlobal.guiLayersCount += 1

        if self.initialized:
            self.layer_changed_slot()

    @Slot(QListWidgetItem)
    def layer_parameters_remove_slot(self, layerItem: QListWidgetItem):
        row = self.layersListWidget.row(layerItem)
        from app.src.guiUtils.AcuGuiGlobal import AcuGuiGlobal
        AcuGuiGlobal.guiLayersCount -= 1

        self.layersListWidget.removeItemWidget(layerItem)
        self.layersListWidget.model().removeRow(row)

        self.layer_changed_slot()

    @Slot(QListWidgetItem)
    def layer_type_changed_slot(self, layerItem: QListWidgetItem):
        widget = self.layersListWidget.itemWidget(layerItem)

        if widget.editorHBox.itemAt(0) is not None:
            widget.editorHBox.itemAt(0).widget().adjustSize()
            height = widget.editorHBox.itemAt(0).widget().height()
        else:
            if widget.currentEditorWidget is not None:
                height = -widget.currentEditorWidget.height() - 10
            else:
                height = 0

        widget.adjustSize()
        widget.update()

        layerItem.setSizeHint(QSize(layerItem.sizeHint().width(), widget.size().height() + height))
        self.layersListWidget.adjustSize()

    @Slot(QListWidgetItem)
    def layer_changed_slot(self):
        tempLayers = []
        for i in range(self.layersListWidget.count()):
            widget = self.layersListWidget.itemWidget(self.layersListWidget.item(i))
            if hasattr(widget, 'get_current_representation'):
                tempLayers.append(widget.get_current_representation())

        from app.src.guiUtils.AcuGuiGlobal import AcuGuiGlobal
        AcuGuiGlobal.currentLayers = tempLayers
        AcuGuiGlobal.layerUpdateSignal.emit()

    def layer_item_selected_slot(self, item: QListWidgetItem):
        self.selectedItem = item
