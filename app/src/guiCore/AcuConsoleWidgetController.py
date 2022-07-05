from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPlainTextEdit, QWidget

from app.res.qss.styleSheet import styleSheetsDict
from app.src.utils.acuUtils import load_qt_ui


class AcuConsoleWidgetController(QWidget):
    def __init__(self):
        super(AcuConsoleWidgetController, self).__init__()
        load_qt_ui(self, 'consoleWidget')
        self.setStyleSheet(styleSheetsDict['dialog'])

        self.consoleTextEdit: QPlainTextEdit = self.consoleTextEdit

        from app.src.guiUtils.AcuGuiGlobal import AcuGuiGlobal
        AcuGuiGlobal.consoleTextSignal.connect(self.new_console_text_slot)

    @Slot(str)
    def new_console_text_slot(self, text: str):
        self.consoleTextEdit.appendPlainText(text)