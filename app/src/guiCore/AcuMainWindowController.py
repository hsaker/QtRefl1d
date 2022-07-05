__author__ = "Helmy Saker"
__date__ = "5/17/2021"
__copyright__ = "AccuStrata, Inc. 2021"
__project__ = "QtRefl1D"
__license__ = "Released under MIT License"

from PySide6 import QtWidgets
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenuBar, QMenu, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout

from app.res.acuCompiledUi import uiDict
from app.res.qss.styleSheet import styleSheetsDict
from app.src.utils.acuUtils import create_module_from_code

mainWindowUi = create_module_from_code('mainwindow', uiDict['mainwindow'])


class AcuMainWindowController(QtWidgets.QMainWindow, mainWindowUi.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        mainWindowUi.Ui_MainWindow.__init__(self)
        self.setStyleSheet(styleSheetsDict['mainWidget'])

        self.setWindowTitle("Qt Refl 1D")

        self.centralwidget: QWidget = self.centralwidget
        self.mainWidget: QWidget = self.mainWidget

        self.centerVBox: QVBoxLayout = self.centerVBox

        self.menuBar: QMenuBar = self.menuBar
        self.menuWidget: QMenu = self.menuWidget