__author__ = "Helmy Saker"
__date__ = "5/17/2021"
__copyright__ = "AccuStrata, Inc. 2021"
__project__ = "QtRefl1D"
__license__ = "Released under MIT License"

import sys


if __name__ == "__main__":
    if '--uic' in sys.argv:
        from app.src.utils.acuQtResCompiler import compile_qt_ui_files
        compile_qt_ui_files()
    if '--rcc' in sys.argv:
        from app.src.utils.acuQtResCompiler import compile_qt_rc_files
        compile_qt_rc_files()

    from app.src.core.AcuCore import AcuCore
    AcuCore()
    exit(0)
