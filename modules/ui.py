# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main2spAxlO.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QScrollArea, QScrollBar, QSizePolicy, QSlider,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 900)
        MainWindow.setMinimumSize(QSize(1600, 900))
        MainWindow.setMaximumSize(QSize(1600, 900))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
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
"color: rgb(221, 221, 221);\n"
"font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"color: #ffffff;\n"
"background-color: rgba(33, 37, 43, 180);\n"
"border: 1px solid rgb(44, 49, 58);\n"
"background-image: none;\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 2px solid rgb(0, 204, 255);\n"
"text-align: left;\n"
"padding-left: 8px;\n"
"margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp { \n"
"background-color: rgb(37, 39,"
                        " 43);\n"
"border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg { \n"
"background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"background-color: rgb(33, 37, 43);\n"
"background-image: url(:/images/images/images/mess2_beta.png);\n"
"background-position: centered;\n"
"background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(0, 204, 255 ); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton { \n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 22px solid transparent;\n"
"background-color: transparent;\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"background-color: rgb(37, 39, 43);\n"
"}\n"
"#topMenu .QPushButton:pressed { \n"
"background-color: rgb(98, 114, 164 );\n"
"color: rgb(255, 255"
                        ", 255);\n"
"}\n"
"#bottomMenu .QPushButton { \n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"background-color:transparent;\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"background-color: rgb(37, 39, 43);\n"
"}\n"
"#bottomMenu .QPushButton:pressed { \n"
"background-color: rgb(98, 114, 164 );\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"background-color: rgb(37, 41, 48);\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"color: rgb(138, 139, 141);\n"
"}\n"
"#toggleButton:hover {\n"
"background-color: rgb(37, 39, 43);\n"
"}\n"
"#toggleButton:pressed {\n"
"background-color: rgb(98, 114, 164 );\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* ////////////////////"
                        "/////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox { \n"
"background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{ \n"
"background-color: rgb(98, 114, 164 )\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none; border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(98, 114, 164 ); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(98, 114, 164 ); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"border-top: 3px solid rgb(37, 39, 43);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left cen"
                        "ter;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 22px solid transparent;\n"
"background-color:transparent;\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"background-color: rgb(37, 39, 43);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed { \n"
"background-color: rgb(98, 114, 164 );\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{ \n"
"background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"border-top: 3px solid rgb(0, 204, 255);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none; border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; "
                        "}\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(0, 204, 255 ); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(255, 0, 0); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton { \n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 22px solid transparent;\n"
"background-color:transparent;\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"background-color: rgb(37, 39, 43);\n"
"}\n"
"#contentSettings .QPushButton:pressed { \n"
"background-color: rgb(98, 114, 164 );\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidge"
                        "t { \n"
"background-color: transparent;\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"gridline-color: rgb(44, 49, 58);\n"
"border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"border-color: rgb(44, 49, 60);\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"background-color: rgb(98, 114, 164 );\n"
"}\n"
"QHeaderView::section{\n"
"background-color: rgb(33, 37, 43);\n"
"max-width: 30px;\n"
"border: 1px solid rgb(44, 49, 58);\n"
"border-style: none;\n"
"border-bottom: 1px solid rgb(44, 49, 60);\n"
"border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader { \n"
"background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"border: 1px solid rgb(33, 37, 43);\n"
"background-color: rgb(33, 37, 43);\n"
"padding: 3px;\n"
"border-top-left-radius: 7px;\n"
"border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"border: 1px solid rgb(44, 49, 60);\n"
""
                        "}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(33, 37, 43);\n"
"padding-left: 10px;\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(0, 204, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"background-color: rgb(27, 29, 35);\n"
"border-radius: 0px;\n"
"padding: 6px;\n"
"selection-color: rgb(231, 231, 231);\n"
"selection-background-color: rgb(0, 114, 143);\n"
"}\n"
"QPlainTextEdit QScrollBar:vertical {\n"
"width: 8px;\n"
"}\n"
"QPlainTextEdit QScrollBar:horizontal {\n"
"height: 8px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"border: 2px solid rgb(64, 71, 88"
                        ");\n"
"}\n"
"QPlainTextEdit:focus {\n"
"border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"border: none;\n"
"background: rgb(52, 59, 72);\n"
"height: 8px;\n"
"margin: 0px 21px 0 21px;\n"
"border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"background: rgb(98, 114, 164 );\n"
"min-width: 25px;\n"
"border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"border: none;\n"
"background: rgb(55, 63, 77);\n"
"width: 20px;\n"
"border-top-right-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"subcontrol-position: right;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"border: none;\n"
"background: rgb(55, 63, 77);\n"
"width: 20px;\n"
"border-top-left-radius: 4px;\n"
"border-bottom-left-radius: 4px;\n"
"subcontrol-position: left;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar:"
                        ":down-arrow:horizontal\n"
"{\n"
"background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"background: none;\n"
"}\n"
"QScrollBar:vertical {\n"
"border: none;\n"
"background: rgb(52, 59, 72);\n"
"width: 8px;\n"
"margin: 0 0 0 0;\n"
"border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical { \n"
"background: rgb(40, 44, 52);\n"
"min-height: 25px;\n"
"border-radius: 4px\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"background: rgb(60, 64, 72);\n"
"}\n"
"QScrollBar::handle:vertical:pressed { \n"
"background: rgb(60, 64, 72); \n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"border: none;\n"
"background: rgb(55, 63, 77);\n"
"height: 0px;\n"
"border-bottom-left-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"border: none;\n"
"background: rgb(55, 63, 77);\n"
"height: 0px;\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"subcontrol-positio"
                        "n: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"border: 3px solid rgb(52, 59, 72);\n"
"width: 15px;\n"
"height: 15px;\n"
"border-radius: 10px;\n"
"background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"background: 3px solid rgb(52, 59, 72);\n"
"border: 3px solid rgb(52, 59, 72); \n"
"background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"border: 3px solid rgb(52, 59, 72);\n"
"width: 15px;\n"
"heig"
                        "ht: 15px;\n"
"border-radius: 10px;\n"
"background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"background: 3px solid rgb(94, 106, 130);\n"
"border: 3px solid rgb(52, 59, 72); \n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"background-color: rgb(27, 29, 35);\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(33, 37, 43);\n"
"padding: 5px;\n"
"padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"width: 25px; \n"
"border-left-width: 3px;\n"
"border-left-color: rgba(39, 44, 54, 150);\n"
"border-left-style: solid;\n"
"border-top-right-radius: 3px;\n"
"border-bottom-right-radius: 3px; \n"
"background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"background-position: "
                        "center;\n"
"background-repeat: no-reperat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"color: rgb(0, 204, 255); \n"
"background-color: rgb(33, 37, 43);\n"
"padding: 10px;\n"
"selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"border-radius: 5px;\n"
"height: 10px;\n"
"margin: 0px;\n"
"background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"background-color: rgb(98, 114, 164 );\n"
"border: none;\n"
"height: 10px;\n"
"width: 10px;\n"
"margin: 0px;\n"
"border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"background-color: rgb(0, 204, 255);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"border-radius: 5px;\n"
"width: 10px;\n"
"margin: 0px;\n"
"backgr"
                        "ound-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"background-color: rgb(98, 114, 164 );\n"
"border: none;\n"
"height: 10px;\n"
"width: 10px;\n"
"margin: 0px;\n"
"border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"background-color: rgb(0, 204, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton { \n"
"color: rgb(0, 204, 255);\n"
"border-radius: 5px;\n"
"padding: 5px;\n"
"color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover { \n"
"color: rgb(255, 170, 255);\n"
"background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed { \n"
"color: rgb(98, 114, 164 );\n"
"background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* //////////////////////////////////////////////////////////////////"
                        "///////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"border: 2px solid rgb(52, 59, 72);\n"
"border-radius: 5px; \n"
"background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"background-color: rgb(57, 65, 80);\n"
"border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed { \n"
"background-color: rgb(35, 40, 49);\n"
"border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"#diagnosticsRow11 QPushButton {\n"
"background-color: rbg(255, 0, 0);\n"
"}\n"
"#diagnosticsRow11 QPushButton:pressed {\n"
"background-color: rbg(0, 204, 255);\n"
"}\n"
"#toggleBox{\n"
"border-top: 3px solid rgb(0, 204, 255);\n"
"}\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setStyleSheet(u"background-color: rgb(13, 16, 21);")
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setStyleSheet(u"background-color: rgb(13, 16, 21);")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
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
        self.toggleButton.setMinimumSize(QSize(0, 45))
        palette = QPalette()
        brush = QBrush(QColor(138, 139, 141, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(21, 23, 27, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(138, 139, 141, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.toggleButton.setPalette(palette)
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);\n"
"background-color: rgb(21, 23, 27);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
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
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_diagnostics = QPushButton(self.topMenu)
        self.btn_diagnostics.setObjectName(u"btn_diagnostics")
        sizePolicy.setHeightForWidth(self.btn_diagnostics.sizePolicy().hasHeightForWidth())
        self.btn_diagnostics.setSizePolicy(sizePolicy)
        self.btn_diagnostics.setMinimumSize(QSize(0, 45))
        self.btn_diagnostics.setFont(font)
        self.btn_diagnostics.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_diagnostics.setLayoutDirection(Qt.LeftToRight)
        self.btn_diagnostics.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-rss.png);")

        self.verticalLayout_8.addWidget(self.btn_diagnostics)

        self.btn_planner = QPushButton(self.topMenu)
        self.btn_planner.setObjectName(u"btn_planner")
        self.btn_planner.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_planner.sizePolicy().hasHeightForWidth())
        self.btn_planner.setSizePolicy(sizePolicy)
        self.btn_planner.setMinimumSize(QSize(0, 45))
        self.btn_planner.setFont(font)
        self.btn_planner.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.btn_planner)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_settings = QPushButton(self.bottomMenu)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        self.btn_settings.setMinimumSize(QSize(0, 45))
        self.btn_settings.setFont(font)
        self.btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings.setLayoutDirection(Qt.LeftToRight)
        self.btn_settings.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.btn_settings)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
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
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

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
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
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
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setStyleSheet(u"background-color: rgb(13, 16, 21);")
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
        self.leftBox.setStyleSheet(u"background-color: rgb(13, 16, 21);")
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
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setStyleSheet(u"background-color: rgb(13, 16, 21);")
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
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
        self.contentBottom.setAutoFillBackground(False)
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        palette1 = QPalette()
        brush3 = QBrush(QColor(221, 221, 221, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        brush4 = QBrush(QColor(30, 33, 39, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush4)
        brush5 = QBrush(QColor(66, 74, 87, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush5)
        brush6 = QBrush(QColor(55, 61, 72, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        brush7 = QBrush(QColor(22, 25, 29, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush7)
        brush8 = QBrush(QColor(29, 33, 39, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush8)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush3)
        brush9 = QBrush(QColor(255, 255, 255, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush9)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush4)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        brush11 = QBrush(QColor(22, 24, 29, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush11)
        brush12 = QBrush(QColor(255, 255, 220, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush12)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
        brush13 = QBrush(QColor(221, 221, 221, 128))
        brush13.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush13)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        brush14 = QBrush(QColor(75, 75, 75, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush14)
        brush15 = QBrush(QColor(42, 42, 42, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush15)
        brush16 = QBrush(QColor(33, 33, 33, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush16)
        brush17 = QBrush(QColor(38, 38, 38, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush17)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush14)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        brush18 = QBrush(QColor(25, 25, 25, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush18)
        brush19 = QBrush(QColor(43, 43, 43, 255))
        brush19.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush19)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush13)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        brush20 = QBrush(QColor(37, 37, 37, 255))
        brush20.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush20)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush19)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.stackedWidget.setPalette(palette1)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(30, 33, 39);")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"/*\n"
"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"*/")
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 520, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon4)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush13)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush13)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.tableWidget.setPalette(palette2)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.diagnostics = QWidget()
        self.diagnostics.setObjectName(u"diagnostics")
        sizePolicy2.setHeightForWidth(self.diagnostics.sizePolicy().hasHeightForWidth())
        self.diagnostics.setSizePolicy(sizePolicy2)
        self.horizontalLayout_7 = QHBoxLayout(self.diagnostics)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.diagnosticsMenu = QFrame(self.diagnostics)
        self.diagnosticsMenu.setObjectName(u"diagnosticsMenu")
        self.diagnosticsMenu.setMinimumSize(QSize(250, 60))
        self.diagnosticsMenu.setMaximumSize(QSize(250, 16777215))
        self.diagnosticsMenu.setStyleSheet(u"#diagnosticsMenu {\n"
"background-color: rgb(21, 23, 27);\n"
"}\n"
"#diagnosticsMenu QFrame {\n"
"background: transparent;\n"
"border: None;\n"
"}\n"
"")
        self.diagnosticsMenu.setFrameShape(QFrame.NoFrame)
        self.diagnosticsMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.diagnosticsMenu)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.diagnosticsMenuLayout = QFrame(self.diagnosticsMenu)
        self.diagnosticsMenuLayout.setObjectName(u"diagnosticsMenuLayout")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.diagnosticsMenuLayout.sizePolicy().hasHeightForWidth())
        self.diagnosticsMenuLayout.setSizePolicy(sizePolicy4)
        self.diagnosticsMenuLayout.setStyleSheet(u"")
        self.diagnosticsMenuLayout.setFrameShape(QFrame.NoFrame)
        self.diagnosticsMenuLayout.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.diagnosticsMenuLayout)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(-1, 6, -1, 27)
        self.diagnosticsMenu1 = QFrame(self.diagnosticsMenuLayout)
        self.diagnosticsMenu1.setObjectName(u"diagnosticsMenu1")
        sizePolicy2.setHeightForWidth(self.diagnosticsMenu1.sizePolicy().hasHeightForWidth())
        self.diagnosticsMenu1.setSizePolicy(sizePolicy2)
        self.diagnosticsMenu1.setStyleSheet(u"QFrame QPushButton {\n"
"border: 2px solid rgb(0, 204, 255);\n"
"border-radius: 20px;\n"
"background-color: transparent;\n"
"min-height: 40px;\n"
"}\n"
"QFrame QPushButton:hover {\n"
"	background-color: rgb(25, 40, 50);\n"
"}\n"
"QFrame QPushButton:pressed {\n"
"	background-color: rgb(25, 40, 50);\n"
"}\n"
"QFrame QLabel {\n"
"color: rgb(201, 201, 201);\n"
"font-weight: 600;\n"
"border-bottom: 1px solid rgb(0, 204, 255);\n"
"}\n"
"")
        self.diagnosticsMenu1.setFrameShape(QFrame.StyledPanel)
        self.diagnosticsMenu1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.diagnosticsMenu1)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.diagnosticsMenu1Layout = QVBoxLayout()
        self.diagnosticsMenu1Layout.setSpacing(27)
        self.diagnosticsMenu1Layout.setObjectName(u"diagnosticsMenu1Layout")
        self.diagnosticsMenu1Layout.setContentsMargins(1, 8, 1, 54)
        self.diagnosticsMenu1ExperimentSelection = QFrame(self.diagnosticsMenu1)
        self.diagnosticsMenu1ExperimentSelection.setObjectName(u"diagnosticsMenu1ExperimentSelection")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.diagnosticsMenu1ExperimentSelection.sizePolicy().hasHeightForWidth())
        self.diagnosticsMenu1ExperimentSelection.setSizePolicy(sizePolicy5)
        self.diagnosticsMenu1ExperimentSelection.setFrameShape(QFrame.StyledPanel)
        self.diagnosticsMenu1ExperimentSelection.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.diagnosticsMenu1ExperimentSelection)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.diagnosticsMenu1ExperimentSelectionLabel = QLabel(self.diagnosticsMenu1ExperimentSelection)
        self.diagnosticsMenu1ExperimentSelectionLabel.setObjectName(u"diagnosticsMenu1ExperimentSelectionLabel")
        self.diagnosticsMenu1ExperimentSelectionLabel.setMaximumSize(QSize(16777215, 24))

        self.verticalLayout_33.addWidget(self.diagnosticsMenu1ExperimentSelectionLabel)

        self.diagnosticsMenu1ExperimentFile = QFrame(self.diagnosticsMenu1ExperimentSelection)
        self.diagnosticsMenu1ExperimentFile.setObjectName(u"diagnosticsMenu1ExperimentFile")
        self.diagnosticsMenu1ExperimentFile.setMaximumSize(QSize(16777215, 16777215))
        self.diagnosticsMenu1ExperimentFile.setStyleSheet(u"QFrame QLabel {\n"
"color: rgb(201, 201, 201);\n"
"font-weight: 400;\n"
"font-size: 11px;\n"
"border-bottom: 0px solid rgb(0, 204, 255);\n"
"}\n"
"QPushButton {\n"
"background-color: rgb(30, 33, 39);\n"
"border: none;\n"
"color: rgb(201, 201, 201);\n"
"font-size: 11px;\n"
"selection-color: rgb(221, 221, 231);\n"
"selection-background-color: rgb(0, 114, 143);\n"
"border-radius: 5px;\n"
"min-height: 17px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(40, 44, 52);\n"
"}\n"
"QLineEdit {\n"
"background-color: rgb(30, 33, 39);\n"
"border: none;\n"
"color: rgb(201, 201, 201);\n"
"font-size: 9px;\n"
"selection-color: rgb(221, 221, 231);\n"
"selection-background-color: rgb(0, 114, 143);\n"
"padding: 0 6px 0 6px;\n"
"}\n"
"QLineEdit:hover {\n"
"background-color: rgb(40, 44, 52);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(40, 44, 52);\n"
"}")
        self.diagnosticsMenu1ExperimentFile.setFrameShape(QFrame.StyledPanel)
        self.diagnosticsMenu1ExperimentFile.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.diagnosticsMenu1ExperimentFile)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 15, 0, 9)
        self.diagnosticsMenu1ExperimentFileLabel = QLabel(self.diagnosticsMenu1ExperimentFile)
        self.diagnosticsMenu1ExperimentFileLabel.setObjectName(u"diagnosticsMenu1ExperimentFileLabel")
        self.diagnosticsMenu1ExperimentFileLabel.setMinimumSize(QSize(0, 17))
        self.diagnosticsMenu1ExperimentFileLabel.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_10.addWidget(self.diagnosticsMenu1ExperimentFileLabel)

        self.diagnosticsMenu1ExperimentFileText = QLineEdit(self.diagnosticsMenu1ExperimentFile)
        self.diagnosticsMenu1ExperimentFileText.setObjectName(u"diagnosticsMenu1ExperimentFileText")
        self.diagnosticsMenu1ExperimentFileText.setMinimumSize(QSize(0, 17))
        self.diagnosticsMenu1ExperimentFileText.setMaximumSize(QSize(16777215, 24))
        self.diagnosticsMenu1ExperimentFileText.setFrame(True)
        self.diagnosticsMenu1ExperimentFileText.setDragEnabled(False)
        self.diagnosticsMenu1ExperimentFileText.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.diagnosticsMenu1ExperimentFileText)

        self.buttonExperimentSelect = QPushButton(self.diagnosticsMenu1ExperimentFile)
        self.buttonExperimentSelect.setObjectName(u"buttonExperimentSelect")
        sizePolicy.setHeightForWidth(self.buttonExperimentSelect.sizePolicy().hasHeightForWidth())
        self.buttonExperimentSelect.setSizePolicy(sizePolicy)
        self.buttonExperimentSelect.setMinimumSize(QSize(0, 17))
        self.buttonExperimentSelect.setMaximumSize(QSize(16777215, 16777215))
        self.buttonExperimentSelect.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonExperimentSelect.setStyleSheet(u"background-image: url(:/icons/images/icons2/browse_files.png);\n"
"background-repeat: no-repeat;\n"
"background-position: bottom;")

        self.horizontalLayout_10.addWidget(self.buttonExperimentSelect)


        self.verticalLayout_33.addWidget(self.diagnosticsMenu1ExperimentFile)

        self.diagnosticsMenu1ExperimentSelectionButtons = QFrame(self.diagnosticsMenu1ExperimentSelection)
        self.diagnosticsMenu1ExperimentSelectionButtons.setObjectName(u"diagnosticsMenu1ExperimentSelectionButtons")
        sizePolicy4.setHeightForWidth(self.diagnosticsMenu1ExperimentSelectionButtons.sizePolicy().hasHeightForWidth())
        self.diagnosticsMenu1ExperimentSelectionButtons.setSizePolicy(sizePolicy4)
        self.diagnosticsMenu1ExperimentSelectionButtons.setStyleSheet(u"#diagnosticsMenu1ExperimentSelectionButtons QPushButton {\n"
"background-color: rgb(30, 33, 39);\n"
"border-radius: 6px;\n"
"padding: 0 9px 0 9px;\n"
"min-height: 24px;\n"
"max-height: 24px;\n"
"border: none;\n"
"color: rgb(201, 201, 201);\n"
"font-size: 11px;\n"
"}\n"
"#diagnosticsMenu1ExperimentSelectionButtons QPushButton:hover {\n"
"background-color: rgb(40, 44, 52);\n"
"}\n"
"#diagnosticsMenu1ExperimentSelectionButtons QPushButton:pressed {\n"
"background-color: rgb(40, 44, 52);\n"
"}\n"
"")
        self.diagnosticsMenu1ExperimentSelectionButtons.setFrameShape(QFrame.StyledPanel)
        self.diagnosticsMenu1ExperimentSelectionButtons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.diagnosticsMenu1ExperimentSelectionButtons)
        self.verticalLayout_36.setSpacing(9)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.buttonExperimentLoad = QPushButton(self.diagnosticsMenu1ExperimentSelectionButtons)
        self.buttonExperimentLoad.setObjectName(u"buttonExperimentLoad")
        self.buttonExperimentLoad.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_36.addWidget(self.buttonExperimentLoad)


        self.verticalLayout_33.addWidget(self.diagnosticsMenu1ExperimentSelectionButtons)


        self.diagnosticsMenu1Layout.addWidget(self.diagnosticsMenu1ExperimentSelection)

        self.diagnosticsMenu1Settings = QFrame(self.diagnosticsMenu1)
        self.diagnosticsMenu1Settings.setObjectName(u"diagnosticsMenu1Settings")
        sizePolicy4.setHeightForWidth(self.diagnosticsMenu1Settings.sizePolicy().hasHeightForWidth())
        self.diagnosticsMenu1Settings.setSizePolicy(sizePolicy4)
        self.diagnosticsMenu1Settings.setMinimumSize(QSize(0, 0))
        self.diagnosticsMenu1Settings.setFrameShape(QFrame.StyledPanel)
        self.diagnosticsMenu1Settings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.diagnosticsMenu1Settings)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.dataCollectionLabel = QLabel(self.diagnosticsMenu1Settings)
        self.dataCollectionLabel.setObjectName(u"dataCollectionLabel")
        self.dataCollectionLabel.setMaximumSize(QSize(16777215, 24))

        self.verticalLayout_39.addWidget(self.dataCollectionLabel)

        self.dataCollectionSettings = QFrame(self.diagnosticsMenu1Settings)
        self.dataCollectionSettings.setObjectName(u"dataCollectionSettings")
        sizePolicy5.setHeightForWidth(self.dataCollectionSettings.sizePolicy().hasHeightForWidth())
        self.dataCollectionSettings.setSizePolicy(sizePolicy5)
        self.dataCollectionSettings.setMinimumSize(QSize(0, 0))
        self.dataCollectionSettings.setMaximumSize(QSize(16777215, 36))
        self.dataCollectionSettings.setStyleSheet(u"QFrame QLabel {\n"
"color: rgb(201, 201, 201);\n"
"font-weight: 400;\n"
"font-size: 11px;\n"
"border-bottom: 0px solid rgb(0, 204, 255);\n"
"}\n"
"QPushButton {\n"
"background-color: rgb(30, 33, 39);\n"
"border: none;\n"
"color: rgb(201, 201, 201);\n"
"font-size: 11px;\n"
"selection-background-color: rgb(0, 153, 191);\n"
"border-radius: 5px;\n"
"min-height: 17px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(40, 44, 52);\n"
"}\n"
"QLineEdit {\n"
"background-color: rgb(30, 33, 39);\n"
"border: none;\n"
"color: rgb(201, 201, 201);\n"
"font-size: 9px;\n"
"selection-color: rgb(221, 221, 231);\n"
"selection-background-color: rgb(0, 114, 143);\n"
"padding: 0 6px 0 6px;\n"
"}\n"
"QLineEdit:hover {\n"
"background-color: rgb(40, 44, 52);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(40, 44, 52);\n"
"}")
        self.dataCollectionSettings.setFrameShape(QFrame.StyledPanel)
        self.dataCollectionSettings.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.dataCollectionSettings)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 15, 0, 0)
        self.dataCollectionPathLabel = QLabel(self.dataCollectionSettings)
        self.dataCollectionPathLabel.setObjectName(u"dataCollectionPathLabel")
        self.dataCollectionPathLabel.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_13.addWidget(self.dataCollectionPathLabel)

        self.logSavePathText = QLineEdit(self.dataCollectionSettings)
        self.logSavePathText.setObjectName(u"logSavePathText")
        self.logSavePathText.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.logSavePathText)

        self.btn_log_save_path_select = QPushButton(self.dataCollectionSettings)
        self.btn_log_save_path_select.setObjectName(u"btn_log_save_path_select")
        self.btn_log_save_path_select.setMaximumSize(QSize(16777215, 16))
        self.btn_log_save_path_select.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_log_save_path_select.setStyleSheet(u"background-image: url(:/icons/images/icons2/browse_files.png);\n"
"background-repeat: no-repeat;\n"
"background-position: bottom;")

        self.horizontalLayout_13.addWidget(self.btn_log_save_path_select)


        self.verticalLayout_39.addWidget(self.dataCollectionSettings)

        self.frame_3 = QFrame(self.diagnosticsMenu1Settings)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame QLabel {\n"
"color: rgb(92, 95, 102);\n"
"font-weight: 400;\n"
"font-size: 10px;\n"
"font-style: italic;\n"
"border-bottom: 0px solid rgb(0, 204, 255);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_3)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 6, 0, 0)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_30.addWidget(self.label_2)


        self.verticalLayout_39.addWidget(self.frame_3)

        self.dataCollectionButtons = QFrame(self.diagnosticsMenu1Settings)
        self.dataCollectionButtons.setObjectName(u"dataCollectionButtons")
        sizePolicy5.setHeightForWidth(self.dataCollectionButtons.sizePolicy().hasHeightForWidth())
        self.dataCollectionButtons.setSizePolicy(sizePolicy5)
        self.dataCollectionButtons.setStyleSheet(u"#dataCollectionButtons QPushButton {\n"
"background-color: rgb(30, 33, 39);\n"
"border-radius: 6px;\n"
"padding: 0 9px 0 9px;\n"
"min-height: 24px;\n"
"max-height: 24px;\n"
"border: none;\n"
"color: rgb(201, 201, 201);\n"
"font-size: 11px;\n"
"}\n"
"#dataCollectionButtons QPushButton:hover {\n"
"background-color: rgb(40, 44, 52);\n"
"}\n"
"#dataCollectionButtons QPushButton:pressed {\n"
"background-color: rgb(40, 44, 52);\n"
"}\n"
"")
        self.dataCollectionButtons.setFrameShape(QFrame.StyledPanel)
        self.dataCollectionButtons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.dataCollectionButtons)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 9, 0, 0)
        self.btn_logs_download = QPushButton(self.dataCollectionButtons)
        self.btn_logs_download.setObjectName(u"btn_logs_download")
        self.btn_logs_download.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_40.addWidget(self.btn_logs_download)


        self.verticalLayout_39.addWidget(self.dataCollectionButtons)


        self.diagnosticsMenu1Layout.addWidget(self.diagnosticsMenu1Settings)

        self.diagnosticsMenu1ExperimentLocalOps = QFrame(self.diagnosticsMenu1)
        self.diagnosticsMenu1ExperimentLocalOps.setObjectName(u"diagnosticsMenu1ExperimentLocalOps")
        self.diagnosticsMenu1ExperimentLocalOps.setFrameShape(QFrame.NoFrame)
        self.diagnosticsMenu1ExperimentLocalOps.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.diagnosticsMenu1ExperimentLocalOps)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.diagnosticsMenu1ExperimentLocalOpsLabel = QLabel(self.diagnosticsMenu1ExperimentLocalOps)
        self.diagnosticsMenu1ExperimentLocalOpsLabel.setObjectName(u"diagnosticsMenu1ExperimentLocalOpsLabel")

        self.verticalLayout_37.addWidget(self.diagnosticsMenu1ExperimentLocalOpsLabel)

        self.diagnosticsMenu1ExperimentLocalOpsButtons = QFrame(self.diagnosticsMenu1ExperimentLocalOps)
        self.diagnosticsMenu1ExperimentLocalOpsButtons.setObjectName(u"diagnosticsMenu1ExperimentLocalOpsButtons")
        self.diagnosticsMenu1ExperimentLocalOpsButtons.setStyleSheet(u"#diagnosticsMenu1ExperimentLocalOpsButtons QPushButton {\n"
"background-color: rgb(30, 33, 39);\n"
"border-radius: 6px;\n"
"padding: 0 9px 0 9px;\n"
"min-height: 24px;\n"
"max-height: 24px;\n"
"border: none;\n"
"color: rgb(201, 201, 201);\n"
"font-size: 11px;\n"
"}\n"
"#diagnosticsMenu1ExperimentLocalOpsButtons QPushButton:hover {\n"
"background-color: rgb(40, 44, 52);\n"
"}\n"
"#diagnosticsMenu1ExperimentLocalOpsButtons QPushButton:pressed {\n"
"background-color: rgb(40, 44, 52);\n"
"}\n"
"")
        self.diagnosticsMenu1ExperimentLocalOpsButtons.setFrameShape(QFrame.NoFrame)
        self.diagnosticsMenu1ExperimentLocalOpsButtons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.diagnosticsMenu1ExperimentLocalOpsButtons)
        self.verticalLayout_38.setSpacing(9)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 15, 0, 0)
        self.buttonROS2LocalLaunchShutdown = QPushButton(self.diagnosticsMenu1ExperimentLocalOpsButtons)
        self.buttonROS2LocalLaunchShutdown.setObjectName(u"buttonROS2LocalLaunchShutdown")
        self.buttonROS2LocalLaunchShutdown.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_38.addWidget(self.buttonROS2LocalLaunchShutdown)


        self.verticalLayout_37.addWidget(self.diagnosticsMenu1ExperimentLocalOpsButtons)


        self.diagnosticsMenu1Layout.addWidget(self.diagnosticsMenu1ExperimentLocalOps)

        self.diagnosticsMenu1ExperimentRemoteOps = QFrame(self.diagnosticsMenu1)
        self.diagnosticsMenu1ExperimentRemoteOps.setObjectName(u"diagnosticsMenu1ExperimentRemoteOps")
        self.diagnosticsMenu1ExperimentRemoteOps.setMinimumSize(QSize(0, 0))
        self.diagnosticsMenu1ExperimentRemoteOps.setFrameShape(QFrame.NoFrame)
        self.diagnosticsMenu1ExperimentRemoteOps.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.diagnosticsMenu1ExperimentRemoteOps)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.diagnosticsMenu1ExperimentRemoteOpsLabel = QLabel(self.diagnosticsMenu1ExperimentRemoteOps)
        self.diagnosticsMenu1ExperimentRemoteOpsLabel.setObjectName(u"diagnosticsMenu1ExperimentRemoteOpsLabel")

        self.verticalLayout_21.addWidget(self.diagnosticsMenu1ExperimentRemoteOpsLabel)

        self.diagnosticsMenu1ExperimentRemoteOpsButtons = QFrame(self.diagnosticsMenu1ExperimentRemoteOps)
        self.diagnosticsMenu1ExperimentRemoteOpsButtons.setObjectName(u"diagnosticsMenu1ExperimentRemoteOpsButtons")
        self.diagnosticsMenu1ExperimentRemoteOpsButtons.setMinimumSize(QSize(0, 60))
        self.diagnosticsMenu1ExperimentRemoteOpsButtons.setStyleSheet(u"#diagnosticsMenu1ExperimentRemoteOpsButtons QPushButton {\n"
"background-color: rgb(30, 33, 39);\n"
"border-radius: 6px;\n"
"padding: 0 9px 0 9px;\n"
"min-height: 24px;\n"
"max-height: 24px;\n"
"border: none;\n"
"color: rgb(201, 201, 201);\n"
"font-size: 11px;\n"
"}\n"
"#diagnosticsMenu1ExperimentRemoteOpsButtons QPushButton:hover {\n"
"background-color: rgb(40, 44, 52);\n"
"}\n"
"#diagnosticsMenu1ExperimentRemoteOpsButtons QPushButton:pressed {\n"
"background-color: rgb(40, 44, 52);\n"
"}\n"
"")
        self.diagnosticsMenu1ExperimentRemoteOpsButtons.setFrameShape(QFrame.NoFrame)
        self.diagnosticsMenu1ExperimentRemoteOpsButtons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.diagnosticsMenu1ExperimentRemoteOpsButtons)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.buttonNetworkRemoteConnectDisconnect = QPushButton(self.diagnosticsMenu1ExperimentRemoteOpsButtons)
        self.buttonNetworkRemoteConnectDisconnect.setObjectName(u"buttonNetworkRemoteConnectDisconnect")
        self.buttonNetworkRemoteConnectDisconnect.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_23.addWidget(self.buttonNetworkRemoteConnectDisconnect)

        self.buttonROS2RemoteLaunchShutdown = QPushButton(self.diagnosticsMenu1ExperimentRemoteOpsButtons)
        self.buttonROS2RemoteLaunchShutdown.setObjectName(u"buttonROS2RemoteLaunchShutdown")
        self.buttonROS2RemoteLaunchShutdown.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_23.addWidget(self.buttonROS2RemoteLaunchShutdown)


        self.verticalLayout_21.addWidget(self.diagnosticsMenu1ExperimentRemoteOpsButtons)


        self.diagnosticsMenu1Layout.addWidget(self.diagnosticsMenu1ExperimentRemoteOps)

        self.diagnosticsMenu1Spacer = QFrame(self.diagnosticsMenu1)
        self.diagnosticsMenu1Spacer.setObjectName(u"diagnosticsMenu1Spacer")
        sizePolicy2.setHeightForWidth(self.diagnosticsMenu1Spacer.sizePolicy().hasHeightForWidth())
        self.diagnosticsMenu1Spacer.setSizePolicy(sizePolicy2)
        self.diagnosticsMenu1Spacer.setFrameShape(QFrame.NoFrame)
        self.diagnosticsMenu1Spacer.setFrameShadow(QFrame.Raised)

        self.diagnosticsMenu1Layout.addWidget(self.diagnosticsMenu1Spacer)


        self.verticalLayout_32.addLayout(self.diagnosticsMenu1Layout)


        self.verticalLayout_29.addWidget(self.diagnosticsMenu1)

        self.diagnosticsMenu2 = QFrame(self.diagnosticsMenuLayout)
        self.diagnosticsMenu2.setObjectName(u"diagnosticsMenu2")
        self.diagnosticsMenu2.setMinimumSize(QSize(0, 0))
        self.diagnosticsMenu2.setMaximumSize(QSize(16777215, 16777215))
        self.diagnosticsMenu2.setStyleSheet(u"#buttonExperimentRunAbort  {\n"
"color: rgb(201, 201, 201);\n"
"background-color: rgb(35, 28, 30);\n"
"font-size: 14px;\n"
"min-height: 36px;\n"
"max-height: 36px;\n"
"border: 2px solid rgb(217, 83, 79);\n"
"border-radius: 12px;\n"
"}")
        self.diagnosticsMenu2.setFrameShape(QFrame.NoFrame)
        self.diagnosticsMenu2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.diagnosticsMenu2)
        self.verticalLayout_35.setSpacing(9)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 9)
        self.buttonExperimentRunAbort = QPushButton(self.diagnosticsMenu2)
        self.buttonExperimentRunAbort.setObjectName(u"buttonExperimentRunAbort")
        self.buttonExperimentRunAbort.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_35.addWidget(self.buttonExperimentRunAbort)


        self.verticalLayout_29.addWidget(self.diagnosticsMenu2)


        self.verticalLayout_7.addWidget(self.diagnosticsMenuLayout)


        self.horizontalLayout_7.addWidget(self.diagnosticsMenu)

        self.diagnosticsTiles = QFrame(self.diagnostics)
        self.diagnosticsTiles.setObjectName(u"diagnosticsTiles")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.diagnosticsTiles.sizePolicy().hasHeightForWidth())
        self.diagnosticsTiles.setSizePolicy(sizePolicy6)
        self.diagnosticsTiles.setMinimumSize(QSize(400, 60))
        self.diagnosticsTiles.setStyleSheet(u"")
        self.diagnosticsTiles.setFrameShape(QFrame.NoFrame)
        self.diagnosticsTiles.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.diagnosticsTiles)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.diagnosticsTilesLayout = QVBoxLayout()
        self.diagnosticsTilesLayout.setSpacing(0)
        self.diagnosticsTilesLayout.setObjectName(u"diagnosticsTilesLayout")
        self.diagnosticsTilesMenu = QFrame(self.diagnosticsTiles)
        self.diagnosticsTilesMenu.setObjectName(u"diagnosticsTilesMenu")
        self.diagnosticsTilesMenu.setMinimumSize(QSize(0, 43))
        self.diagnosticsTilesMenu.setMaximumSize(QSize(16777215, 43))
        self.diagnosticsTilesMenu.setStyleSheet(u"#diagnosticsTilesMenu {\n"
"background-color: rgb(21, 23, 27);\n"
"}\n"
"#diagnosticsTilesMenu .QFrame {\n"
"background: transparent;\n"
"}\n"
"#diagnosticsTilesMenu .QPushButton { \n"
"background-color: transparent;\n"
"border: None;\n"
"border-radius: 0;\n"
"color: rgb(201, 201, 201);\n"
"font-size: 14px;\n"
"height: 100%;\n"
"padding: 0 18px 0 18px;\n"
"text-align: center;\n"
"}\n"
"#diagnosticsTilesMenu .QPushButton:pressed { \n"
"color: rgb(255, 255, 255);\n"
"}")
        self.diagnosticsTilesMenu.setFrameShape(QFrame.NoFrame)
        self.diagnosticsTilesMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.diagnosticsTilesMenu)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.diagnosticsTilesMenu1 = QFrame(self.diagnosticsTilesMenu)
        self.diagnosticsTilesMenu1.setObjectName(u"diagnosticsTilesMenu1")
        self.diagnosticsTilesMenu1.setFrameShape(QFrame.NoFrame)
        self.diagnosticsTilesMenu1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.diagnosticsTilesMenu1)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.diagnosticsTilesMenu1Buttons = QHBoxLayout()
        self.diagnosticsTilesMenu1Buttons.setSpacing(0)
        self.diagnosticsTilesMenu1Buttons.setObjectName(u"diagnosticsTilesMenu1Buttons")

        self.horizontalLayout_16.addLayout(self.diagnosticsTilesMenu1Buttons)


        self.horizontalLayout_14.addWidget(self.diagnosticsTilesMenu1)

        self.diagnosticsTilesMenu2 = QFrame(self.diagnosticsTilesMenu)
        self.diagnosticsTilesMenu2.setObjectName(u"diagnosticsTilesMenu2")
        sizePolicy1.setHeightForWidth(self.diagnosticsTilesMenu2.sizePolicy().hasHeightForWidth())
        self.diagnosticsTilesMenu2.setSizePolicy(sizePolicy1)
        self.diagnosticsTilesMenu2.setFrameShape(QFrame.NoFrame)
        self.diagnosticsTilesMenu2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.diagnosticsTilesMenu2)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.buttonDiagnosticsRefresh = QPushButton(self.diagnosticsTilesMenu2)
        self.buttonDiagnosticsRefresh.setObjectName(u"buttonDiagnosticsRefresh")
        self.buttonDiagnosticsRefresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonDiagnosticsRefresh.setStyleSheet(u"font-size: 11px;")

        self.horizontalLayout_17.addWidget(self.buttonDiagnosticsRefresh, 0, Qt.AlignRight)


        self.horizontalLayout_14.addWidget(self.diagnosticsTilesMenu2)


        self.diagnosticsTilesLayout.addWidget(self.diagnosticsTilesMenu)

        self.diagnosticsTilesWindow = QFrame(self.diagnosticsTiles)
        self.diagnosticsTilesWindow.setObjectName(u"diagnosticsTilesWindow")
        sizePolicy2.setHeightForWidth(self.diagnosticsTilesWindow.sizePolicy().hasHeightForWidth())
        self.diagnosticsTilesWindow.setSizePolicy(sizePolicy2)
        self.diagnosticsTilesWindow.setFrameShape(QFrame.StyledPanel)
        self.diagnosticsTilesWindow.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.diagnosticsTilesWindow)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.diagnosticsTilesDefaultPage = QStackedWidget(self.diagnosticsTilesWindow)
        self.diagnosticsTilesDefaultPage.setObjectName(u"diagnosticsTilesDefaultPage")
        self.diagnosticsTilesDefaultPage1 = QWidget()
        self.diagnosticsTilesDefaultPage1.setObjectName(u"diagnosticsTilesDefaultPage1")
        self.diagnosticsTilesDefaultPage.addWidget(self.diagnosticsTilesDefaultPage1)
        self.diagnosticsTilesDefaultPage2 = QWidget()
        self.diagnosticsTilesDefaultPage2.setObjectName(u"diagnosticsTilesDefaultPage2")
        self.diagnosticsTilesDefaultPage.addWidget(self.diagnosticsTilesDefaultPage2)

        self.verticalLayout_22.addWidget(self.diagnosticsTilesDefaultPage)


        self.diagnosticsTilesLayout.addWidget(self.diagnosticsTilesWindow)


        self.verticalLayout_14.addLayout(self.diagnosticsTilesLayout)


        self.horizontalLayout_7.addWidget(self.diagnosticsTiles)

        self.diagnosticsConsole = QFrame(self.diagnostics)
        self.diagnosticsConsole.setObjectName(u"diagnosticsConsole")
        self.diagnosticsConsole.setMinimumSize(QSize(500, 60))
        self.diagnosticsConsole.setMaximumSize(QSize(500, 16777215))
        self.diagnosticsConsole.setStyleSheet(u"background-color: rgb(13, 16, 21);\n"
"/*border-left: 6px solid rgb(21, 23, 27);*/")
        self.diagnosticsConsole.setFrameShape(QFrame.NoFrame)
        self.diagnosticsConsole.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.diagnosticsConsole)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(9, 9, 9, 5)
        self.diagnosticsConsoleDisplay = QPlainTextEdit(self.diagnosticsConsole)
        self.diagnosticsConsoleDisplay.setObjectName(u"diagnosticsConsoleDisplay")
        self.diagnosticsConsoleDisplay.setStyleSheet(u"border: None;\n"
"background: transparent;\n"
"")
        self.diagnosticsConsoleDisplay.setFrameShape(QFrame.NoFrame)
        self.diagnosticsConsoleDisplay.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.diagnosticsConsoleDisplay.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.diagnosticsConsoleDisplay.setReadOnly(True)

        self.verticalLayout_13.addWidget(self.diagnosticsConsoleDisplay)


        self.horizontalLayout_7.addWidget(self.diagnosticsConsole)

        self.stackedWidget.addWidget(self.diagnostics)
        self.test = QWidget()
        self.test.setObjectName(u"test")
        self.test.setMinimumSize(QSize(1198, 623))
        self.test.setAutoFillBackground(False)
        self.verticalLayout_20 = QVBoxLayout(self.test)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.stackedWidget.addWidget(self.test)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setStyleSheet(u"background-color: rgb(21, 23, 27);")
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setStyleSheet(u"color: rgb(221, 221, 221);")
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setStyleSheet(u"color: rgb(221, 221, 221)")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
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

        self.stackedWidget.setCurrentIndex(2)
        self.diagnosticsTilesDefaultPage.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"mess2", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"ace lab @ wpi", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_diagnostics.setText(QCoreApplication.translate("MainWindow", u"Diagnostics", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zen"
                        "o Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#8be9fd;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Modular Experiment Software System 2", None))
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
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.diagnosticsMenu1ExperimentSelectionLabel.setText(QCoreApplication.translate("MainWindow", u"EXPERIMENT SELECTION", None))
        self.diagnosticsMenu1ExperimentFileLabel.setText(QCoreApplication.translate("MainWindow", u"Experiment File:", None))
        self.diagnosticsMenu1ExperimentFileText.setText("")
        self.buttonExperimentSelect.setText("")
        self.buttonExperimentLoad.setText(QCoreApplication.translate("MainWindow", u"Load Experiment", None))
        self.dataCollectionLabel.setText(QCoreApplication.translate("MainWindow", u"EXPERIMENT SETTINGS", None))
        self.dataCollectionPathLabel.setText(QCoreApplication.translate("MainWindow", u"Save Path:", None))
        self.logSavePathText.setText("")
        self.btn_log_save_path_select.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Subdirectories for each trial are auto-generated", None))
        self.btn_logs_download.setText(QCoreApplication.translate("MainWindow", u"Download Experiment Logs", None))
        self.diagnosticsMenu1ExperimentLocalOpsLabel.setText(QCoreApplication.translate("MainWindow", u"LOCAL OPERATIONS", None))
        self.buttonROS2LocalLaunchShutdown.setText(QCoreApplication.translate("MainWindow", u"Launch Local ROS2 Nodes", None))
        self.diagnosticsMenu1ExperimentRemoteOpsLabel.setText(QCoreApplication.translate("MainWindow", u"REMOTE OPERATIONS", None))
        self.buttonNetworkRemoteConnectDisconnect.setText(QCoreApplication.translate("MainWindow", u"Connect to Remote Devices", None))
        self.buttonROS2RemoteLaunchShutdown.setText(QCoreApplication.translate("MainWindow", u"Launch Remote ROS2 Nodes", None))
        self.buttonExperimentRunAbort.setText(QCoreApplication.translate("MainWindow", u"Run Experiment", None))
        self.buttonDiagnosticsRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Marina J. Nelson", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v0.2.1", None))
    # retranslateUi

