# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tileDiagnosticsPagesmMvnw.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_tileDiagnosticsPage(object):
    def setupUi(self, tileDiagnosticsPage):
        if not tileDiagnosticsPage.objectName():
            tileDiagnosticsPage.setObjectName(u"tileDiagnosticsPage")
        tileDiagnosticsPage.resize(748, 732)
        self.verticalLayout = QVBoxLayout(tileDiagnosticsPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 3, 3, 3)
        self.diagnostics2ScrollArea = QScrollArea(tileDiagnosticsPage)
        self.diagnostics2ScrollArea.setObjectName(u"diagnostics2ScrollArea")
        self.diagnostics2ScrollArea.setFrameShape(QFrame.NoFrame)
        self.diagnostics2ScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.diagnostics2ScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.diagnostics2ScrollArea.setWidgetResizable(True)
        self.diagnostics2ScrollAreaContent = QWidget()
        self.diagnostics2ScrollAreaContent.setObjectName(u"diagnostics2ScrollAreaContent")
        self.diagnostics2ScrollAreaContent.setGeometry(QRect(0, 0, 722, 726))
        self.verticalLayout_2 = QVBoxLayout(self.diagnostics2ScrollAreaContent)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 18, 27, 18)
        self.diagnostics2ScrollAreaLayout = QGridLayout()
        self.diagnostics2ScrollAreaLayout.setSpacing(9)
        self.diagnostics2ScrollAreaLayout.setObjectName(u"diagnostics2ScrollAreaLayout")

        self.verticalLayout_2.addLayout(self.diagnostics2ScrollAreaLayout)

        self.diagnostics2ScrollArea.setWidget(self.diagnostics2ScrollAreaContent)

        self.verticalLayout.addWidget(self.diagnostics2ScrollArea)


        self.retranslateUi(tileDiagnosticsPage)

        QMetaObject.connectSlotsByName(tileDiagnosticsPage)
    # setupUi

    def retranslateUi(self, tileDiagnosticsPage):
        tileDiagnosticsPage.setWindowTitle(QCoreApplication.translate("tileDiagnosticsPage", u"Form", None))
    # retranslateUi

