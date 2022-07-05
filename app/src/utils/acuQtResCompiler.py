__author__ = "Helmy Saker"
__date__ = "5/17/2021"
__copyright__ = "AccuStrata, Inc. 2021"
__project__ = "QtRefl1D"
__license__ = "Released under MIT License"

import shutil
import glob
import os
import threading
from subprocess import Popen, PIPE
from typing import List, Union

import PySide6

from app.src.utils.acuUtils import app_path

RES_DIR = 'res'
UI_DIR = 'res/qtui'
QRC_DIRS = ['res/qrc/periodicTable', 'res/qrc/icons']


UI_Dir = app_path(UI_DIR)
OUT_Dir = app_path(RES_DIR)
OUT_UI_DICT = 'acuCompiledUi.py'


def generate_py_from_ui(inDir: str, recursive: bool):
    uiFiles = glob.glob(f'{inDir}/*.ui', recursive=recursive)
    pyside_dir = os.path.dirname(PySide6.__file__)
    if os.name == 'posix':
        exe = os.path.join(f'{pyside_dir}/Qt/libexec', "uic")
    else:
        exe = os.path.join(pyside_dir, "uic")

    for file in uiFiles:
        cmd = [exe] + ['-g', 'python', f'{file}', '-o', f'{file.split(".")[0]}.py']
        print(f'UIC: Compiling {os.path.basename(file)}')
        proc = Popen(cmd, stderr=PIPE)
        out, err = proc.communicate()
        if err:
            msg = err.decode("utf-8")
            command = ' '.join(cmd)
            print(f"Error: {msg}\nwhile executing '{command}'")
        proc.kill()


def generate_py_from_qrc(inDir: str, recursive: bool):
    qrcFiles = glob.glob(f'{inDir}/*.qrc', recursive=recursive)
    pyside_dir = os.path.dirname(PySide6.__file__)
    if os.name == 'posix':
        exe = os.path.join(f'{pyside_dir}/Qt/libexec', "rcc")
    else:
        exe = os.path.join(pyside_dir, "rcc")
    for file in qrcFiles:
        cmd = [exe] + ['-g', 'python', f'{file}', '-o', f'{file.split(".")[0]}.py']
        print(f'RCC: Compiling {os.path.basename(file)}')
        proc = Popen(cmd, stderr=PIPE)

        out, err = proc.communicate()
        if err:
            msg = err.decode("utf-8")
            command = ' '.join(cmd)
            print(f"Error: {msg}\nwhile executing '{command}'")
        proc.kill()


def compile_qt_ui_files(inDir: str = UI_Dir, outDir: str = OUT_Dir, outputFile: str = OUT_UI_DICT, recursive: bool = False):
    generate_py_from_ui(inDir, recursive)

    uiDict = {}
    pyUiFiles = glob.glob(f'{inDir}/*.py')

    for pyFile in pyUiFiles:
        file = open(os.path.join(inDir, pyFile), 'r')
        fileStr = file.read()
        uiDict.update({os.path.basename(pyFile).split(".")[0]: fileStr})

    file = open(os.path.join(outDir, outputFile), 'w')
    file.write("uiDict = " + str(uiDict))

    pyUiFiles = glob.glob(f'{inDir}/*.py')
    for pyFile in pyUiFiles:
        os.remove(os.path.join(inDir, pyFile))


def compile_qt_rc_files(inDirs: Union[str, List[str]] = QRC_DIRS, outDir: str = OUT_Dir, recursive: bool = False):
    if isinstance(inDirs, str):
        inDirs = [inDirs]
    elif isinstance(inDirs, list):
        pass
    else:
        raise AttributeError

    for inDir in inDirs:
        generate_py_from_qrc(app_path(inDir), recursive)
        pyQrcFiles = glob.glob(f'{inDir}/*.py')
        for pyFile in pyQrcFiles:
            if os.path.exists(os.path.join(outDir, os.path.basename(pyFile))):
                os.remove(os.path.join(outDir, os.path.basename(pyFile)))
            shutil.move(pyFile, outDir)

