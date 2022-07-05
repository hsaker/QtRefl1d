__author__ = "Helmy Saker"
__date__ = "5/17/2021"
__copyright__ = "AccuStrata, Inc. 2021"
__project__ = "QtRefl1D"
__license__ = "Released under MIT License"

from app.res.qss.styleSheetConsts import *
from app.res import icons

styleSheetsDict = dict(mainWidget=f"""
QWidget{{
	background-color: {mainColorDict['mainWidgetBackgroundColor']};
	font: {fontDict['mainWidgetFont']};
	color: {mainColorDict['mainWidgetColor']};
	alternate-background-color: {mainColorDict['mainWidgetAlternateBackgroundColor']};
	border-color: {mainColorDict['mainWidgetBorderColor']};
	gridline-color: {mainColorDict['mainWidgetGridlineColor']};
	selection-background-color: {mainColorDict['mainWidgetSelectionBackgroundColor']};
	selection-color: {mainColorDict['mainWidgetSelectionColor']};
}}

QWidget#dialogWidget{{
background-color: {mainColorDict['widgetBackgroundColor1']};
	font: {fontDict['widgetFont1']};
	color: {mainColorDict['widgetColor1']};
	alternate-background-color: {mainColorDict['widgetAlternateBackgroundColor1']};
	border-color: {mainColorDict['widgetBorderColor1']};
	gridline-color: {mainColorDict['widgetGridlineColor1']};
	selection-background-color: {mainColorDict['widgetSelectionBackgroundColor1']};
	selection-color: {mainColorDict['widgetSelectionColor1']};
	border-radius: {constsDict['borderRadius1']};
}}


QToolBox{{
	color: {mainColorDict['widgetColor2']};	
	background-color: {mainColorDict['widgetBackgroundColor2']};
	border-color: {mainColorDict['widgetBorderColor2']};
	border-style: {constsDict['borderStyle1']};
	border-width: {constsDict['borderWidth1']};
	border-radius: {constsDict['borderRadius2']};
	padding: {constsDict['padding1']};
}}

QToolBox:tab{{
	background-color: {mainColorDict['tabBackgroundColor1']};
	border-style: {constsDict['borderStyle1']};
	border-color: {mainColorDict['tabBorderColor1']};
	border-width: {constsDict['borderWidth2']};
	border-radius: {constsDict['borderRadius3']};
	margin: {constsDict['margin1']};
}}

QToolBox:tab:hover{{
	background-color: {mainColorDict['tabHoverBackgroundColor1']};
    border-style: {constsDict['borderStyle2']};
}}

QToolBox:tab:selected{{
	color: {mainColorDict['tabSelectedBackgroundColor1']};
	background-color: qlineargradient(spread:pad, x1:0.494727, y1:0, x2:0.494682, y2:1, stop:0 rgba(142, 142, 142, 255), stop:0.505682 						rgba(223, 223, 223, 255), stop:1 rgba(126, 126, 126, 255));
    border-style: {constsDict['borderStyle2']};
	font-weight: {fontDict['fontWeight1']};
}}


QTabBar::tab{{
	color: {mainColorDict['tabColor1']};
	background-color: {mainColorDict['tabBackgroundColor1']};
	alternate-background-color: {mainColorDict['tabAlternateBackgroundColor1']};
}}

QTabBar::tab:hover{{
	color: rgb(0, 0, 0);
	background-color: rgb(227, 227, 227);
}}

QTabBar::tab:selected 
{{
    color: rgb(0, 0, 0);
	background-color: qlineargradient(spread:pad, x1:0.494727, y1:0, x2:0.494682, y2:1, stop:0 rgba(142, 142, 142, 255), stop:0.505682 						rgba(223, 223, 223, 255), stop:1 rgba(126, 126, 126, 255));
	font-weight: bold;
	font-size: 9pt;
}}

QTabWidget::pane {{

}}

QPushButton#chemInfoButton:checked:!hover:!disabled{{
	background-color: qlineargradient(spread:pad, x1:0.494727, y1:0, x2:0.494682, y2:1, stop:0 rgba(142, 142, 142, 255), stop:0.505682 						rgba(223, 223, 223, 255), stop:1 rgba(126, 126, 126, 255));
}}

QPushButton#controlsButton:checked:!hover:!disabled{{
	background-color: qlineargradient(spread:pad, x1:0.494727, y1:0, x2:0.494682, y2:1, stop:0 rgba(142, 142, 142, 255), stop:0.505682 						rgba(223, 223, 223, 255), stop:1 rgba(126, 126, 126, 255));
}}

QPushButton#dataButton:checked:!hover:!disabled{{
	background-color: qlineargradient(spread:pad, x1:0.494727, y1:0, x2:0.494682, y2:1, stop:0 rgba(142, 142, 142, 255), stop:0.505682 						rgba(223, 223, 223, 255), stop:1 rgba(126, 126, 126, 255));
}}

QPushButton#postAnalysisButton:checked:!hover:!disabled{{
	background-color: qlineargradient(spread:pad, x1:0.494727, y1:0, x2:0.494682, y2:1, stop:0 rgba(142, 142, 142, 255), stop:0.505682 						rgba(223, 223, 223, 255), stop:1 rgba(126, 126, 126, 255));
}}

QPushButton{{
	background-color: rgb(106, 106, 106);
	color: rgb(255, 255, 255);
	border-style: outset;
	border-color: rgb(102, 102, 102);
	border-width: 1.3px;
	border-radius: 2px;
	margin: 1px;
	padding: 3px;
}}

QPushButton:hover {{
	background-color: rgb(157,171,176);
    border-style: inset;
}}

QPushButton:pressed {{
	color: rgb(39, 39, 39);
	background-color: rgb(220, 225, 227);
    border-style: inset;
}}

QPushButton:checked:!hover:!disabled{{
	color: rgb(39, 39, 39);
	background-color: rgb(220, 225, 227);
	border-color: rgb(95, 90, 90) ;
    border-style: inset;
	font-weight: bold;	
	font-size: 9pt;
}}

QPushButton:disabled {{
	color: rgb(170, 170, 170);
	background-color: rgb(210, 210, 210);
}}

QHeaderView::section {{
	background-color: rgb(230, 230, 230);
	color: rgb(45, 45, 45);
    padding: 1px;
	font: 75 10pt "Arial";
}}

QHeaderView::section:hover {{
	background-color: rgb(200, 200, 200);
	color: rgb(45, 45, 45);
}}

QHeaderView::section:checked {{
	background-color: rgb(185, 185, 185);
	color: rgb(45, 45, 45);
	border-color:  rgb(175, 175, 175);
	border-width: 1px;
	border-style: inset;
}}

QTableWidget QTableCornerButton::section {{
   background-color: rgb(230, 230, 230);
}}

QTableWidget QTableCornerButton::section {{
   background-color: rgb(230, 230, 230);
}}


QScrollBar::add-page, QScrollBar::sub-page {{
	background-color: rgb(185, 185, 185);
}}

QComboBox, QDateEdit, QTextEdit, QSpinBox, QDoubleSpinBox, QLineEdit, QDateTimeEdit{{
	background: rgb(80,80,80);
	border: 1px solid #666666;
	border-style: outset;
	border-radius: 2px;
	min-width: 5em;
}}

QComboBox:disabled, QDateEdit:disabled, QTextEdit:disabled, QSpinBox:disabled, QDoubleSpinBox:disabled, QLineEdit:disabled, QDateTimeEdit:disabled{{
	background: rgb(210, 210, 210);
	color:  rgb(170, 170, 170);
	border-style: inset;
}}

QComboBox:hover, QDateEdit:hover, QTextEdit:hover, QSpinBox:hover, QDoubleSpinBox:hover, QLineEdit:hover, QDateTimeEdit:hover{{
	background: rgb(100, 100, 100);
	border-style: inset;
}}

QComboBox:pressed, QDateEdit:pressed, QTextEdit:pressed, QSpinBox:pressed, QDoubleSpinBox:pressed, QLineEdit:pressed, QDateTimeEdit:pressed{{
	background: rgb(105, 105, 105);
	border-style: inset;
}}

QCheckBox::indicator{{
	background-color: rgb(220, 220, 220);
	border: 1px solid  rgb(120, 120, 120);
	border-radius: 2px;
	border-style: outset;
}}

QCheckBox::indicator:hover{{
	background-color: rgb(185, 185, 185);
	border: 1px solid  rgb(120, 120, 120);
	border-radius: 2px;
	border-style: inset;
}}

QCheckBox::indicator:checked:!hover{{
	image: url(:/icon/check_e.png);
	background-color: rgb(220, 220, 220);
	border: 1px solid  rgb(90, 90, 90);
	border-radius: 2px;
	border-style: inset;
}}

QCheckBox::indicator:checked{{
	image: url(:/icon/check_e.png);
}}


QCheckBox:disabled{{
	color:  rgb(170, 170, 170);
}}

QCheckBox::indicator:disabled{{
	background-color: rgb(85, 85, 85);
	border: 1px solid  rgb(110, 110, 110);
	border-radius: 2px;
}}

QCheckBox::indicator:disabled:checked{{
	image: url(:/icon/check_d.png);
	background-color: rgb(85, 85, 85);
	border: 1px solid  rgb(110, 110, 110);
	border-radius: 2px;
}}

QSlider::handle{{
	background-color: rgb(210, 149, 0, 205);
}}

QSlider::handle:hover{{
	background-color: rgb(255, 228, 166, 205);
}}

QSlider::handle:pressed{{
	background-color: rgb(246, 255, 253, 205);
}}


QProgressBar {{
	background-color: rgb(75, 75, 75);
    border: 1px solid  rgb(160, 160, 160);
    border-radius: 2px;
	padding: 1px;
}}

QProgressBar::chunk {{
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.807, y2:1, stop:0 rgba(102, 162, 175, 255), stop:0.5 rgba(152, 182, 193, 255), stop:1 rgba(102, 162, 175, 255));
	border-radius: 4px;
}}


QPushButton#hideButton{{
	background-color: rgb(70, 70, 70);
	color: rgb(255, 255, 255);
	border-style: outset;
	border-color: rgb(100, 100, 100);
	border-width: 1px;
	border-radius: 1px;
}}

QPushButton:hover#hideButton {{
	background-color: rgb(90,90,90);
    border-style: inset;
}}

QPushButton:pressed#hideButton {{
	color: rgb(39, 39, 39);
	background-color: rgb(220, 225, 227);
    border-style: inset;
}}


QWidget#controlBarWidget{{
	background-color: qlineargradient(spread:pad, x1:0.455, y1:0, x2:0.471591, y2:1, stop:0 rgba(55, 55, 55, 255), stop:0.488636 rgba(110, 110, 110, 255), stop:1 rgba(55, 55, 55, 255));
	color: rgb(255, 255, 255);
	border-style: inset;
	border-color: rgb(80, 80, 80);
	border-width: 1.5px;
	border-radius: 1.5px;
}}

QLabel#title1{{
	font-weight: bold;
	font-size: 11pt;
	margin: 2px;
}}

QLabel#red{{
	background-color: rgb(106, 56, 58);
}}

QLabel#green{{
	background-color: rgb(45, 110, 61);
}}

QLabel#blue{{
	background-color: rgb(84, 100, 105);
}}

""",
                       widgets="""
QWidget{
	background-color: rgb(60,60,60);
	font: 10pt "Arial"
}

QWidget#widget{
color: rgb(255, 255, 255);
background-color: rgb(72,72,72);
alternate-background-color: rgb(63, 63, 63);
border-color: rgb(160, 160, 160);
border-style: inset;
border-width: 2px;
border-radius: 2px;
}

QWidget#widget QLabel, QWidget#widget QRadioButton{
background-color: rgb(72,72,72);
}

QWidget#mainWidget{
color: rgb(255, 255, 255);
background-color: rgb(60,60,60);
alternate-background-color: rgb(65, 65, 65);
border-color: rgb(160, 160, 160);
border-style: inset;
border-width: 2px;
border-radius: 2px;
}



QWidget#tableWidget{
color: rgb(255, 255, 255);
background-color: rgb(60,60,60);
alternate-background-color: rgb(65, 65, 65);
border-color: rgb(160, 160, 160);
}

QWidget#infoWidget, QToolBox#toolBox{
color: rgb(255, 255, 255);
background-color: rgb(60,60,60);
alternate-background-color: rgb(65, 65, 65);
}


QPushButton#hideButton{
	background-color: rgb(70, 70, 70);
	color: rgb(255, 255, 255);
	border-style: outset;
	border-color: rgb(100, 100, 100);
	border-width: 1px;
	border-radius: 1px;
}
QPushButton:hover#hideButton {
	background-color: rgb(90,90,90);
    border-style: inset;
}
QPushButton:pressed#hideButton {
	color: rgb(39, 39, 39);
	background-color: rgb(220, 225, 227);
    border-style: inset;
}



QPushButton{
	background-color: rgb(106, 106, 106);
	color: rgb(255, 255, 255);
	border-style: outset;
	border-color: rgb(102, 102, 102);
	border-width: 1.3px;
	border-radius: 2px;
	margin: 1px;
	padding: 3px;
}
QPushButton:hover {
	background-color: rgb(157,171,176);
    border-style: inset;
}
QPushButton:pressed {
	color: rgb(39, 39, 39);
	background-color: rgb(220, 225, 227);
    border-style: inset;
}
QPushButton:checked:!hover:!disabled{
	color: rgb(39, 39, 39);
	background-color: rgb(220, 225, 227);
	border-color: rgb(95, 90, 90) ;
    border-style: inset;
	font-weight: bold;	
	font-size: 9pt;
}
QPushButton:disabled {
	color: rgb(170, 170, 170);
	background-color: rgb(210, 210, 210);
}




QHeaderView::section {
	background-color: rgb(230, 230, 230);
	color: rgb(45, 45, 45);
    padding: 1px;
	font: 75 10pt "Arial";
}

QHeaderView::section:hover {
	background-color: rgb(200, 200, 200);
	color: rgb(45, 45, 45);
}

QHeaderView::section:checked {
	background-color: rgb(185, 185, 185);
	color: rgb(45, 45, 45);
	border-color:  rgb(175, 175, 175);
	border-width: 1px;
	border-style: inset;
}

QTableWidget QTableCornerButton::section {
   background-color: rgb(230, 230, 230);
}

QTableWidget QTableCornerButton::section {
   background-color: rgb(230, 230, 230);
}


QScrollBar::add-page, QScrollBar::sub-page {
	background-color: rgb(185, 185, 185);
}

QComboBox, QDateEdit, QTextEdit, QSpinBox, QDoubleSpinBox, QLineEdit, QDateTimeEdit{
	background: rgb(80,80,80);
	border: 1px solid #666666;
	border-style: outset;
	border-radius: 2px;
	min-width: 5em;
}

QComboBox:disabled, QDateEdit:disabled, QTextEdit:disabled, QSpinBox:disabled, QDoubleSpinBox:disabled, QLineEdit:disabled, QDateTimeEdit:disabled{
	background: rgb(210, 210, 210);
	color:  rgb(170, 170, 170);
	border-style: inset;
}

QComboBox:hover, QDateEdit:hover, QTextEdit:hover, QSpinBox:hover, QDoubleSpinBox:hover, QLineEdit:hover, QDateTimeEdit:hover{
	background: rgb(100, 100, 100);
	border-style: inset;
}

QComboBox:pressed, QDateEdit:pressed, QTextEdit:pressed, QSpinBox:pressed, QDoubleSpinBox:pressed, QLineEdit:pressed, QDateTimeEdit:pressed{
	background: rgb(105, 105, 105);
	border-style: inset;
}


QCheckBox::indicator{
	background-color: rgb(220, 220, 220);
	border: 1px solid  rgb(120, 120, 120);
	border-radius: 2px;
	border-style: outset;
}

QCheckBox::indicator:hover{
	background-color: rgb(185, 185, 185);
	border: 1px solid  rgb(120, 120, 120);
	border-radius: 2px;
	border-style: inset;
}

QCheckBox::indicator:checked:!hover{
	image: url(:/icon/check_e.png);
	background-color: rgb(220, 220, 220);
	border: 1px solid  rgb(90, 90, 90);
	border-radius: 2px;
	border-style: inset;
}

QCheckBox::indicator:checked{
	image: url(:/icon/check_e.png);
}


QCheckBox:disabled{
	color:  rgb(170, 170, 170);
}
QCheckBox::indicator:disabled{
	background-color: rgb(85, 85, 85);
	border: 1px solid  rgb(110, 110, 110);
	border-radius: 2px;
}
QCheckBox::indicator:disabled:checked{
	image: url(:/icon/check_d.png);
	background-color: rgb(85, 85, 85);
	border: 1px solid  rgb(110, 110, 110);
	border-radius: 2px;
}


QSlider::handle{
	background-color: rgb(210, 149, 0, 205);
}
QSlider::handle:hover{
	background-color: rgb(255, 228, 166, 205);
}
QSlider::handle:pressed{
	background-color: rgb(246, 255, 253, 205);
}


QProgressBar {
	background-color: rgb(75, 75, 75);
    border: 1px solid  rgb(160, 160, 160);
    border-radius: 2px;
	padding: 1px;
}

QProgressBar::chunk {
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.807, y2:1, stop:0 rgba(102, 162, 175, 255), stop:0.5 rgba(152, 182, 193, 255), stop:1 rgba(102, 162, 175, 255));
	border-radius: 4px;
}

QLabel#title1{
	font-weight: bold;
	font-size: 11pt;
	margin: 2px;
}
QLabel#red{
	background-color: rgb(106, 56, 58);
}
QLabel#green{
	background-color: rgb(45, 110, 61);
}
QLabel#blue{
	background-color: rgb(84, 100, 105);
}
""",
                       dialog="""
QWidget{
    font: 10pt "Arial";
	color: rgb(255, 255, 255);
}
QWidget#Form{
	background: transparent;
	font: 10pt "Arial";
	color: rgb(255, 255, 255);
}

QWidget#dialogWidget{
    background-color: rgb(70, 70, 72);
	font: 10pt "Arial";
	color: rgb(255, 255, 255);
	alternate-background-color: rgb(57, 57, 57);
	border-color: rgb(160, 160, 160);
	gridline-color: rgb(180,184,186);
	selection-background-color: rgb(215, 225, 225);
	selection-color: rgb(50, 50, 50);
	border-radius: 10px;
}


QToolBox{
	color: rgb(255, 255, 255);	
	background-color: rgb(70, 70, 70);
	border-color: rgb(160, 160, 160);
	border-style: outset;
	border-width: 1.5px;
	border-radius: 1.5px;
	padding: 1px;
}

QToolBox:tab{
	background-color: rgb(106, 106, 106);
	border-style: outset;
	border-color: rgb(102, 102, 102);
	border-width: 1px;
	border-radius: 2px;
	margin: 1px;
}
QToolBox:tab:hover{
	background-color: rgb(157,171,176);
    border-style: inset;
}
QToolBox:tab:selected{
	color: rgb(39, 39, 39);
	background-color: qlineargradient(spread:pad, x1:0.494727, y1:0, x2:0.494682, y2:1, stop:0 rgba(142, 142, 142, 255), stop:0.505682 						rgba(223, 223, 223, 255), stop:1 rgba(126, 126, 126, 255));
    border-style: inset;
	font-weight: bold;
}



QTabBar::tab{
	color: rgb(255, 255, 255);
	background-color: rgb(106, 106, 106);
	alternate-background-color: rgb(232, 232, 232);
}

QTabBar::tab:hover{
	color: rgb(0, 0, 0);
	background-color: rgb(227, 227, 227);
}

QTabBar::tab:selected 
{
    color: rgb(0, 0, 0);
	background-color: qlineargradient(spread:pad, x1:0.494727, y1:0, x2:0.494682, y2:1, stop:0 rgba(142, 142, 142, 255), stop:0.505682 						rgba(223, 223, 223, 255), stop:1 rgba(126, 126, 126, 255));
	font-weight: bold;
	font-size: 9pt;
}

QTabWidget::pane {

}


QPushButton{
	background-color: rgb(106, 106, 106);
	color: rgb(255, 255, 255);
	border-style: outset;
	border-color: rgb(102, 102, 102);
	border-width: 1.3px;
	border-radius: 2px;
	margin: 1px;
	padding: 3px;
}
QPushButton:hover {
	background-color: rgb(157,171,176);
    border-style: inset;
}
QPushButton:pressed {
	color: rgb(39, 39, 39);
	background-color: rgb(220, 225, 227);
    border-style: inset;
}
QPushButton:checked:!hover:!disabled{
	color: rgb(39, 39, 39);
	background-color: rgb(220, 225, 227);
	border-color: rgb(95, 90, 90) ;
    border-style: inset;
	font-weight: bold;	
	font-size: 9pt;
}
QPushButton:disabled {
	color: rgb(170, 170, 170);
	background-color: rgb(210, 210, 210);
}




QHeaderView::section {
	background-color: rgb(230, 230, 230);
	color: rgb(45, 45, 45);
    padding: 1px;
	font: 75 10pt "Arial";
}

QHeaderView::section:hover {
	background-color: rgb(200, 200, 200);
	color: rgb(45, 45, 45);
}

QHeaderView::section:checked {
	background-color: rgb(185, 185, 185);
	color: rgb(45, 45, 45);
	border-color:  rgb(175, 175, 175);
	border-width: 1px;
	border-style: inset;
}

QTableWidget QTableCornerButton::section {
   background-color: rgb(230, 230, 230);
}

QTableWidget QTableCornerButton::section {
   background-color: rgb(230, 230, 230);
}


QScrollBar::add-page, QScrollBar::sub-page {
	background-color: rgb(185, 185, 185);
}

QComboBox, QDateEdit, QTextEdit, QSpinBox, QDoubleSpinBox, QLineEdit, QDateTimeEdit{
	background: rgb(80,80,80);
	border: 1px solid #666666;
	border-style: outset;
	border-radius: 2px;
	min-width: 5em;
}

QComboBox:disabled, QDateEdit:disabled, QTextEdit:disabled, QSpinBox:disabled, QDoubleSpinBox:disabled, QLineEdit:disabled, QDateTimeEdit:disabled{
	background: rgb(210, 210, 210);
	color:  rgb(170, 170, 170);
	border-style: inset;
}

QComboBox:hover, QDateEdit:hover, QTextEdit:hover, QSpinBox:hover, QDoubleSpinBox:hover, QLineEdit:hover, QDateTimeEdit:hover{
	background: rgb(100, 100, 100);
	border-style: inset;
}

QComboBox:pressed, QDateEdit:pressed, QTextEdit:pressed, QSpinBox:pressed, QDoubleSpinBox:pressed, QLineEdit:pressed, QDateTimeEdit:pressed{
	background: rgb(105, 105, 105);
	border-style: inset;
}

QCheckBox::indicator{
	background-color: rgb(220, 220, 220);
	border: 1px solid  rgb(120, 120, 120);
	border-radius: 2px;
	border-style: outset;
}

QCheckBox::indicator:hover{
	background-color: rgb(185, 185, 185);
	border: 1px solid  rgb(120, 120, 120);
	border-radius: 2px;
	border-style: inset;
}

QCheckBox::indicator:checked:!hover{
	image: url(:/icon/check_e.png);
	background-color: rgb(220, 220, 220);
	border: 1px solid  rgb(90, 90, 90);
	border-radius: 2px;
	border-style: inset;
}

QCheckBox::indicator:checked{
	image: url(:/icon/check_e.png);
}


QCheckBox:disabled{
	color:  rgb(170, 170, 170);
}
QCheckBox::indicator:disabled{
	background-color: rgb(85, 85, 85);
	border: 1px solid  rgb(110, 110, 110);
	border-radius: 2px;
}
QCheckBox::indicator:disabled:checked{
	image: url(:/icon/check_d.png);
	background-color: rgb(85, 85, 85);
	border: 1px solid  rgb(110, 110, 110);
	border-radius: 2px;
}


QSlider::handle{
	background-color: rgb(210, 149, 0, 205);
}
QSlider::handle:hover{
	background-color: rgb(255, 228, 166, 205);
}
QSlider::handle:pressed{
	background-color: rgb(246, 255, 253, 205);
}


QProgressBar {
	background-color: rgb(75, 75, 75);
    border: 1px solid  rgb(160, 160, 160);
    border-radius: 2px;
	padding: 1px;
}

QProgressBar::chunk {
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.807, y2:1, stop:0 rgba(102, 162, 175, 255), stop:0.5 rgba(152, 182, 193, 255), stop:1 rgba(102, 162, 175, 255));
	border-radius: 4px;
}



QPushButton#hideButton{
	background-color: rgb(70, 70, 70);
	color: rgb(255, 255, 255);
	border-style: outset;
	border-color: rgb(100, 100, 100);
	border-width: 1px;
	border-radius: 1px;
}
QPushButton:hover#hideButton {
	background-color: rgb(90,90,90);
    border-style: inset;
}
QPushButton:pressed#hideButton {
	color: rgb(39, 39, 39);
	background-color: rgb(220, 225, 227);
    border-style: inset;
}


QWidget#controlBarWidget{
	background-color: qlineargradient(spread:pad, x1:0.455, y1:0, x2:0.471591, y2:1, stop:0 rgba(55, 55, 55, 255), stop:0.488636 rgba(110, 110, 110, 255), stop:1 rgba(55, 55, 55, 255));
	color: rgb(255, 255, 255);
	border-style: inset;
	border-color: rgb(80, 80, 80);
	border-width: 1.5px;
	border-radius: 1.5px;
}

QLabel#title1{
	font-weight: bold;
	font-size: 11pt;
	margin: 2px;
}

QLabel#messageLabel{
	font-size: 13pt;
	margin: 3px;
}

QLabel#red{
	background-color: rgb(106, 56, 58);
}
QLabel#green{
	background-color: rgb(45, 110, 61);
}
QLabel#blue{
	background-color: rgb(84, 100, 105);
}

""")

