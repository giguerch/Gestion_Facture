# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ADRESSE.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from ADRESSE import ADRESSE, ADRESSE_LIST
from functools import partial

class Ui_ADRESSE(QDialog):
    def __init__(self, Dialog):
        super(Ui_ADRESSE, self).__init__()
        self.setObjectName("ADRESSE")
        self.resize(667, 782)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(310, 730, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.Liste_Adresse = QtWidgets.QTreeWidget(self)
        self.Liste_Adresse.setGeometry(QtCore.QRect(60, 80, 501, 321))
        self.Liste_Adresse.setObjectName("Liste_Adresse")
        self.Chercher_Address = QtWidgets.QLineEdit(self)
        self.Chercher_Address.setGeometry(QtCore.QRect(60, 40, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Chercher_Address.setFont(font)
        self.Chercher_Address.setObjectName("Chercher_Address")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(60, 540, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(60, 430, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(60, 660, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.Nom_Adresse = QtWidgets.QLineEdit(self)
        self.Nom_Adresse.setGeometry(QtCore.QRect(130, 460, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Nom_Adresse.setFont(font)
        self.Nom_Adresse.setObjectName("Nom_Adresse")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(60, 580, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(60, 460, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.CP_Edit = QtWidgets.QLineEdit(self)
        self.CP_Edit.setGeometry(QtCore.QRect(450, 660, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CP_Edit.setFont(font)
        self.CP_Edit.setAlignment(QtCore.Qt.AlignCenter)
        self.CP_Edit.setObjectName("CP_Edit")
        self.Ville_Edit = QtWidgets.QLineEdit(self)
        self.Ville_Edit.setGeometry(QtCore.QRect(130, 620, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Ville_Edit.setFont(font)
        self.Ville_Edit.setObjectName("Ville_Edit")
        self.Lieu2_Edit = QtWidgets.QLineEdit(self)
        self.Lieu2_Edit.setGeometry(QtCore.QRect(130, 540, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Lieu2_Edit.setFont(font)
        self.Lieu2_Edit.setObjectName("Lieu2_Edit")
        self.Adresse_Edit = QtWidgets.QLineEdit(self)
        self.Adresse_Edit.setGeometry(QtCore.QRect(130, 580, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Adresse_Edit.setFont(font)
        self.Adresse_Edit.setObjectName("Adresse_Edit")
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(360, 660, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(60, 500, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(60, 620, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.Ajouter_Adresse = QtWidgets.QPushButton(self)
        self.Ajouter_Adresse.setGeometry(QtCore.QRect(220, 420, 121, 31))
        self.Ajouter_Adresse.setObjectName("Ajouter_Adresse")
        self.Retirer_Adresse = QtWidgets.QPushButton(self)
        self.Retirer_Adresse.setGeometry(QtCore.QRect(350, 420, 121, 31))
        self.Retirer_Adresse.setObjectName("Retirer_Adresse")
        self.Lieu1_Edit = QtWidgets.QLineEdit(self)
        self.Lieu1_Edit.setGeometry(QtCore.QRect(130, 500, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Lieu1_Edit.setFont(font)
        self.Lieu1_Edit.setObjectName("Lieu1_Edit")
        self.Province_Combo = QtWidgets.QComboBox(self)
        self.Province_Combo.setGeometry(QtCore.QRect(130, 660, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Province_Combo.setFont(font)
        self.Province_Combo.setObjectName("Province_Combo")
        self.Province_Combo.addItem("")
        self.Province_Combo.addItem("")
        self.AL = ADRESSE_LIST()
        self.retranslateUi(self)
        self.buttonBox.accepted.connect(partial(self.MAJ, Dialog))
        self.buttonBox.rejected.connect(self.reject)
        self.Ajouter_Adresse.clicked.connect(self.ajouter)
        self.Retirer_Adresse.clicked.connect(self.retirer)
        self.Chercher_Address.textChanged.connect(self.find)
        
        QtCore.QMetaObject.connectSlotsByName(self)
        self.exec_()

    def MAJ(self, diag):
        self.accept()
        INDEX = self.Liste_Adresse.selectedIndexes()
        if len(INDEX):
            i = self.Liste_Adresse.selectedIndexes()[0]
            ind = int(i.row())
            test = -1
            for i, c in enumerate(self.AL.CLF):
                if c:
                    test += 1
                else:
                    pass
                if test == ind:
                    ind = i
                    break
            ID = self.AL.CL[ind].ID
            diag.id = ID
        else:
            diag.id = -1     
        
    def find(self):
        txt_filter = self.Chercher_Address.text()        
        if txt_filter != "Chercher Client":
             self.AL.filter(txt_filter)
        self.reload()
        
        
        
    def reload(self):
        self.Liste_Adresse.clear()
        test = -1
        for i,j in enumerate(self.AL.CL):
            if self.AL.CLF[i]:
                test = test + 1
                item_0 = QtWidgets.QTreeWidgetItem(self.Liste_Adresse)
                item_1 = QtWidgets.QTreeWidgetItem(item_0)
                item_1 = QtWidgets.QTreeWidgetItem(item_0)
                item_1 = QtWidgets.QTreeWidgetItem(item_0)
                item_1 = QtWidgets.QTreeWidgetItem(item_0)
                item_1 = QtWidgets.QTreeWidgetItem(item_0)
                item_1 = QtWidgets.QTreeWidgetItem(item_0)
                self.Liste_Adresse.topLevelItem(test).setText(0, j.NOM)
                self.Liste_Adresse.topLevelItem(test).child(0).setText(0, j.LIEU1)
                self.Liste_Adresse.topLevelItem(test).child(1).setText(0, j.LIEU2)
                self.Liste_Adresse.topLevelItem(test).child(2).setText(0, j.ADRESSE)
                self.Liste_Adresse.topLevelItem(test).child(3).setText(0, j.VILLE)
                self.Liste_Adresse.topLevelItem(test).child(4).setText(0, j.PROVINCE)
                self.Liste_Adresse.topLevelItem(test).child(5).setText(0, j.CP)
                
    def ajouter(self):
        self.AL.add(ID       = self.AL.max_id() + 1,
                    NOM      = self.Nom_Adresse.text(),
                    LIEU1    = self.Lieu1_Edit.text(),
                    LIEU2    = self.Lieu2_Edit.text(),
                    ADR      = self.Adresse_Edit.text(),
                    VILLE    = self.Ville_Edit.text(),
                    PROVINCE = self.Province_Combo.currentText(),
                    CP       = self.CP_Edit.text())
        self.reload()

    def retirer(self):
        i = self.Liste_Adresse.selectedIndexes()[0]
        ind = int(i.row())
        test = -1
        for i, c in enumerate(self.AL.CLF):
            if c:
                test += 1
            else:
                pass
            if test == ind:
                ind = i
                break
        ID = self.AL.CL[ind].ID
        self.AL.delete(ID)        
        self.reload()
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Liste_Adresse.headerItem().setText(0, _translate("Dialog", "Adresse de Facturation"))
        __sortingEnabled = self.Liste_Adresse.isSortingEnabled()
        self.Liste_Adresse.setSortingEnabled(False)
        self.Liste_Adresse.setSortingEnabled(__sortingEnabled)
        Dialog.setTabOrder(self.Chercher_Address, self.Liste_Adresse)
        Dialog.setTabOrder(self.Liste_Adresse, self.Ajouter_Adresse)
        Dialog.setTabOrder(self.Ajouter_Adresse, self.Retirer_Adresse)
        Dialog.setTabOrder(self.Retirer_Adresse, self.Nom_Adresse)
        Dialog.setTabOrder(self.Nom_Adresse, self.Lieu1_Edit)
        Dialog.setTabOrder(self.Lieu1_Edit, self.Lieu2_Edit)
        Dialog.setTabOrder(self.Lieu2_Edit, self.Adresse_Edit)
        Dialog.setTabOrder(self.Adresse_Edit, self.Ville_Edit)
        Dialog.setTabOrder(self.Ville_Edit, self.Province_Combo)
        Dialog.setTabOrder(self.Province_Combo, self.CP_Edit)
        self.reload()
        self.Chercher_Address.setText(_translate("Dialog", "Chercher Adresse"))
        self.label_6.setText(_translate("Dialog", "Lieu 2"))
        self.label_3.setText(_translate("Dialog", "Nouvelle Adresse"))
        self.label_9.setText(_translate("Dialog", "Province"))
        self.label_7.setText(_translate("Dialog", "Adresse"))
        self.label_4.setText(_translate("Dialog", "Nom"))
        self.CP_Edit.setInputMask(_translate("Dialog", "A9A-9A9"))
        self.CP_Edit.setText(_translate("Dialog", "-"))
        self.label_10.setText(_translate("Dialog", "Code Postal"))
        self.label_5.setText(_translate("Dialog", "Lieu 1"))
        self.label_8.setText(_translate("Dialog", "Ville"))
        self.Ajouter_Adresse.setText(_translate("Dialog", "Ajouter à la liste"))
        self.Retirer_Adresse.setText(_translate("Dialog", "Retirer à la liste"))
        self.Province_Combo.setItemText(0, _translate("Dialog", "Québec"))
        self.Province_Combo.setItemText(1, _translate("Dialog", "Ontario"))

