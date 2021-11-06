# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyMessangerQuxauK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QLabel(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 40, 681, 461))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.textEdit.setWordWrap(False)
        self.entry = QTextEdit(self.centralwidget)
        self.entry.setObjectName(u"entry")
        self.entry.setGeometry(QRect(10, 520, 681, 31))
        self.send_button = QPushButton(self.centralwidget)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setGeometry(QRect(700, 520, 75, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        self.send_button.setFont(font1)
        self.send_button.setAutoDefault(False)
        self.send_button.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.send_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textEdit.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><br/></p></body></html>", None))
        self.entry.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.send_button.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi

