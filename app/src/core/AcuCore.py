__author__ = "Helmy Saker"
__date__ = "5/17/2021"
__copyright__ = "AccuStrata, Inc. 2021"
__project__ = "QtRefl1D"
__license__ = "Released under MIT License"

from app.src.core.AcuLogger import AcuLogger

import os.path
import sys

from refl1d.main import setup_bumps


from app.src.core.AcuReflProxy import AcuReflProxy
from app.src.guiCore.AcuGuiCore import AcuGuiCore
from PySide6.QtWidgets import QApplication

from app.src.utils.acuUtils import app_path


class AcuCore:
    def __init__(self):
        self.qApp = QApplication(sys.argv)
        self.guiCore = AcuGuiCore()
        setup_bumps()

        self.qApp.exec()
        self.qApp.quit()
