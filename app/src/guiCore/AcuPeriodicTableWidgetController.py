from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap, Qt
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout

from app.res.qss.styleSheet import styleSheetsDict
from app.src.guiUtils.AcuStaticConsts import ELEMENT_ICON_SIZE, LEGEND_LABEL_SIZE
from app.src.utils.acuUtils import load_qt_ui
from app.res import periodicTable


class AcuPeriodicTableWidgetController(QWidget):
    def __init__(self):
        super(AcuPeriodicTableWidgetController, self).__init__()
        load_qt_ui(self, 'periodicTable')
        self.setStyleSheet(styleSheetsDict['widgets'])

        self.tableLegendWidget: QWidget = self.tableLegendWidget
        self.elementsGrid: QGridLayout = self.elementsGrid
        self.numbersGrid: QGridLayout = self.numbersGrid
        self.hideLegendButton: QPushButton = self.hideLegendButton

        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self._init_element_buttons()
        self._init_number_buttons()
        self._init_legend_labels()
        self.hideLegendButton.clicked.connect(self.hide_legend_button_clicked_slot)

    def _init_element_buttons(self):
        for i in range(0, self.elementsGrid.count()):
            child = self.elementsGrid.itemAt(i).widget()
            if isinstance(child, QPushButton):
                name = child.objectName().replace('Button', '')
                child.setFocusPolicy(Qt.FocusPolicy.NoFocus)
                icon = QIcon(QPixmap(f':/periodicTable/{name}.png'))
                if not icon.isNull():
                    child.setIcon(icon)
                    child.setText('')
                    child.setStyleSheet("padding: 0px; background: transparent;")
                child.setIconSize(ELEMENT_ICON_SIZE)
                child.clicked.connect(self.periodic_table_button_slot)

    def _init_number_buttons(self):
        for i in range(0, self.numbersGrid.count()):
            child = self.numbersGrid.itemAt(i).widget()
            if isinstance(child, QPushButton):
                child.setFocusPolicy(Qt.FocusPolicy.NoFocus)
                child.clicked.connect(self.periodic_table_button_slot)

    def _init_legend_labels(self):
        children = self.tableLegendWidget.children()
        for child in children:
            if isinstance(child, QLabel):
                name = child.objectName().replace('Label', '')
                child.setFocusPolicy(Qt.FocusPolicy.NoFocus)

                icon = QIcon(QPixmap(f':/periodicTable/{name}.png'))
                if not icon.isNull():
                    child.setText('')
                    child.setStyleSheet("padding: 0px; background: transparent;")
                    child.setContentsMargins(0, 0, 0, 0)
                    child.setPixmap(icon.pixmap(LEGEND_LABEL_SIZE))
                    child.setMaximumSize(LEGEND_LABEL_SIZE)

    def periodic_table_button_slot(self):
        sender = self.sender()
        from app.src.guiUtils.AcuGuiGlobal import AcuGuiGlobal
        AcuGuiGlobal.periodicTableSignal.emit(sender.objectName().replace('Button', ''))

    def hide_legend_button_clicked_slot(self):
        self.tableLegendWidget.setVisible(not self.tableLegendWidget.isVisible())
