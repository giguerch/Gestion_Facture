# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RAPPORT_CLIENT.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog


class Ui_RAPPORT_CLIENT(QDialog):
    '''Interface d'utilisateur du Rapport Client'''
    def __init__(self, Dialog):
        super(Ui_RAPPORT_CLIENT, self).__init__(Dialog)
        self.setObjectName("Dialog")
        self.resize(574, 656)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(210, 600, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.treeWidget = QtWidgets.QTreeWidget(self)
        self.treeWidget.setGeometry(QtCore.QRect(20, 50, 361, 511))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)

        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.exec_()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "Statistique sur les clients"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Dialog", "Total "))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("Dialog", "Nb de factures: 30"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("Dialog", "Année du premier contrat: 2008"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("Dialog", "Année du dernier contrat: 2022"))
        self.treeWidget.topLevelItem(0).child(3).setText(0, _translate("Dialog", "Montant total: 100000$"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Dialog", "Sandra Favret"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("Dialog", "Nb de factures: 3"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("Dialog", "Année du premier contrat: 2012"))
        self.treeWidget.topLevelItem(1).child(2).setText(0, _translate("Dialog", "Année du dernier contrat: 2022"))
        self.treeWidget.topLevelItem(1).child(3).setText(0, _translate("Dialog", "Montant total: 20000$"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("Dialog", "Isabelle Brunette"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("Dialog", "Nb de factures: 2"))
        self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("Dialog", "Année du premier contrat: 2015"))
        self.treeWidget.topLevelItem(2).child(2).setText(0, _translate("Dialog", "Année du dernier contrat: 2015"))
        self.treeWidget.topLevelItem(2).child(3).setText(0, _translate("Dialog", "Montant total: 3000$"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)