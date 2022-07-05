__author__ = "Helmy Saker"
__date__ = "6/14/2021"
__copyright__ = "AccuStrata, Inc. 2021"
__project__ = "QtRefl1D"
__license__ = "Released under MIT License"


# Layer Parameters Widget
from typing import List
LAYER_TYPES: List[str] = ['Material', 'SLD']

# Layer Builder
MIN_DRAG_ENABLE: int = 35
DRAG_SAFE_MARGIN: int = 5

# Material Widget
FIT_BY_TYPES: List[str] = ['bulk_density', 'natural_density', 'relative_density', 'cell_volume', 'number_density']
FIT_BY_UNITS: List[str] = ['Kg/L', 'Kg/L', '', 'Å3', 'atoms/cm^3']

# Periodic Table Widget
from PySide6.QtCore import QSize
ELEMENT_ICON_SIZE: QSize = QSize(28, 28)
LEGEND_LABEL_SIZE: QSize = QSize(55, 55)

