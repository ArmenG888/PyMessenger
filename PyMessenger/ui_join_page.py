# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'join_pageBfymkc.ui'
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
        MainWindow.resize(729, 388)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ip_entry = QLineEdit(self.centralwidget)
        self.ip_entry.setObjectName(u"ip_entry")
        self.ip_entry.setGeometry(QRect(320, 100, 141, 41))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.ip_entry.setFont(font)
        self.ip_entry.setStyleSheet(u"border-radius: 15px;")
        self.port_entry = QLineEdit(self.centralwidget)
        self.port_entry.setObjectName(u"port_entry")
        self.port_entry.setGeometry(QRect(320, 160, 141, 41))
        self.port_entry.setFont(font)
        self.port_entry.setStyleSheet(u"border-radius: 15px;")
        self.username_entry = QLineEdit(self.centralwidget)
        self.username_entry.setObjectName(u"username_entry")
        self.username_entry.setGeometry(QRect(320, 220, 141, 41))
        self.username_entry.setFont(font)
        self.username_entry.setStyleSheet(u"border-radius: 15px;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 110, 51, 21))
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 170, 31, 21))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 230, 71, 21))
        self.label_3.setFont(font)
        self.join_button = QPushButton(self.centralwidget)
        self.join_button.setObjectName(u"join_button")
        self.join_button.setGeometry(QRect(350, 290, 91, 31))
        self.join_button.setFont(font)
        self.join_button.setStyleSheet(u"border-radius: 15px;\n"
"border: 2px solid #42f5f5; background-color:white;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ip_entry.setText("")
        self.port_entry.setText("")
        self.username_entry.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Chat IP", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.join_button.setText(QCoreApplication.translate("MainWindow", u"Join", None))
    # retranslateUi

