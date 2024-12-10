# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tileDiagnosticsLinewRnElr.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_tileDiagnosticsROS2Line(object):
    def setupUi(self, tileDiagnosticsROS2Line):
        if not tileDiagnosticsROS2Line.objectName():
            tileDiagnosticsROS2Line.setObjectName(u"tileDiagnosticsROS2Line")
        tileDiagnosticsROS2Line.resize(326, 18)
        tileDiagnosticsROS2Line.setMinimumSize(QSize(326, 18))
        tileDiagnosticsROS2Line.setMaximumSize(QSize(326, 18))
        tileDiagnosticsROS2Line.setStyleSheet(u"QWidget {\n"
"background: transparent;\n"
"font-size: 10px !important;\n"
"}\n"
"QWidget #node {\n"
"color: rgb(131, 131, 131) !important;\n"
"font-weight: 400 !important;\n"
"}\n"
"QWidget #status_not_running {\n"
"color: rgb(217, 83, 79) !important;\n"
"}\n"
"QWidget #status_running {\n"
"color: rgb(60, 179, 113) !important;\n"
"}")
        self.horizontalLayout = QHBoxLayout(tileDiagnosticsROS2Line)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 0, 4, 0)
        self.node = QLabel(tileDiagnosticsROS2Line)
        self.node.setObjectName(u"node")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.node.sizePolicy().hasHeightForWidth())
        self.node.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.node)

        self.status_running = QLabel(tileDiagnosticsROS2Line)
        self.status_running.setObjectName(u"status_running")

        self.horizontalLayout.addWidget(self.status_running, 0, Qt.AlignRight)

        self.status_not_running = QLabel(tileDiagnosticsROS2Line)
        self.status_not_running.setObjectName(u"status_not_running")

        self.horizontalLayout.addWidget(self.status_not_running, 0, Qt.AlignRight)


        self.retranslateUi(tileDiagnosticsROS2Line)

        QMetaObject.connectSlotsByName(tileDiagnosticsROS2Line)
    # setupUi

    def retranslateUi(self, tileDiagnosticsROS2Line):
        tileDiagnosticsROS2Line.setWindowTitle(QCoreApplication.translate("tileDiagnosticsROS2Line", u"Form", None))
        self.node.setText(QCoreApplication.translate("tileDiagnosticsROS2Line", u"TextLabel", None))
        self.status_running.setText(QCoreApplication.translate("tileDiagnosticsROS2Line", u"running", None))
        self.status_not_running.setText(QCoreApplication.translate("tileDiagnosticsROS2Line", u"not running", None))
    # retranslateUi

