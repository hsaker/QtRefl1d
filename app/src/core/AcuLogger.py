import sys

from app.src.utils.acuUtils import singleton


@singleton
class AcuLogger(object):
    def __init__(self):
        self.stdout = sys.stdout
        sys.stdout = self

    def write(self, text: str):
        self.stdout.write(text)
        from app.src.guiUtils.AcuGuiGlobal import AcuGuiGlobal
        AcuGuiGlobal.consoleTextSignal.emit(text)

    def flush(self):
        self.stdout.flush()