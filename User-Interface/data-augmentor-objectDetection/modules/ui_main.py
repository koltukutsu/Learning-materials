# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 719)
        MainWindow.setMinimumSize(QSize(1280, 719))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setMinimumSize(QSize(1260, 699))
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 697))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(60, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        self.titleLeftApp.setMinimumSize(QSize(160, 20))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMinimumSize(QSize(160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_75 = QLabel(self.topLogoInfo)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(10, 0, 51, 51))
        self.label_75.setMinimumSize(QSize(51, 51))
        self.label_75.setMaximumSize(QSize(51, 51))
        self.label_75.setPixmap(QPixmap(u":/images/images/images/iconaesk.png"))

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(60, 647))
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMinimumSize(QSize(60, 45))
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(60, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setMinimumSize(QSize(60, 225))
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(60, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(60, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(60, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_new)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(60, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png)")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(60, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setMinimumSize(QSize(60, 45))
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(60, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 697))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 20))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 28))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setMinimumSize(QSize(0, 647))
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setMinimumSize(QSize(0, 135))
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setMinimumSize(QSize(0, 499))
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 481))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setMinimumSize(QSize(0, 10))
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setMinimumSize(QSize(1198, 697))
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(1198, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setMinimumSize(QSize(1061, 50))
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMinimumSize(QSize(1061, 45))
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(127, 50))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setMinimumSize(QSize(1198, 647))
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setMinimumSize(QSize(1198, 622))
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setMinimumSize(QSize(1198, 622))
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(221, 221, 221, 128))
        brush1.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(221, 221, 221, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(221, 221, 221, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.pagesContainer.setPalette(palette)
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(1178, 602))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setAutoFillBackground(False)
        self.home.setStyleSheet(u"background-image: url(:/images/images/images//LOGO.genisbeyaz.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setFont(font)
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(1158, 582))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame = QFrame(self.row_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(1138, 562))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, -30, 1151, 171))
        self.frame_2.setMinimumSize(QSize(1151, 171))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 0))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush4)
        brush5 = QBrush(QColor(221, 221, 221, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        brush6 = QBrush(QColor(221, 221, 221, 128))
        brush6.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        brush7 = QBrush(QColor(221, 221, 221, 128))
        brush7.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.frame_2.setPalette(palette1)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.keras_from = QLineEdit(self.frame_2)
        self.keras_from.setObjectName(u"keras_from")
        self.keras_from.setGeometry(QRect(0, 90, 831, 30))
        self.keras_from.setMinimumSize(QSize(831, 30))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush8 = QBrush(QColor(33, 37, 43, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush8)
        brush9 = QBrush(QColor(255, 121, 198, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        brush10 = QBrush(QColor(255, 255, 255, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
        brush11 = QBrush(QColor(16, 92, 130, 128))
        brush11.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.keras_from.setPalette(palette2)
        self.keras_from.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.keras_to = QLineEdit(self.frame_2)
        self.keras_to.setObjectName(u"keras_to")
        self.keras_to.setGeometry(QRect(-10, 140, 961, 30))
        self.keras_to.setMinimumSize(QSize(961, 30))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette3.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette3.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.keras_to.setPalette(palette3)
        self.keras_to.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.keras_uret = QPushButton(self.frame_2)
        self.keras_uret.setObjectName(u"keras_uret")
        self.keras_uret.setGeometry(QRect(970, 120, 151, 51))
        self.keras_uret.setMinimumSize(QSize(151, 51))
        self.keras_uret.setFont(font)
        self.keras_uret.setCursor(QCursor(Qt.PointingHandCursor))
        self.keras_uret.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.keras_uret.setIcon(icon4)
        self.label_47 = QLabel(self.frame_2)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(0, 120, 79, 19))
        self.label_47.setMinimumSize(QSize(79, 19))
        self.label_48 = QLabel(self.frame_2)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(0, 70, 111, 21))
        self.label_48.setMinimumSize(QSize(111, 21))
        self.label_73 = QLabel(self.frame_2)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(840, 30, 281, 81))
        self.label_73.setMinimumSize(QSize(281, 81))
        self.label_73.setPixmap(QPixmap(u":/images/images/images/kerasLogo.png"))
        self.keras_iterasyon = QLineEdit(self.frame_2)
        self.keras_iterasyon.setObjectName(u"keras_iterasyon")
        self.keras_iterasyon.setGeometry(QRect(450, 50, 71, 31))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette4.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette4.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.keras_iterasyon.setPalette(palette4)
        self.keras_iterasyon.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.keras_img_type = QLineEdit(self.frame_2)
        self.keras_img_type.setObjectName(u"keras_img_type")
        self.keras_img_type.setGeometry(QRect(540, 50, 71, 31))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette5.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette5.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.keras_img_type.setPalette(palette5)
        self.keras_img_type.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.keras_final_type = QLineEdit(self.frame_2)
        self.keras_final_type.setObjectName(u"keras_final_type")
        self.keras_final_type.setGeometry(QRect(660, 50, 71, 31))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette6.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette6.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette6.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette6.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.keras_final_type.setPalette(palette6)
        self.keras_final_type.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.label_76 = QLabel(self.frame_2)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(530, 30, 111, 21))
        self.label_76.setMinimumSize(QSize(111, 21))
        self.label_77 = QLabel(self.frame_2)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(450, 30, 111, 21))
        self.label_77.setMinimumSize(QSize(111, 21))
        self.label_78 = QLabel(self.frame_2)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(660, 30, 111, 21))
        self.label_78.setMinimumSize(QSize(111, 21))
        self.label_79 = QLabel(self.frame_2)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(750, 30, 111, 21))
        self.label_79.setMinimumSize(QSize(111, 21))
        self.keras_cikan_isim = QLineEdit(self.frame_2)
        self.keras_cikan_isim.setObjectName(u"keras_cikan_isim")
        self.keras_cikan_isim.setGeometry(QRect(740, 50, 81, 31))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette7.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette7.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette7.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette7.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.keras_cikan_isim.setPalette(palette7)
        self.keras_cikan_isim.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.row_3 = QFrame(self.frame)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setGeometry(QRect(-10, 190, 1161, 391))
        self.row_3.setMinimumSize(QSize(1161, 391))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.row_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 261, 331))
        self.layoutWidget.setMinimumSize(QSize(261, 331))
        self.verticalLayout_16 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.lbl_1 = QCheckBox(self.layoutWidget)
        self.lbl_1.setObjectName(u"lbl_1")
        self.lbl_1.setMinimumSize(QSize(241, 18))
        self.lbl_1.setMaximumSize(QSize(241, 18))

        self.verticalLayout_16.addWidget(self.lbl_1)

        self.txt_1 = QLineEdit(self.layoutWidget)
        self.txt_1.setObjectName(u"txt_1")
        self.txt_1.setMinimumSize(QSize(241, 19))
        self.txt_1.setMaximumSize(QSize(241, 19))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette8.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette8.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette8.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_1.setPalette(palette8)

        self.verticalLayout_16.addWidget(self.txt_1)

        self.lbl_2 = QCheckBox(self.layoutWidget)
        self.lbl_2.setObjectName(u"lbl_2")
        self.lbl_2.setMinimumSize(QSize(241, 18))
        self.lbl_2.setMaximumSize(QSize(241, 18))

        self.verticalLayout_16.addWidget(self.lbl_2)

        self.txt_2 = QLineEdit(self.layoutWidget)
        self.txt_2.setObjectName(u"txt_2")
        self.txt_2.setMinimumSize(QSize(241, 19))
        self.txt_2.setMaximumSize(QSize(241, 19))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette9.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette9.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_2.setPalette(palette9)

        self.verticalLayout_16.addWidget(self.txt_2)

        self.lbl_3 = QCheckBox(self.layoutWidget)
        self.lbl_3.setObjectName(u"lbl_3")
        self.lbl_3.setMinimumSize(QSize(241, 18))
        self.lbl_3.setMaximumSize(QSize(241, 18))

        self.verticalLayout_16.addWidget(self.lbl_3)

        self.txt_3 = QLineEdit(self.layoutWidget)
        self.txt_3.setObjectName(u"txt_3")
        self.txt_3.setMinimumSize(QSize(241, 19))
        self.txt_3.setMaximumSize(QSize(241, 19))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette10.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette10.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_3.setPalette(palette10)

        self.verticalLayout_16.addWidget(self.txt_3)

        self.lbl_4 = QCheckBox(self.layoutWidget)
        self.lbl_4.setObjectName(u"lbl_4")
        self.lbl_4.setMinimumSize(QSize(241, 18))
        self.lbl_4.setMaximumSize(QSize(241, 18))

        self.verticalLayout_16.addWidget(self.lbl_4)

        self.txt_4 = QLineEdit(self.layoutWidget)
        self.txt_4.setObjectName(u"txt_4")
        self.txt_4.setMinimumSize(QSize(241, 19))
        self.txt_4.setMaximumSize(QSize(241, 19))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette11.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette11.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_4.setPalette(palette11)

        self.verticalLayout_16.addWidget(self.txt_4)

        self.lbl_5 = QCheckBox(self.layoutWidget)
        self.lbl_5.setObjectName(u"lbl_5")
        self.lbl_5.setMinimumSize(QSize(241, 18))
        self.lbl_5.setMaximumSize(QSize(241, 18))

        self.verticalLayout_16.addWidget(self.lbl_5)

        self.txt_5 = QLineEdit(self.layoutWidget)
        self.txt_5.setObjectName(u"txt_5")
        self.txt_5.setMinimumSize(QSize(241, 19))
        self.txt_5.setMaximumSize(QSize(241, 19))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette12.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette12.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette12.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_5.setPalette(palette12)

        self.verticalLayout_16.addWidget(self.txt_5)

        self.lbl_6 = QCheckBox(self.layoutWidget)
        self.lbl_6.setObjectName(u"lbl_6")
        self.lbl_6.setMinimumSize(QSize(241, 18))
        self.lbl_6.setMaximumSize(QSize(241, 18))

        self.verticalLayout_16.addWidget(self.lbl_6)

        self.txt_6 = QLineEdit(self.layoutWidget)
        self.txt_6.setObjectName(u"txt_6")
        self.txt_6.setMinimumSize(QSize(241, 19))
        self.txt_6.setMaximumSize(QSize(241, 19))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette13.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette13.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette13.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette13.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_6.setPalette(palette13)

        self.verticalLayout_16.addWidget(self.txt_6)

        self.layoutWidget1 = QWidget(self.row_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(290, 10, 261, 321))
        self.layoutWidget1.setMinimumSize(QSize(261, 321))
        self.verticalLayout_23 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.lbl_7 = QCheckBox(self.layoutWidget1)
        self.lbl_7.setObjectName(u"lbl_7")
        self.lbl_7.setMinimumSize(QSize(241, 18))
        self.lbl_7.setMaximumSize(QSize(241, 18))

        self.verticalLayout_23.addWidget(self.lbl_7)

        self.txt_7 = QLineEdit(self.layoutWidget1)
        self.txt_7.setObjectName(u"txt_7")
        self.txt_7.setMinimumSize(QSize(241, 19))
        self.txt_7.setMaximumSize(QSize(241, 19))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette14.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette14.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette14.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette14.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_7.setPalette(palette14)

        self.verticalLayout_23.addWidget(self.txt_7)

        self.lbl_8 = QCheckBox(self.layoutWidget1)
        self.lbl_8.setObjectName(u"lbl_8")
        self.lbl_8.setMinimumSize(QSize(241, 18))
        self.lbl_8.setMaximumSize(QSize(241, 18))

        self.verticalLayout_23.addWidget(self.lbl_8)

        self.txt_8 = QLineEdit(self.layoutWidget1)
        self.txt_8.setObjectName(u"txt_8")
        self.txt_8.setMinimumSize(QSize(241, 19))
        self.txt_8.setMaximumSize(QSize(241, 19))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette15.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette15.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette15.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette15.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_8.setPalette(palette15)

        self.verticalLayout_23.addWidget(self.txt_8)

        self.lbl_9 = QCheckBox(self.layoutWidget1)
        self.lbl_9.setObjectName(u"lbl_9")
        self.lbl_9.setMinimumSize(QSize(241, 18))
        self.lbl_9.setMaximumSize(QSize(241, 18))

        self.verticalLayout_23.addWidget(self.lbl_9)

        self.txt_9 = QLineEdit(self.layoutWidget1)
        self.txt_9.setObjectName(u"txt_9")
        self.txt_9.setMinimumSize(QSize(241, 19))
        self.txt_9.setMaximumSize(QSize(241, 19))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette16.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette16.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette16.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette16.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette16.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette16.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_9.setPalette(palette16)

        self.verticalLayout_23.addWidget(self.txt_9)

        self.lbl_10 = QCheckBox(self.layoutWidget1)
        self.lbl_10.setObjectName(u"lbl_10")
        self.lbl_10.setMinimumSize(QSize(241, 22))
        self.lbl_10.setMaximumSize(QSize(241, 22))

        self.verticalLayout_23.addWidget(self.lbl_10)

        self.txt_10 = QLineEdit(self.layoutWidget1)
        self.txt_10.setObjectName(u"txt_10")
        self.txt_10.setMinimumSize(QSize(241, 29))
        self.txt_10.setMaximumSize(QSize(241, 29))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette17.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette17.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette17.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette17.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette17.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette17.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_10.setPalette(palette17)

        self.verticalLayout_23.addWidget(self.txt_10)

        self.lbl_11 = QCheckBox(self.layoutWidget1)
        self.lbl_11.setObjectName(u"lbl_11")
        self.lbl_11.setMinimumSize(QSize(241, 22))
        self.lbl_11.setMaximumSize(QSize(241, 22))

        self.verticalLayout_23.addWidget(self.lbl_11)

        self.txt_11 = QLineEdit(self.layoutWidget1)
        self.txt_11.setObjectName(u"txt_11")
        self.txt_11.setMinimumSize(QSize(241, 29))
        self.txt_11.setMaximumSize(QSize(241, 29))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette18.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette18.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette18.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette18.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette18.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette18.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_11.setPalette(palette18)

        self.verticalLayout_23.addWidget(self.txt_11)

        self.layoutWidget2 = QWidget(self.row_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(560, 10, 241, 321))
        self.layoutWidget2.setMinimumSize(QSize(241, 321))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.layoutWidget2.setPalette(palette19)
        self.verticalLayout_24 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.lbl_12 = QCheckBox(self.layoutWidget2)
        self.lbl_12.setObjectName(u"lbl_12")
        self.lbl_12.setMinimumSize(QSize(190, 22))
        self.lbl_12.setMaximumSize(QSize(190, 22))

        self.verticalLayout_24.addWidget(self.lbl_12)

        self.txt_12 = QLineEdit(self.layoutWidget2)
        self.txt_12.setObjectName(u"txt_12")
        self.txt_12.setMinimumSize(QSize(190, 29))
        self.txt_12.setMaximumSize(QSize(190, 29))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette20.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette20.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette20.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette20.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette20.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette20.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_12.setPalette(palette20)

        self.verticalLayout_24.addWidget(self.txt_12)

        self.lbl_13 = QCheckBox(self.layoutWidget2)
        self.lbl_13.setObjectName(u"lbl_13")
        self.lbl_13.setMinimumSize(QSize(190, 22))
        self.lbl_13.setMaximumSize(QSize(190, 22))

        self.verticalLayout_24.addWidget(self.lbl_13)

        self.txt_13 = QLineEdit(self.layoutWidget2)
        self.txt_13.setObjectName(u"txt_13")
        self.txt_13.setMinimumSize(QSize(190, 29))
        self.txt_13.setMaximumSize(QSize(190, 29))
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette21.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette21.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette21.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette21.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette21.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette21.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_13.setPalette(palette21)

        self.verticalLayout_24.addWidget(self.txt_13)

        self.lbl_14 = QCheckBox(self.layoutWidget2)
        self.lbl_14.setObjectName(u"lbl_14")
        self.lbl_14.setMinimumSize(QSize(190, 18))
        self.lbl_14.setMaximumSize(QSize(190, 18))

        self.verticalLayout_24.addWidget(self.lbl_14)

        self.txt_14 = QLineEdit(self.layoutWidget2)
        self.txt_14.setObjectName(u"txt_14")
        self.txt_14.setMinimumSize(QSize(190, 19))
        self.txt_14.setMaximumSize(QSize(190, 19))
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette22.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette22.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette22.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette22.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette22.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette22.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_14.setPalette(palette22)

        self.verticalLayout_24.addWidget(self.txt_14)

        self.lbl_15 = QCheckBox(self.layoutWidget2)
        self.lbl_15.setObjectName(u"lbl_15")
        self.lbl_15.setMinimumSize(QSize(190, 18))
        self.lbl_15.setMaximumSize(QSize(190, 18))

        self.verticalLayout_24.addWidget(self.lbl_15)

        self.txt_15 = QLineEdit(self.layoutWidget2)
        self.txt_15.setObjectName(u"txt_15")
        self.txt_15.setMinimumSize(QSize(190, 19))
        self.txt_15.setMaximumSize(QSize(190, 19))
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette23.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette23.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette23.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette23.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette23.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette23.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_15.setPalette(palette23)

        self.verticalLayout_24.addWidget(self.txt_15)

        self.lbl_16 = QCheckBox(self.layoutWidget2)
        self.lbl_16.setObjectName(u"lbl_16")
        self.lbl_16.setMinimumSize(QSize(190, 18))
        self.lbl_16.setMaximumSize(QSize(190, 18))

        self.verticalLayout_24.addWidget(self.lbl_16)

        self.txt_16 = QLineEdit(self.layoutWidget2)
        self.txt_16.setObjectName(u"txt_16")
        self.txt_16.setMinimumSize(QSize(190, 19))
        self.txt_16.setMaximumSize(QSize(190, 19))
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette24.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette24.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette24.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette24.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette24.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette24.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_16.setPalette(palette24)

        self.verticalLayout_24.addWidget(self.txt_16)

        self.layoutWidget3 = QWidget(self.row_3)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(820, 10, 301, 341))
        self.layoutWidget3.setMinimumSize(QSize(301, 341))
        self.verticalLayout_25 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.lbl_17 = QCheckBox(self.layoutWidget3)
        self.lbl_17.setObjectName(u"lbl_17")
        self.lbl_17.setMinimumSize(QSize(190, 18))
        self.lbl_17.setMaximumSize(QSize(190, 18))

        self.verticalLayout_25.addWidget(self.lbl_17)

        self.txt_17 = QLineEdit(self.layoutWidget3)
        self.txt_17.setObjectName(u"txt_17")
        self.txt_17.setMinimumSize(QSize(190, 19))
        self.txt_17.setMaximumSize(QSize(190, 19))
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette25.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette25.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette25.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette25.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette25.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette25.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_17.setPalette(palette25)

        self.verticalLayout_25.addWidget(self.txt_17)

        self.lbl_18 = QCheckBox(self.layoutWidget3)
        self.lbl_18.setObjectName(u"lbl_18")
        self.lbl_18.setMinimumSize(QSize(190, 18))
        self.lbl_18.setMaximumSize(QSize(190, 18))

        self.verticalLayout_25.addWidget(self.lbl_18)

        self.txt_18 = QLineEdit(self.layoutWidget3)
        self.txt_18.setObjectName(u"txt_18")
        self.txt_18.setMinimumSize(QSize(190, 19))
        self.txt_18.setMaximumSize(QSize(190, 19))
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette26.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette26.setBrush(QPalette.Active, QPalette.Text, brush)
        palette26.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette26.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette26.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette26.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette26.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette26.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette26.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette26.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette26.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette26.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_18.setPalette(palette26)

        self.verticalLayout_25.addWidget(self.txt_18)

        self.lbl_19 = QCheckBox(self.layoutWidget3)
        self.lbl_19.setObjectName(u"lbl_19")
        self.lbl_19.setMinimumSize(QSize(190, 18))
        self.lbl_19.setMaximumSize(QSize(190, 18))

        self.verticalLayout_25.addWidget(self.lbl_19)

        self.txt_19 = QLineEdit(self.layoutWidget3)
        self.txt_19.setObjectName(u"txt_19")
        self.txt_19.setMinimumSize(QSize(190, 19))
        self.txt_19.setMaximumSize(QSize(190, 19))
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette27.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette27.setBrush(QPalette.Active, QPalette.Text, brush)
        palette27.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette27.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette27.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette27.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette27.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette27.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette27.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette27.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette27.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette27.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_19.setPalette(palette27)

        self.verticalLayout_25.addWidget(self.txt_19)

        self.lbl_20 = QCheckBox(self.layoutWidget3)
        self.lbl_20.setObjectName(u"lbl_20")
        self.lbl_20.setMinimumSize(QSize(190, 18))
        self.lbl_20.setMaximumSize(QSize(190, 18))

        self.verticalLayout_25.addWidget(self.lbl_20)

        self.txt_20 = QLineEdit(self.layoutWidget3)
        self.txt_20.setObjectName(u"txt_20")
        self.txt_20.setMinimumSize(QSize(190, 19))
        self.txt_20.setMaximumSize(QSize(190, 19))
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette28.setBrush(QPalette.Active, QPalette.Text, brush)
        palette28.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette28.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette28.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette28.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette28.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette28.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette28.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette28.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette28.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette28.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_20.setPalette(palette28)

        self.verticalLayout_25.addWidget(self.txt_20)

        self.lbl_21 = QCheckBox(self.layoutWidget3)
        self.lbl_21.setObjectName(u"lbl_21")
        self.lbl_21.setMinimumSize(QSize(190, 18))
        self.lbl_21.setMaximumSize(QSize(190, 18))

        self.verticalLayout_25.addWidget(self.lbl_21)

        self.txt_21 = QLineEdit(self.layoutWidget3)
        self.txt_21.setObjectName(u"txt_21")
        self.txt_21.setMinimumSize(QSize(190, 19))
        self.txt_21.setMaximumSize(QSize(190, 19))
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette29.setBrush(QPalette.Active, QPalette.Text, brush)
        palette29.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette29.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette29.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette29.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette29.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette29.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette29.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette29.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette29.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette29.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_21.setPalette(palette29)

        self.verticalLayout_25.addWidget(self.txt_21)

        self.lbl_22 = QCheckBox(self.layoutWidget3)
        self.lbl_22.setObjectName(u"lbl_22")
        self.lbl_22.setMinimumSize(QSize(190, 18))
        self.lbl_22.setMaximumSize(QSize(190, 18))

        self.verticalLayout_25.addWidget(self.lbl_22)

        self.txt_22 = QLineEdit(self.layoutWidget3)
        self.txt_22.setObjectName(u"txt_22")
        self.txt_22.setMinimumSize(QSize(190, 19))
        self.txt_22.setMaximumSize(QSize(190, 19))
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette30.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette30.setBrush(QPalette.Active, QPalette.Text, brush)
        palette30.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette30.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette30.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette30.setBrush(QPalette.Active, QPalette.Highlight, brush9)
        palette30.setBrush(QPalette.Active, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette30.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette30.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette30.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette30.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette30.setBrush(QPalette.Inactive, QPalette.Highlight, brush9)
        palette30.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette30.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette30.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette30.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette30.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette30.setBrush(QPalette.Disabled, QPalette.Highlight, brush9)
        palette30.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.txt_22.setPalette(palette30)

        self.verticalLayout_25.addWidget(self.txt_22)

        self.keras_temizle = QPushButton(self.frame)
        self.keras_temizle.setObjectName(u"keras_temizle")
        self.keras_temizle.setGeometry(QRect(970, 150, 150, 30))
        self.keras_temizle.setMinimumSize(QSize(150, 30))
        self.keras_temizle.setFont(font)
        self.keras_temizle.setCursor(QCursor(Qt.PointingHandCursor))
        self.keras_temizle.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.keras_temizle.setIcon(icon4)

        self.verticalLayout_19.addWidget(self.frame)


        self.verticalLayout.addWidget(self.row_2)

        self.stackedWidget.addWidget(self.widgets)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.row_4 = QFrame(self.page)
        self.row_4.setObjectName(u"row_4")
        self.row_4.setGeometry(QRect(0, 0, 1158, 582))
        self.row_4.setMinimumSize(QSize(0, 150))
        self.row_4.setFrameShape(QFrame.StyledPanel)
        self.row_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.row_4)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_3 = QFrame(self.row_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 0, 1151, 171))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.augment_from = QLineEdit(self.frame_4)
        self.augment_from.setObjectName(u"augment_from")
        self.augment_from.setGeometry(QRect(0, 30, 411, 30))
        self.augment_from.setMinimumSize(QSize(0, 30))
        self.augment_from.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.augment_to = QLineEdit(self.frame_4)
        self.augment_to.setObjectName(u"augment_to")
        self.augment_to.setGeometry(QRect(0, 80, 411, 30))
        self.augment_to.setMinimumSize(QSize(0, 30))
        self.augment_to.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(970, 110, 151, 51))
        self.pushButton_4.setMinimumSize(QSize(150, 30))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_4.setIcon(icon4)
        self.label_49 = QLabel(self.frame_4)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(0, 60, 79, 19))
        self.label_50 = QLabel(self.frame_4)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(0, 0, 111, 21))
        self.augment_label = QLineEdit(self.frame_4)
        self.augment_label.setObjectName(u"augment_label")
        self.augment_label.setGeometry(QRect(420, 30, 411, 30))
        self.augment_label.setMinimumSize(QSize(0, 30))
        self.augment_label.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.label_101 = QLabel(self.frame_4)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setGeometry(QRect(440, 0, 111, 21))
        self.label_ayni_dosya = QCheckBox(self.frame_4)
        self.label_ayni_dosya.setObjectName(u"label_ayni_dosya")
        self.label_ayni_dosya.setGeometry(QRect(190, 0, 221, 21))
        self.label_ayni_dosya.setLayoutDirection(Qt.RightToLeft)
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-description.png", QSize(), QIcon.Normal, QIcon.Off)
        self.label_ayni_dosya.setIcon(icon5)
        self.label_ayni_dosya.setChecked(True)
        self.row_5 = QFrame(self.frame_3)
        self.row_5.setObjectName(u"row_5")
        self.row_5.setGeometry(QRect(-10, 190, 1161, 391))
        self.row_5.setMinimumSize(QSize(0, 150))
        self.row_5.setFrameShape(QFrame.StyledPanel)
        self.row_5.setFrameShadow(QFrame.Raised)
        self.layoutWidget_5 = QWidget(self.row_5)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(20, 10, 261, 331))
        self.verticalLayout_27 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_51 = QCheckBox(self.layoutWidget_5)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(241, 18))
        self.label_51.setMaximumSize(QSize(241, 18))

        self.verticalLayout_27.addWidget(self.label_51)

        self.text_47 = QLineEdit(self.layoutWidget_5)
        self.text_47.setObjectName(u"text_47")
        self.text_47.setMinimumSize(QSize(241, 19))
        self.text_47.setMaximumSize(QSize(241, 19))

        self.verticalLayout_27.addWidget(self.text_47)

        self.label_52 = QCheckBox(self.layoutWidget_5)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(241, 18))
        self.label_52.setMaximumSize(QSize(241, 18))

        self.verticalLayout_27.addWidget(self.label_52)

        self.text_48 = QLineEdit(self.layoutWidget_5)
        self.text_48.setObjectName(u"text_48")
        self.text_48.setMinimumSize(QSize(241, 19))
        self.text_48.setMaximumSize(QSize(241, 19))

        self.verticalLayout_27.addWidget(self.text_48)

        self.label_53 = QCheckBox(self.layoutWidget_5)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(241, 18))
        self.label_53.setMaximumSize(QSize(241, 18))

        self.verticalLayout_27.addWidget(self.label_53)

        self.text_49 = QLineEdit(self.layoutWidget_5)
        self.text_49.setObjectName(u"text_49")
        self.text_49.setMinimumSize(QSize(241, 19))
        self.text_49.setMaximumSize(QSize(241, 19))

        self.verticalLayout_27.addWidget(self.text_49)

        self.label_54 = QCheckBox(self.layoutWidget_5)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(241, 18))
        self.label_54.setMaximumSize(QSize(241, 18))

        self.verticalLayout_27.addWidget(self.label_54)

        self.text_50 = QLineEdit(self.layoutWidget_5)
        self.text_50.setObjectName(u"text_50")
        self.text_50.setMinimumSize(QSize(241, 19))
        self.text_50.setMaximumSize(QSize(241, 19))

        self.verticalLayout_27.addWidget(self.text_50)

        self.label_55 = QCheckBox(self.layoutWidget_5)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(241, 18))
        self.label_55.setMaximumSize(QSize(241, 18))

        self.verticalLayout_27.addWidget(self.label_55)

        self.text_51 = QLineEdit(self.layoutWidget_5)
        self.text_51.setObjectName(u"text_51")
        self.text_51.setMinimumSize(QSize(241, 19))
        self.text_51.setMaximumSize(QSize(241, 19))

        self.verticalLayout_27.addWidget(self.text_51)

        self.label_56 = QCheckBox(self.layoutWidget_5)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(241, 18))
        self.label_56.setMaximumSize(QSize(241, 18))

        self.verticalLayout_27.addWidget(self.label_56)

        self.text_52 = QLineEdit(self.layoutWidget_5)
        self.text_52.setObjectName(u"text_52")
        self.text_52.setMinimumSize(QSize(241, 19))
        self.text_52.setMaximumSize(QSize(241, 19))

        self.verticalLayout_27.addWidget(self.text_52)

        self.layoutWidget_6 = QWidget(self.row_5)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(290, 10, 261, 321))
        self.verticalLayout_28 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QCheckBox(self.layoutWidget_6)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(241, 18))
        self.label_57.setMaximumSize(QSize(241, 18))

        self.verticalLayout_28.addWidget(self.label_57)

        self.text_53 = QLineEdit(self.layoutWidget_6)
        self.text_53.setObjectName(u"text_53")
        self.text_53.setMinimumSize(QSize(241, 19))
        self.text_53.setMaximumSize(QSize(241, 19))

        self.verticalLayout_28.addWidget(self.text_53)

        self.label_58 = QCheckBox(self.layoutWidget_6)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(241, 18))
        self.label_58.setMaximumSize(QSize(241, 18))

        self.verticalLayout_28.addWidget(self.label_58)

        self.text_54 = QLineEdit(self.layoutWidget_6)
        self.text_54.setObjectName(u"text_54")
        self.text_54.setMinimumSize(QSize(241, 19))
        self.text_54.setMaximumSize(QSize(241, 19))

        self.verticalLayout_28.addWidget(self.text_54)

        self.label_59 = QCheckBox(self.layoutWidget_6)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(241, 18))
        self.label_59.setMaximumSize(QSize(241, 18))

        self.verticalLayout_28.addWidget(self.label_59)

        self.text_55 = QLineEdit(self.layoutWidget_6)
        self.text_55.setObjectName(u"text_55")
        self.text_55.setMinimumSize(QSize(241, 19))
        self.text_55.setMaximumSize(QSize(241, 19))

        self.verticalLayout_28.addWidget(self.text_55)

        self.label_60 = QCheckBox(self.layoutWidget_6)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(241, 22))
        self.label_60.setMaximumSize(QSize(241, 22))

        self.verticalLayout_28.addWidget(self.label_60)

        self.text_56 = QLineEdit(self.layoutWidget_6)
        self.text_56.setObjectName(u"text_56")
        self.text_56.setMinimumSize(QSize(241, 29))
        self.text_56.setMaximumSize(QSize(241, 29))

        self.verticalLayout_28.addWidget(self.text_56)

        self.label_61 = QCheckBox(self.layoutWidget_6)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(241, 22))
        self.label_61.setMaximumSize(QSize(241, 22))

        self.verticalLayout_28.addWidget(self.label_61)

        self.text_57 = QLineEdit(self.layoutWidget_6)
        self.text_57.setObjectName(u"text_57")
        self.text_57.setMinimumSize(QSize(241, 29))
        self.text_57.setMaximumSize(QSize(241, 29))

        self.verticalLayout_28.addWidget(self.text_57)

        self.layoutWidget_7 = QWidget(self.row_5)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(560, 10, 241, 321))
        self.verticalLayout_29 = QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_62 = QCheckBox(self.layoutWidget_7)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(190, 22))
        self.label_62.setMaximumSize(QSize(190, 22))

        self.verticalLayout_29.addWidget(self.label_62)

        self.text_58 = QLineEdit(self.layoutWidget_7)
        self.text_58.setObjectName(u"text_58")
        self.text_58.setMinimumSize(QSize(190, 29))
        self.text_58.setMaximumSize(QSize(190, 29))

        self.verticalLayout_29.addWidget(self.text_58)

        self.label_63 = QCheckBox(self.layoutWidget_7)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(190, 22))
        self.label_63.setMaximumSize(QSize(190, 22))

        self.verticalLayout_29.addWidget(self.label_63)

        self.text_59 = QLineEdit(self.layoutWidget_7)
        self.text_59.setObjectName(u"text_59")
        self.text_59.setMinimumSize(QSize(190, 29))
        self.text_59.setMaximumSize(QSize(190, 29))

        self.verticalLayout_29.addWidget(self.text_59)

        self.label_64 = QCheckBox(self.layoutWidget_7)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(190, 18))
        self.label_64.setMaximumSize(QSize(190, 18))

        self.verticalLayout_29.addWidget(self.label_64)

        self.text_60 = QLineEdit(self.layoutWidget_7)
        self.text_60.setObjectName(u"text_60")
        self.text_60.setMinimumSize(QSize(190, 19))
        self.text_60.setMaximumSize(QSize(190, 19))

        self.verticalLayout_29.addWidget(self.text_60)

        self.label_65 = QCheckBox(self.layoutWidget_7)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(190, 18))
        self.label_65.setMaximumSize(QSize(190, 18))

        self.verticalLayout_29.addWidget(self.label_65)

        self.text_61 = QLineEdit(self.layoutWidget_7)
        self.text_61.setObjectName(u"text_61")
        self.text_61.setMinimumSize(QSize(190, 19))
        self.text_61.setMaximumSize(QSize(190, 19))

        self.verticalLayout_29.addWidget(self.text_61)

        self.label_66 = QCheckBox(self.layoutWidget_7)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(190, 18))
        self.label_66.setMaximumSize(QSize(190, 18))

        self.verticalLayout_29.addWidget(self.label_66)

        self.text_62 = QLineEdit(self.layoutWidget_7)
        self.text_62.setObjectName(u"text_62")
        self.text_62.setMinimumSize(QSize(190, 19))
        self.text_62.setMaximumSize(QSize(190, 19))

        self.verticalLayout_29.addWidget(self.text_62)

        self.layoutWidget_8 = QWidget(self.row_5)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(820, 10, 301, 341))
        self.verticalLayout_30 = QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_67 = QCheckBox(self.layoutWidget_8)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(190, 18))
        self.label_67.setMaximumSize(QSize(190, 18))

        self.verticalLayout_30.addWidget(self.label_67)

        self.text_63 = QLineEdit(self.layoutWidget_8)
        self.text_63.setObjectName(u"text_63")
        self.text_63.setMinimumSize(QSize(190, 19))
        self.text_63.setMaximumSize(QSize(190, 19))

        self.verticalLayout_30.addWidget(self.text_63)

        self.label_68 = QCheckBox(self.layoutWidget_8)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(190, 18))
        self.label_68.setMaximumSize(QSize(190, 18))

        self.verticalLayout_30.addWidget(self.label_68)

        self.text_64 = QLineEdit(self.layoutWidget_8)
        self.text_64.setObjectName(u"text_64")
        self.text_64.setMinimumSize(QSize(190, 19))
        self.text_64.setMaximumSize(QSize(190, 19))

        self.verticalLayout_30.addWidget(self.text_64)

        self.label_69 = QCheckBox(self.layoutWidget_8)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMinimumSize(QSize(190, 18))
        self.label_69.setMaximumSize(QSize(190, 18))

        self.verticalLayout_30.addWidget(self.label_69)

        self.text_65 = QLineEdit(self.layoutWidget_8)
        self.text_65.setObjectName(u"text_65")
        self.text_65.setMinimumSize(QSize(190, 19))
        self.text_65.setMaximumSize(QSize(190, 19))

        self.verticalLayout_30.addWidget(self.text_65)

        self.label_70 = QCheckBox(self.layoutWidget_8)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMinimumSize(QSize(190, 18))
        self.label_70.setMaximumSize(QSize(190, 18))

        self.verticalLayout_30.addWidget(self.label_70)

        self.text_66 = QLineEdit(self.layoutWidget_8)
        self.text_66.setObjectName(u"text_66")
        self.text_66.setMinimumSize(QSize(190, 19))
        self.text_66.setMaximumSize(QSize(190, 19))

        self.verticalLayout_30.addWidget(self.text_66)

        self.label_71 = QCheckBox(self.layoutWidget_8)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMinimumSize(QSize(190, 18))
        self.label_71.setMaximumSize(QSize(190, 18))

        self.verticalLayout_30.addWidget(self.label_71)

        self.text_67 = QLineEdit(self.layoutWidget_8)
        self.text_67.setObjectName(u"text_67")
        self.text_67.setMinimumSize(QSize(190, 19))
        self.text_67.setMaximumSize(QSize(190, 19))

        self.verticalLayout_30.addWidget(self.text_67)

        self.label_72 = QCheckBox(self.layoutWidget_8)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMinimumSize(QSize(190, 18))
        self.label_72.setMaximumSize(QSize(190, 18))

        self.verticalLayout_30.addWidget(self.label_72)

        self.text_68 = QLineEdit(self.layoutWidget_8)
        self.text_68.setObjectName(u"text_68")
        self.text_68.setMinimumSize(QSize(190, 19))
        self.text_68.setMaximumSize(QSize(190, 19))

        self.verticalLayout_30.addWidget(self.text_68)


        self.verticalLayout_26.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label = QLabel(self.new_page)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label)

        self.stackedWidget.addWidget(self.new_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 622))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMinimumSize(QSize(0, 3))
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setMinimumSize(QSize(0, 612))
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setMinimumSize(QSize(0, 135))
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(1198, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMinimumSize(QSize(589, 16))
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setMinimumSize(QSize(589, 22))
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 22))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)
        self.keras_temizle.clicked.connect(self.keras_from.clear)
        self.keras_temizle.clicked.connect(self.keras_cikan_isim.clear)
        self.keras_temizle.clicked.connect(self.keras_final_type.clear)
        self.keras_temizle.clicked.connect(self.keras_img_type.clear)
        self.keras_temizle.clicked.connect(self.keras_iterasyon.clear)
        self.keras_temizle.clicked.connect(self.keras_to.clear)
        self.keras_temizle.clicked.connect(self.txt_17.clear)
        self.keras_temizle.clicked.connect(self.txt_18.clear)
        self.keras_temizle.clicked.connect(self.txt_19.clear)
        self.keras_temizle.clicked.connect(self.txt_20.clear)
        self.keras_temizle.clicked.connect(self.txt_21.clear)
        self.keras_temizle.clicked.connect(self.txt_22.clear)
        self.keras_temizle.clicked.connect(self.txt_12.clear)
        self.keras_temizle.clicked.connect(self.txt_13.clear)
        self.keras_temizle.clicked.connect(self.txt_14.clear)
        self.keras_temizle.clicked.connect(self.txt_15.clear)
        self.keras_temizle.clicked.connect(self.txt_16.clear)
        self.keras_temizle.clicked.connect(self.txt_7.clear)
        self.keras_temizle.clicked.connect(self.txt_8.clear)
        self.keras_temizle.clicked.connect(self.txt_9.clear)
        self.keras_temizle.clicked.connect(self.txt_10.clear)
        self.keras_temizle.clicked.connect(self.txt_11.clear)
        self.keras_temizle.clicked.connect(self.txt_1.clear)
        self.keras_temizle.clicked.connect(self.txt_2.clear)
        self.keras_temizle.clicked.connect(self.txt_3.clear)
        self.keras_temizle.clicked.connect(self.txt_4.clear)
        self.keras_temizle.clicked.connect(self.txt_5.clear)
        self.keras_temizle.clicked.connect(self.txt_6.clear)
        self.btn_exit.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"AESK", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"OTONOM", None))
        self.label_75.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Ana Sayfa", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Keras ile Augmentation", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"Etiketle Augmentation", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Cik", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Ic Kisim", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><"
                        "span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; "
                        "margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Alternatif Enerjili Sistemler Kulubu", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.keras_from.setText("")
        self.keras_from.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/home/user/", None))
        self.keras_to.setText("")
        self.keras_to.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/home/user/", None))
        self.keras_uret.setText(QCoreApplication.translate("MainWindow", u"Uret", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Sonuc", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Giren", None))
        self.label_73.setText("")
        self.keras_iterasyon.setText("")
        self.keras_iterasyon.setPlaceholderText(QCoreApplication.translate("MainWindow", u"3", None))
        self.keras_img_type.setText("")
        self.keras_img_type.setPlaceholderText(QCoreApplication.translate("MainWindow", u"jpg", None))
        self.keras_final_type.setText("")
        self.keras_final_type.setPlaceholderText(QCoreApplication.translate("MainWindow", u"jpeg", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Giren Resim", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Iterasyon", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Cikan Resim", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Ismi", None))
        self.keras_cikan_isim.setText("")
        self.keras_cikan_isim.setPlaceholderText(QCoreApplication.translate("MainWindow", u"rakunlar", None))
        self.lbl_1.setText(QCoreApplication.translate("MainWindow", u"featurewise_center", None))
        self.txt_1.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.txt_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Boolean", None))
        self.lbl_2.setText(QCoreApplication.translate("MainWindow", u"samplewise_center", None))
        self.txt_2.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.txt_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Boolean", None))
        self.lbl_3.setText(QCoreApplication.translate("MainWindow", u"featurewise_std_normalization", None))
        self.txt_3.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.txt_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Boolean", None))
        self.lbl_4.setText(QCoreApplication.translate("MainWindow", u"samplewise_std_normalization", None))
        self.txt_4.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.txt_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Boolean", None))
        self.lbl_5.setText(QCoreApplication.translate("MainWindow", u"zca_whitening", None))
        self.txt_5.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.txt_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Boollean", None))
        self.lbl_6.setText(QCoreApplication.translate("MainWindow", u"zca_epsilon", None))
        self.txt_6.setText(QCoreApplication.translate("MainWindow", u"1e-06", None))
        self.txt_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Float 1e-06", None))
        self.lbl_7.setText(QCoreApplication.translate("MainWindow", u"rotation_range", None))
        self.txt_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.txt_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0-360 range", None))
        self.lbl_8.setText(QCoreApplication.translate("MainWindow", u"width_shift_range", None))
        self.txt_8.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.txt_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0-1 float range", None))
        self.lbl_9.setText(QCoreApplication.translate("MainWindow", u"height_shift_range", None))
        self.txt_9.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.txt_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0-1 float range", None))
        self.lbl_10.setText(QCoreApplication.translate("MainWindow", u"brightness_range", None))
        self.txt_10.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.txt_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"a,b list yada tuple", None))
        self.lbl_11.setText(QCoreApplication.translate("MainWindow", u"shear_range", None))
        self.txt_11.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.txt_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0-1 float ", None))
        self.lbl_12.setText(QCoreApplication.translate("MainWindow", u"channel_shift_range", None))
        self.txt_12.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.txt_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0-1 range", None))
        self.lbl_13.setText(QCoreApplication.translate("MainWindow", u"zoom_range", None))
        self.txt_13.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.txt_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0-1 range", None))
        self.lbl_14.setText(QCoreApplication.translate("MainWindow", u"fill_mode", None))
        self.txt_14.setText(QCoreApplication.translate("MainWindow", u"\"nearest\"", None))
        self.txt_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"'constant' -cval degeri 'nearest' 'wrap' 'reflect'", None))
        self.lbl_15.setText(QCoreApplication.translate("MainWindow", u"cval", None))
        self.txt_15.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.txt_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"float yalnizca 'constant' icin", None))
        self.lbl_16.setText(QCoreApplication.translate("MainWindow", u"horizontal_flip", None))
        self.txt_16.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.txt_16.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Boolean", None))
        self.lbl_17.setText(QCoreApplication.translate("MainWindow", u"vertical_flip", None))
        self.txt_17.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.txt_17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Boolean", None))
        self.lbl_18.setText(QCoreApplication.translate("MainWindow", u"rescale", None))
        self.txt_18.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.txt_18.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0-1 float", None))
        self.lbl_19.setText(QCoreApplication.translate("MainWindow", u"preprocessing_function", None))
        self.txt_19.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.txt_19.setPlaceholderText(QCoreApplication.translate("MainWindow", u"gerek yok", None))
        self.lbl_20.setText(QCoreApplication.translate("MainWindow", u"data_format", None))
        self.txt_20.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.txt_20.setPlaceholderText(QCoreApplication.translate("MainWindow", u"gerek yok", None))
        self.lbl_21.setText(QCoreApplication.translate("MainWindow", u"validation_split", None))
        self.txt_21.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.txt_21.setPlaceholderText(QCoreApplication.translate("MainWindow", u"gerek yok", None))
        self.lbl_22.setText(QCoreApplication.translate("MainWindow", u"dtype", None))
        self.txt_22.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.txt_22.setPlaceholderText(QCoreApplication.translate("MainWindow", u"gerek yok", None))
        self.keras_temizle.setText(QCoreApplication.translate("MainWindow", u"Temizle", None))
        self.augment_from.setText("")
        self.augment_from.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/home/user/", None))
        self.augment_to.setText("")
        self.augment_to.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/home/user/", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Uret", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Sonuc", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Giren", None))
        self.augment_label.setText("")
        self.augment_label.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/home/user/", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Etiketler", None))
        self.label_ayni_dosya.setText(QCoreApplication.translate("MainWindow", u"Etiketler ayni dosyada mi?", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"featurewise_center", None))
        self.text_47.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"samplewise_center", None))
        self.text_48.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"featurewise_std_normalization", None))
        self.text_49.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"samplewise_std_normalization", None))
        self.text_50.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"zca_whitening", None))
        self.text_51.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"zca_epsilon", None))
        self.text_52.setText(QCoreApplication.translate("MainWindow", u"1e-06", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"rotation_range", None))
        self.text_53.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"width_shift_range", None))
        self.text_54.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"height_shift_range", None))
        self.text_55.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"brightness_range", None))
        self.text_56.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"shear_range", None))
        self.text_57.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"channel_shift_range", None))
        self.text_58.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"zoom_range", None))
        self.text_59.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"fill_mode", None))
        self.text_60.setText(QCoreApplication.translate("MainWindow", u"\"nearest\"", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"cval", None))
        self.text_61.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"horizontal_flip", None))
        self.text_62.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"vertical_flip", None))
        self.text_63.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"rescale", None))
        self.text_64.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"preprocessing_function", None))
        self.text_65.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"data_format", None))
        self.text_66.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"validation_split", None))
        self.text_67.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"dtype", None))
        self.text_68.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Yeni Sayfa Deneme", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Bos", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Bos", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Bos", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Yildiz Teknik AESK", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

# Error: main.ui: Warning: The name 'layoutWidget' (QWidget) is already in use, defaulting to 'layoutWidget1'.
# main.ui: Warning: The name 'layoutWidget' (QWidget) is already in use, defaulting to 'layoutWidget2'.
# main.ui: Warning: The name 'layoutWidget' (QWidget) is already in use, defaulting to 'layoutWidget3'.

# while executing '/home/semih/QT/lib/python3.8/site-packages/PySide6/uic -g python main.ui'
