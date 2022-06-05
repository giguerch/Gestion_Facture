# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CLIENT.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from CLIENT import CLIENT_LIST
from ADRESSE import ADRESSE
from ADRESSE_UI import Ui_ADRESSE


class Ui_CLIENT(QDialog):
    def __init__(self, Dialog):
        super(Ui_CLIENT, self).__init__(Dialog)
        self.setObjectName("Dialog")
        self.resize(850, 575)
        self.Liste_Client = QtWidgets.QListWidget(self)
        self.Liste_Client.setGeometry(QtCore.QRect(10, 80, 281, 321))
        self.Liste_Client.setObjectName("Liste_Client")
        item = QtWidgets.QListWidgetItem()
        self.Liste_Client.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Liste_Client.addItem(item)
        self.NewClient_Titre_Edit = QtWidgets.QLineEdit(self)
        self.NewClient_Titre_Edit.setGeometry(QtCore.QRect(170, 450, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)

        self.NewClient_Titre_Edit.setFont(font)
        self.NewClient_Titre_Edit.setObjectName("NewClient_Titre_Edit")
        self.NewClient_Label = QtWidgets.QLabel(self)
        self.NewClient_Label.setGeometry(QtCore.QRect(30, 450, 131, 21))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.NewClient_Label.setFont(font)
        self.NewClient_Label.setObjectName("NewClient_Label")
        self.NouveauClient_Bouton = QtWidgets.QPushButton(self)
        self.NouveauClient_Bouton.setGeometry(QtCore.QRect(240, 410, 93, 31))
        self.NouveauClient_Bouton.setObjectName("NouveauClient_Bouton")

        self.RetirerClient_Bouton = QtWidgets.QPushButton(self)
        self.RetirerClient_Bouton.setGeometry(QtCore.QRect(140, 410, 93, 31))
        self.RetirerClient_Bouton.setObjectName("RetirerClient_Bouton")

        self.SelectClient_Label = QtWidgets.QLabel(self)
        self.SelectClient_Label.setGeometry(QtCore.QRect(10, 0, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SelectClient_Label.setFont(font)
        self.SelectClient_Label.setObjectName("SelectClient_Label")
        self.ChercherClient_Edit = QtWidgets.QLineEdit(self)
        self.ChercherClient_Edit.setGeometry(QtCore.QRect(10, 40, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ChercherClient_Edit.setFont(font)
        self.ChercherClient_Edit.setObjectName("ChercherClient_Edit")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(310, 200, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(310, 320, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.Nom_Adresse_Edit = QtWidgets.QLineEdit(self)
        self.Nom_Adresse_Edit.setGeometry(QtCore.QRect(380, 110, 450, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Nom_Adresse_Edit.setFont(font)
        self.Nom_Adresse_Edit.setObjectName("Nom_Adresse_Edit")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(310, 240, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(310, 120, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.CP_Edit = QtWidgets.QLineEdit(self)
        self.CP_Edit.setGeometry(QtCore.QRect(600, 320, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CP_Edit.setFont(font)
        self.CP_Edit.setAlignment(QtCore.Qt.AlignCenter)
        self.CP_Edit.setObjectName("CP_Edit")
        self.Ville_Edit = QtWidgets.QLineEdit(self)
        self.Ville_Edit.setGeometry(QtCore.QRect(380, 270, 450, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Ville_Edit.setFont(font)
        self.Ville_Edit.setObjectName("Ville_Edit")
        self.Lieu2_Edit = QtWidgets.QLineEdit(self)
        self.Lieu2_Edit.setGeometry(QtCore.QRect(380, 190, 450, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Lieu2_Edit.setFont(font)
        self.Lieu2_Edit.setObjectName("Lieu2_Edit")
        self.Adresse_Edit = QtWidgets.QLineEdit(self)
        self.Adresse_Edit.setGeometry(QtCore.QRect(380, 230, 450, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Adresse_Edit.setFont(font)
        self.Adresse_Edit.setObjectName("Adresse_Edit")
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(570, 320, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(310, 160, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(310, 280, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.Adresse_Bouton = QtWidgets.QPushButton(self)
        self.Adresse_Bouton.setGeometry(QtCore.QRect(380, 70, 241, 31))
        self.Adresse_Bouton.setObjectName("Adresse_Bouton")
        self.Lieu1_Edit = QtWidgets.QLineEdit(self)
        self.Lieu1_Edit.setGeometry(QtCore.QRect(380, 150, 450, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Lieu1_Edit.setFont(font)
        self.Lieu1_Edit.setObjectName("Lieu1_Edit")
        self.Province_Combo = QtWidgets.QComboBox(self)
        self.Province_Combo.setGeometry(QtCore.QRect(380, 320, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Province_Combo.setFont(font)
        self.Province_Combo.setObjectName("Province_Combo")
        self.Province_Combo.addItem("")
        self.Province_Combo.addItem("")
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(450, 530, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel |
                                          QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.CL = CLIENT_LIST()
        self.NewClient_Label_2 = QtWidgets.QLabel(self)
        self.NewClient_Label_2.setGeometry(QtCore.QRect(30, 490, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NewClient_Label_2.setFont(font)
        self.NewClient_Label_2.setObjectName("NewClient_Label_2")
        self.NewClient_Prenom_Edit = QtWidgets.QLineEdit(self)
        self.NewClient_Prenom_Edit.setGeometry(QtCore.QRect(170, 490, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NewClient_Prenom_Edit.setFont(font)
        self.NewClient_Prenom_Edit.setObjectName("NewClient_Prenom_Edit")
        self.NewClient_Label_3 = QtWidgets.QLabel(self)
        self.NewClient_Label_3.setGeometry(QtCore.QRect(30, 530, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NewClient_Label_3.setFont(font)
        self.NewClient_Label_3.setObjectName("NewClient_Label_3")
        self.NewClient_Nom_Edit = QtWidgets.QLineEdit(self)
        self.NewClient_Nom_Edit.setGeometry(QtCore.QRect(170, 530, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NewClient_Nom_Edit.setFont(font)
        self.NewClient_Nom_Edit.setObjectName("NewClient_Nom_Edit")
        self.NouveauClient_Bouton.clicked.connect(self.Add_Client)
        self.ChercherClient_Edit.setText("Chercher Client")
        self.ChercherClient_Edit.textChanged.connect(self.Filter)
        self.RetirerClient_Bouton.clicked.connect(self.Retirer)
        self.id_list = list()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.retranslateUi(self)
        self.Liste_Client.clicked.connect(self.change_adresse)
        self.Adresse_Bouton.clicked.connect(self.Ouvrir_Adresse)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.exec_()

    def Ouvrir_Adresse(self):
        diag = QDialog
        Ui_ADRESSE(diag)
        if (len(self.Liste_Client.selectedIndexes()) != 0 and diag.id != -1):
            i = self.Liste_Client.selectedIndexes()[0]
            ind = int(i.row())
            test = -1
            for i, c in enumerate(self.CL.CLF):
                if c:
                    test += 1
                else:
                    pass
                if test == ind:
                    ind = i
                    break
            ID = self.CL.CL[ind].ID
            self.CL.update(ID, ID_ADRESSE=diag.id)
            self.change_adresse()

    def Filter(self):
        txt_filter = self.ChercherClient_Edit.text()
        if txt_filter != "Chercher Client":
            self.CL.filter(txt_filter)
        self.Reload_Item()

    def Retirer(self):
        i = self.Liste_Client.selectedIndexes()[0]
        ind = int(i.row())
        test = -1
        for i, c in enumerate(self.CL.CLF):
            if c:
                test += 1
            else:
                pass
            if test == ind:
                ind = i
                break
        ID = self.CL.CL[ind].ID
        self.CL.delete(ID)
        self.Reload_Item()

    def Reload_Item(self):
        self.Liste_Client.clear()
        self.id_list.clear()
        for i, cl in enumerate(self.CL.CL):
            if self.CL.CLF[i]:
                CL = "{} {} {}".format(cl.TITRE_CLIENT,
                                       cl.PRENOM_CLIENT,
                                       cl.NOM_CLIENT)
                item = QtWidgets.QListWidgetItem(CL)
                self.id_list.append(cl.ID)
                self.Liste_Client.addItem(item)

    def Add_Client(self):
        titre = self.NewClient_Titre_Edit.text()
        prenom = self.NewClient_Prenom_Edit.text()
        nom = self.NewClient_Nom_Edit.text()
        id = self.CL.max_id() + 1
        self.CL.add(id, titre, prenom, nom)
        self.Filter()

    def change_adresse(self):
        i = self.Liste_Client.selectedIndexes()[0]
        ind = int(i.row())
        test = -1
        for i, c in enumerate(self.CL.CLF):
            if c:
                test += 1
            else:
                pass
            if test == ind:
                ind = i
                break
        ID_ADRESSE = self.CL.CL[ind].ID_ADRESSE
        if ID_ADRESSE != '':
            AD = ADRESSE()
            AD.from_id(ID_ADRESSE)
            self.Nom_Adresse_Edit.setText(AD.NOM)
            self.Lieu1_Edit.setText(AD.LIEU1)
            self.Lieu2_Edit.setText(AD.LIEU2)
            self.Adresse_Edit.setText(AD.ADRESSE)
            self.Ville_Edit.setText(AD.VILLE)
            self.Province_Combo.setCurrentText(AD.PROVINCE)
            self.CP_Edit.setText(AD.CP)
        else:
            self.Nom_Adresse_Edit.setText('')
            self.Lieu1_Edit.setText('')
            self.Lieu2_Edit.setText('')
            self.Adresse_Edit.setText('')
            self.Ville_Edit.setText('')
            self.Province_Combo.setCurrentText('')
            self.CP_Edit.setText('')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.Liste_Client.isSortingEnabled()
        self.setTabOrder(self.ChercherClient_Edit, self.Liste_Client)
        self.setTabOrder(self.Liste_Client, self.NouveauClient_Bouton)
        self.setTabOrder(self.NouveauClient_Bouton, self.NewClient_Titre_Edit)
        self.setTabOrder(self.NewClient_Titre_Edit, self.NewClient_Prenom_Edit)
        self.setTabOrder(self.NewClient_Prenom_Edit, self.NewClient_Nom_Edit)
        self.setTabOrder(self.NewClient_Nom_Edit, self.Adresse_Bouton)
        self.setTabOrder(self.Adresse_Bouton, self.Nom_Adresse_Edit)
        self.setTabOrder(self.Nom_Adresse_Edit, self.Lieu1_Edit)
        self.setTabOrder(self.Lieu1_Edit, self.Lieu2_Edit)
        self.setTabOrder(self.Lieu2_Edit, self.Adresse_Edit)
        self.setTabOrder(self.Adresse_Edit, self.Ville_Edit)
        self.setTabOrder(self.Ville_Edit, self.Province_Combo)
        self.setTabOrder(self.Province_Combo, self.CP_Edit)
        self.Liste_Client.setSortingEnabled(False)
        self.Reload_Item()
        self.Liste_Client.setSortingEnabled(__sortingEnabled)
        self.NewClient_Label.setText(_translate("Dialog", "Titre (Ex: Dr)"))
        self.NouveauClient_Bouton.setText(_translate("Dialog", "Ajouter"))
        self.RetirerClient_Bouton.setText(_translate("Dialog", "Retirer"))
        self.SelectClient_Label.setText(_translate("Dialog",
                                                   "Sélectionner le client"))
        self.label_6.setText(_translate("Dialog", "Lieu 2"))
        self.label_9.setText(_translate("Dialog", "Province"))
        self.label_7.setText(_translate("Dialog", "Adresse"))
        self.label_4.setText(_translate("Dialog", "Nom"))
        self.CP_Edit.setInputMask(_translate("Dialog", "A9A-9A9"))
        self.CP_Edit.setText(_translate("Dialog", "-"))
        self.label_10.setText(_translate("Dialog", "CP"))
        self.label_5.setText(_translate("Dialog", "Lieu 1"))
        self.label_8.setText(_translate("Dialog", "Ville"))
        self.Adresse_Bouton.setText(_translate("Dialog",
                                               "Assigner/changer l\'adresse" +
                                               " du Client"))
        self.Province_Combo.setItemText(0, _translate("Dialog", "Québec"))
        self.Province_Combo.setItemText(1, _translate("Dialog", "Ontario"))
        self.NewClient_Label_2.setText(_translate("Dialog", "Prénom"))
        self.NewClient_Label_3.setText(_translate("Dialog", "Nom de famille"))
