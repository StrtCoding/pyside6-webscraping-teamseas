# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pounds_counter.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class ViewPoundsCounter(object):
    def setupUi(self, ViewPoundsCounter):
        if not ViewPoundsCounter.objectName():
            ViewPoundsCounter.setObjectName(u"ViewPoundsCounter")
        ViewPoundsCounter.resize(500, 190)
        ViewPoundsCounter.setStyleSheet(u"background-color: rgb(168, 223, 226);")
        self.label = QLabel(ViewPoundsCounter)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 10, 251, 91))
        self.label.setPixmap(QPixmap(u"./assets/teamseas-tm-logo.png"))
        self.label.setScaledContents(True)
        self.counts_label = QLabel(ViewPoundsCounter)
        self.counts_label.setObjectName(u"counts_label")
        self.counts_label.setGeometry(QRect(0, 120, 501, 61))
        self.counts_label.setStyleSheet(u"")
        self.counts_label.setAlignment(Qt.AlignCenter)
        self.counts_label.setStyleSheet(u"font-size:36pt")

        self.retranslateUi(ViewPoundsCounter)

        QMetaObject.connectSlotsByName(ViewPoundsCounter)
    # setupUi

    def retranslateUi(self, ViewPoundsCounter):
        ViewPoundsCounter.setWindowTitle(QCoreApplication.translate("ViewPoundsCounter", u"Form", None))
        self.counts_label.setText('#Pounds')
        self.counts_label.setText(QCoreApplication.translate("ViewPoundsCounter", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:700;\">#Pounds</span></p></body></html>", None))
    # retranslateUi

