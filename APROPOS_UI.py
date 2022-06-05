# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'APROPOS.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog


class Ui_APROPOS(QDialog):
    '''Class Apropos to display the about menu '''

    def __init__(self, Dialog):
        super(Ui_APROPOS, self).__init__(Dialog)
        self.setObjectName("Dialog")
        self.resize(350, 100)
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 350, 100))
        self.textBrowser.setObjectName("textBrowser")
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.exec_()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "À propos"))
        with open('APROPOS.html', 'r', encoding="utf-8") as AP:
            message = AP.read()
        self.textBrowser.setHtml(_translate("self", message))
