__author__ = "Helmy Saker"
__date__ = "6/14/2021"
__copyright__ = "AccuStrata, Inc. 2021"
__project__ = "QtRefl1D"
__license__ = "Released under MIT License"

from typing import Callable, Union

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout


def connect_all_signals(obj: QObject, targetType: type, targetSignal: str, slot: Callable):
    if hasattr(obj, 'children'):
        if hasattr(obj.children(), '__len__'):
            if len(obj.children()) > 1:
                children = obj.children()
                for child in children:
                    if isinstance(child, targetType):
                        if hasattr(child, targetSignal):
                            getattr(child, targetSignal).connect(slot)


def clear_layout(layout: Union[QVBoxLayout, QHBoxLayout]):
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().setLayout(None)
