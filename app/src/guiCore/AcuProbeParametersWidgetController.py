from PySide6.QtWidgets import QWidget

from app.src.utils.acuUtils import load_qt_ui


class AcuProbeParametersWidgetController(QWidget):
    def __init__(self):
        super(AcuProbeParametersWidgetController, self).__init__()
        load_qt_ui(self, 'probeParametersWidget')
