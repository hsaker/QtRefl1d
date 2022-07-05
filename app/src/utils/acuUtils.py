__author__ = "Helmy Saker"
__date__ = "5/17/2021"
__copyright__ = "AccuStrata, Inc. 2021"
__project__ = "QtRefl1D"
__license__ = "Released under MIT License"

import os
import sys
from importlib.util import module_from_spec, spec_from_loader

from PySide6.QtWidgets import QWidget

import app
from app.res.acuCompiledUi import uiDict


def singleton(cls):
    return cls()


def app_path(relative_path: str = ""):
    """
    @param relative_path relative path from app dir
    @return path absolute path of app plus relative_path
    """
    base_path = os.path.dirname(app.__file__)
    return os.path.join(base_path, relative_path)


def create_module_from_code(moduleName: str, moduleCode: str):
    module = module_from_spec(spec_from_loader(moduleName, loader=None))
    exec(moduleCode, module.__dict__)
    sys.modules[moduleName] = module

    return module


def load_qt_ui(uiControllerObject, moduleName: str):
    uiModule = create_module_from_code(moduleName, uiDict[moduleName])
    if hasattr(uiModule, 'Ui_Form'):
        form = uiModule.Ui_Form()
        uiModule.Ui_Form.setupUi(form, uiControllerObject)
        uiControllerObject.__dict__.update(form.__dict__)
        return form
    elif hasattr(uiModule, 'Ui_Dialog'):
        dialog = uiModule.Ui_Dialog()
        uiModule.Ui_Dialog.setupUi(dialog, uiControllerObject)
        uiControllerObject.__dict__.update(dialog.__dict__)
        return dialog
