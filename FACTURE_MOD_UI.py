# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FACTURE.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog
from CLIENT import CLIENT_LIST
from TARIF import TARIF_LIST
from FACTURE_ACTIVITE import FACTURE_ACTIVITE_LIST
from MAKE_FACTURE import FACTURE_PDF
from functools import partial
from os import system
import datetime


class FACTURE_MOD_UI(QDialog):
    def __init__(self, Dialog):
        super(FACTURE_MOD_UI, self).__init__(Dialog)

        self.FL = Dialog.FL
        self.ID = Dialog.ID
        self.setObjectName("Dialog")
        self.resize(692, 723)

        # ID du projet (LABEL et EDIT).
        self.PROJET_ID_LABEL = QtWidgets.QLabel(self)
        self.PROJET_ID_LABEL.setGeometry(QtCore.QRect(150, 10, 61, 22))
        self.PROJET_ID_LABEL.setObjectName("PROJET_ID_LABEL")

        self.ID_PROJET_EDIT = QtWidgets.QLineEdit(self)
        self.ID_PROJET_EDIT.setGeometry(QtCore.QRect(220, 10, 151, 22))
        self.ID_PROJET_EDIT.setObjectName("ID_PROJET_EDIT")

        # Nom du projet (LABEL et EDIT).
        self.PROJET_LABEL = QtWidgets.QLabel(self)
        self.PROJET_LABEL.setGeometry(QtCore.QRect(10, 40, 51, 22))
        self.PROJET_LABEL.setObjectName("label")

        self.NOM_PROJET_EDIT = QtWidgets.QLineEdit(self)
        self.NOM_PROJET_EDIT.setGeometry(QtCore.QRect(70, 40, 401, 22))
        self.NOM_PROJET_EDIT.setObjectName("NOM_PROJET_EDIT")

        # Nom du client (LABEL et COMBO).
        self.CLIENT_LABEL = QtWidgets.QLabel(self)
        self.CLIENT_LABEL.setGeometry(QtCore.QRect(10, 80, 41, 22))
        self.CLIENT_LABEL.setObjectName("label_5")

        self.CLIENT_COMBO = QtWidgets.QComboBox(self)
        self.CLIENT_COMBO.setGeometry(QtCore.QRect(70, 80, 401, 22))
        self.CLIENT_COMBO.setObjectName("CLIENT_COMBO")

        # Periode de la facture (LABEL, COMBO et EDIT)
        self.PERIODE_LABEL = QtWidgets.QLabel(self)
        self.PERIODE_LABEL.setGeometry(QtCore.QRect(10, 120, 55, 22))
        self.PERIODE_LABEL.setObjectName("PERIODE_LABEL")

        self.DE_LABEL = QtWidgets.QLabel(self)
        self.DE_LABEL.setGeometry(QtCore.QRect(70, 120, 21, 22))
        self.DE_LABEL.setObjectName("DE_LABEL")

        self.A_LABEL = QtWidgets.QLabel(self)
        self.A_LABEL.setGeometry(QtCore.QRect(270, 120, 21, 22))
        self.A_LABEL.setObjectName("A_LABEL")

        # Annee periode minimum (EDIT).
        self.ANNEE_MIN_EDIT = QtWidgets.QLineEdit(self)
        self.ANNEE_MIN_EDIT.setGeometry(QtCore.QRect(200, 120, 41, 22))
        self.ANNEE_MIN_EDIT.setObjectName("ANNEE_MIN_EDIT")

        # Mois periode minimum (COMBO).
        self.MOIS_MIN_COMBO = QtWidgets.QComboBox(self)
        self.MOIS_MIN_COMBO.setGeometry(QtCore.QRect(95, 120, 95, 22))
        self.MOIS_MIN_COMBO.setObjectName("MOIS_MIN_COMBO")
        for i in range(0, 12):
            self.MOIS_MIN_COMBO.addItem("")

        # Annee periode maximum (EDIT).
        self.ANNEE_MAX_EDIT = QtWidgets.QLineEdit(self)
        self.ANNEE_MAX_EDIT.setGeometry(QtCore.QRect(410, 120, 41, 22))
        self.ANNEE_MAX_EDIT.setObjectName("ANNEE_MAX_EDIT")

        # Mois periode maximum (COMBO).
        self.MOIS_MAX_COMBO = QtWidgets.QComboBox(self)
        self.MOIS_MAX_COMBO.setGeometry(QtCore.QRect(300, 120, 95, 22))
        self.MOIS_MAX_COMBO.setObjectName("MOIS_MAX_COMBO")
        for i in range(0, 12):
            self.MOIS_MAX_COMBO.addItem("")

        # Date de la facture (LABEL, EDIT).
        self.DATE_LABEL = QtWidgets.QLabel(self)
        self.DATE_LABEL.setGeometry(QtCore.QRect(10, 160, 131, 22))
        self.DATE_LABEL.setObjectName("DATE_LABEL")

        self.DATE_EDIT = QtWidgets.QDateEdit(self)
        self.DATE_EDIT.setGeometry(QtCore.QRect(150, 160, 91, 22))
        now = datetime.datetime.now()
        self.DATE_EDIT.setDateTime(QtCore.QDateTime(QtCore.QDate(now.year,
                                                                 now.month,
                                                                 now.day),
                                                    QtCore.QTime(0, 0, 0)))
        self.DATE_EDIT.setObjectName("DATE_EDIT")

        # Tarif horaire (LABEL, COMBO).
        self.TARIF_LABEL = QtWidgets.QLabel(self)
        self.TARIF_LABEL.setGeometry(QtCore.QRect(260, 160, 91, 22))
        self.TARIF_LABEL.setObjectName("TARIF_LABEL")

        # Tarif horaire set combo.
        self.TARIF_COMBO = QtWidgets.QComboBox(self)
        self.TARIF_COMBO.setGeometry(QtCore.QRect(360, 160, 91, 22))
        self.TARIF_COMBO.setObjectName("TARIF_COMBO")
        self.TL = TARIF_LIST()

        # Liste des activités (LABEL, LISTWIDGET).
        self.ACTIVITE_LABEL = QtWidgets.QLabel(self)
        self.ACTIVITE_LABEL.setGeometry(QtCore.QRect(10, 220, 181, 22))
        self.ACTIVITE_LABEL.setObjectName("ACTIVITE_LABEL")

        self.ACTIVITE_LISTWIDGET = QtWidgets.QListWidget(self)
        self.ACTIVITE_LISTWIDGET.setGeometry(QtCore.QRect(10, 250, 661, 201))
        self.ACTIVITE_LISTWIDGET.setObjectName("ACTIVITE_LISTWIDGET")

        # ligne indiquant le total.
        self.TOTAL_EDIT = QtWidgets.QLineEdit(self)
        self.TOTAL_EDIT.setGeometry(QtCore.QRect(10, 470, 500, 22))
        self.TOTAL_EDIT.setObjectName("TOTAL_EDIT")

        # Bouton pour ajouter une ligne d'activité
        self.AJOUTER_PUSH_BUTTON = QtWidgets.QPushButton(self)
        self.AJOUTER_PUSH_BUTTON.setGeometry(QtCore.QRect(10, 510, 221, 28))
        self.AJOUTER_PUSH_BUTTON.setObjectName("AJOUTER_PUSH_BUTTON")

        # Bouton pour retirer une ligne d'activité
        self.RETIRER_PUSH_BUTTON = QtWidgets.QPushButton(self)
        self.RETIRER_PUSH_BUTTON.setGeometry(QtCore.QRect(240, 510, 221, 28))
        self.RETIRER_PUSH_BUTTON.setObjectName("RETIRER_PUSH_BUTTON")

        # Description de l'activité (LABEL, EDIT).
        self.DESCRIPTION_ACTIVITE_LABEL = QtWidgets.QLabel(self)
        self.DESCRIPTION_ACTIVITE_LABEL.setGeometry(QtCore.QRect(10, 550,
                                                                 81, 22))
        self.DESCRIPTION_ACTIVITE_LABEL.setObjectName(
            "DESCRIPTION_ACTIVITE_LABEL")

        self.DESCRIPTION_ACTIVITE_EDIT = QtWidgets.QLineEdit(self)
        self.DESCRIPTION_ACTIVITE_EDIT.setGeometry(QtCore.QRect(10, 570,
                                                                451, 22))
        self.DESCRIPTION_ACTIVITE_EDIT.setObjectName(
            "DESCRIPTION_ACTIVITE_EDIT")

        # Date de l'activité (LABEL, EDIT).
        self.DATE_ACTIVITE_LABEL = QtWidgets.QLabel(self)
        self.DATE_ACTIVITE_LABEL.setGeometry(QtCore.QRect(10, 610, 131, 16))
        self.DATE_ACTIVITE_LABEL.setObjectName("DATE_ACTIVITE_LABEL")

        self.DATE_ACTIVITE_EDIT = QtWidgets.QDateEdit(self)
        self.DATE_ACTIVITE_EDIT.setGeometry(QtCore.QRect(10, 630, 91, 22))
        now = datetime.datetime.now()
        TSF = QtCore.QDateTime(QtCore.QDate(now.year,
                                            now.month,
                                            now.day), QtCore.QTime(0, 0, 0))
        self.DATE_ACTIVITE_EDIT.setDateTime(TSF)
        self.DATE_ACTIVITE_EDIT.setObjectName("DATE_ACTIVITE_EDIT")

        # Nombre d'heures de l'activité (LABEL, EDIT).
        self.NB_HEURES_LABEL = QtWidgets.QLabel(self)
        self.NB_HEURES_LABEL.setGeometry(QtCore.QRect(250, 610, 111, 16))
        self.NB_HEURES_LABEL.setObjectName("NB_HEURES_LABEL")

        self.NB_HEURES_EDIT = QtWidgets.QLineEdit(self)
        self.NB_HEURES_EDIT.setGeometry(QtCore.QRect(250, 630, 91, 22))
        self.NB_HEURES_EDIT.setInputMethodHints(
            QtCore.Qt.ImhFormattedNumbersOnly)
        self.NB_HEURES_EDIT.setObjectName("NB_HEURES_EDIT")

        # Bouton pour créer la facture.
        self.CREER_FACTURE_BUTTON = QtWidgets.QPushButton(self)
        self.CREER_FACTURE_BUTTON.setGeometry(QtCore.QRect(520, 100, 151, 28))
        self.CREER_FACTURE_BUTTON.setObjectName("CREER_FACTURE_BUTTON")

        # Bouton pour voir la facture.
        self.VOIR_FACTURE_PDF_BUTTON = QtWidgets.QPushButton(self)
        self.VOIR_FACTURE_PDF_BUTTON.setGeometry(
            QtCore.QRect(520, 130, 151, 28))
        self.VOIR_FACTURE_PDF_BUTTON.setObjectName("VOIR_FACTURE_PDF_BUTTON")

        # STATUT de la facture (LABEL, COMBO).
        self.STATUT_FACTURE_LABEL = QtWidgets.QLabel(self)
        self.STATUT_FACTURE_LABEL.setGeometry(QtCore.QRect(522, 10, 151, 22))
        self.STATUT_FACTURE_LABEL.setObjectName("STATUT_FACTURE_LABEL")

        self.STATUT_FACTURE_COMBO = QtWidgets.QComboBox(self)
        self.STATUT_FACTURE_COMBO.setGeometry(QtCore.QRect(522, 40, 151, 22))
        self.STATUT_FACTURE_COMBO.setObjectName("STATUT_FACTURE_COMBO")
        for i in range(0, 4):
            self.STATUT_FACTURE_COMBO.addItem("")

        # Bouton OK Cancel
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(360, 680, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel |
                                          QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        # Liste de client pour le combo.
        self.CL = CLIENT_LIST()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # ordre des inputs.
        Dialog.setTabOrder(self.ID_PROJET_EDIT, self.NOM_PROJET_EDIT)
        Dialog.setTabOrder(self.NOM_PROJET_EDIT, self.CLIENT_COMBO)
        Dialog.setTabOrder(self.CLIENT_COMBO, self.MOIS_MIN_COMBO)
        Dialog.setTabOrder(self.MOIS_MIN_COMBO, self.ANNEE_MIN_EDIT)
        Dialog.setTabOrder(self.ANNEE_MIN_EDIT, self.MOIS_MAX_COMBO)
        Dialog.setTabOrder(self.MOIS_MAX_COMBO, self.ANNEE_MAX_EDIT)
        Dialog.setTabOrder(self.ANNEE_MAX_EDIT, self.DATE_EDIT)
        Dialog.setTabOrder(self.DATE_EDIT, self.TARIF_COMBO)
        Dialog.setTabOrder(self.TARIF_COMBO, self.ACTIVITE_LISTWIDGET)
        Dialog.setTabOrder(self.ACTIVITE_LISTWIDGET, self.AJOUTER_PUSH_BUTTON)
        Dialog.setTabOrder(self.AJOUTER_PUSH_BUTTON, self.RETIRER_PUSH_BUTTON)
        Dialog.setTabOrder(self.RETIRER_PUSH_BUTTON,
                           self.DESCRIPTION_ACTIVITE_EDIT)
        Dialog.setTabOrder(self.DESCRIPTION_ACTIVITE_EDIT,
                           self.DATE_ACTIVITE_EDIT)
        Dialog.setTabOrder(self.DATE_ACTIVITE_EDIT,
                           self.NB_HEURES_EDIT)
        Dialog.setTabOrder(self.NB_HEURES_EDIT,
                           self.CREER_FACTURE_BUTTON)
        Dialog.setTabOrder(self.CREER_FACTURE_BUTTON,
                           self.VOIR_FACTURE_PDF_BUTTON)

        self.retranslateUi(Dialog)

        # Préparation des Champs.
        cFACT = self.FL.FL[self.ID]
        self.FAL = FACTURE_ACTIVITE_LIST()
        self.FAL.by_id(cFACT.ID)
        self.ID_PROJET_EDIT.setText(str(cFACT.ID))
        self.NOM_PROJET_EDIT.setText(cFACT.PROJET)
        for i, v in enumerate(self.CL.CL):
            if(v.ID == cFACT.ID_CLIENT):
                self.CLIENT_COMBO.setCurrentIndex(i)
        self.MOIS_MIN_COMBO.setCurrentIndex(cFACT.PERIODE_MIN_MS-1)
        self.ANNEE_MIN_EDIT.setText(str(cFACT.PERIODE_MIN_YR))
        if(cFACT.PERIODE_MAX_MS != '' and cFACT.PERIODE_MAX_MS != 'Null'):
            self.MOIS_MAX_COMBO.setCurrentIndex(cFACT.PERIODE_MAX_MS-1)
            self.ANNEE_MAX_EDIT.setText(str(cFACT.PERIODE_MAX_YR))
        self.DATE_EDIT.setDate(QtCore.QDate.fromString(cFACT.DATE,
                                                       "yyyy-MM-dd"))
        for i, j in enumerate(self.TL.TL):
            if j.ID == cFACT.ID_TARIF:
                self.TARIF_COMBO.setCurrentIndex(i)
        self.STATUT_FACTURE_COMBO.setCurrentIndex(cFACT.ID_STATUT-1)

        self.HR = 0
        self.TARIF = float(self.TARIF_COMBO.currentText())
        for i, FA in enumerate(self.FAL.FAL):
            self.HR += float(FA.NB_HEURES)
            item = QtWidgets.QListWidgetItem("{} [{} hrs] {}".format(
                FA.DATE,
                '%.2f' % float(FA.NB_HEURES),
                FA.DESCRIPTION))
            self.ACTIVITE_LISTWIDGET.insertItem(i, item)
        self.TOTAL_EDIT.setText("{} heures x {}$ = {}$".format(self.HR,
                                                               self.TARIF,
                                                               self.TARIF *
                                                               self.HR))
        self.AJOUTER_PUSH_BUTTON.clicked.connect(self.ADD_ACTIVITE)
        self.RETIRER_PUSH_BUTTON.clicked.connect(self.REM_ACTIVITE)
        self.buttonBox.accepted.connect(partial(self.MOD_FACTURE, Dialog))
        self.CREER_FACTURE_BUTTON.clicked.connect(self.PREPARE_FACTURE)
        self.VOIR_FACTURE_PDF_BUTTON.clicked.connect(self.OPEN_FACTURE)
        self.exec_()

    def PREPARE_FACTURE(self, ID):
        FACTURE_PDF(self.FL.FL[self.ID].ID)

    # Ajouter une modification de la facture.
    def MOD_FACTURE(self, parent):
        self.accept()
        MMC = "Null"
        MMY = "Null"
        if self.MOIS_MAX_COMBO.currentText() != "":
            MMC = self.MOIS_MAX_COMBO.currentIndex() + 1
            MMY = self.ANNEE_MAX_EDIT.text()
        parent.FL.update(ID=int(self.ID_PROJET_EDIT.text()),
                         PROJET=self.NOM_PROJET_EDIT.text(),
                         PERIODE_MIN_MS=self.MOIS_MIN_COMBO.currentIndex() + 1,
                         PERIODE_MIN_YR=self.ANNEE_MIN_EDIT.text(),
                         PERIODE_MAX_MS=MMC,
                         PERIODE_MAX_YR=MMY,
                         DATE=self.DATE_EDIT.text(),
                         ID_CLIENT=self.CL.CL[
                             self.CLIENT_COMBO.currentIndex()
                             ].ID,
                         ID_STATUT=self.STATUT_FACTURE_COMBO.currentIndex() +
                         1,
                         ID_TARIF=self.TL.TL[
                             self.TARIF_COMBO.currentIndex()
                             ].ID,
                         FACTURE_PDF=1)

    # Ajouter une activité.
    def ADD_ACTIVITE(self):
        self.FAL.add(self.FAL.max_id() + 1, self.FL.FL[self.ID].ID,
                     self.DATE_ACTIVITE_EDIT.text(),
                     self.DESCRIPTION_ACTIVITE_EDIT.text(),
                     self.NB_HEURES_EDIT.text())

        item = QtWidgets.QListWidgetItem(
            "{} [{} hrs] {}".format(self.DATE_ACTIVITE_EDIT.text(),
                                    '%.2f' % float(self.NB_HEURES_EDIT.text()),
                                    self.DESCRIPTION_ACTIVITE_EDIT.text()))
        item = self.ACTIVITE_LISTWIDGET.addItem(item)
        self.DESCRIPTION_ACTIVITE_EDIT.setText("")
        self.HR += float(self.NB_HEURES_EDIT.text())
        self.NB_HEURES_EDIT.setText("")
        self.TOTAL_EDIT.setText(
            "{} heures x {}$ = {}$".format(self.HR,
                                           self.TARIF,
                                           self.TARIF * self.HR))

    # Retirer une activité.
    def REM_ACTIVITE(self):
        i = self.ACTIVITE_LISTWIDGET.selectedIndexes()[0]
        ind = int(i.row())
        self.HR -= float(self.FAL.FAL[ind].NB_HEURES)
        self.TOTAL_EDIT.setText(
            "{} heures x {}$ = {}$".format(self.HR,
                                           self.TARIF,
                                           self.TARIF * self.HR))
        ID = self.FAL.FAL[ind].ID
        self.FAL.delete(ID)
        self.ACTIVITE_LISTWIDGET.takeItem(ind)

    def OPEN_FACTURE(self):
        system(("start "
                "FACTURES/FACTURE_{}.pdf"
                ).format(int(self.ID_PROJET_EDIT.text())))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        # label de l'ID du projet.
        self.PROJET_ID_LABEL.setText(_translate("Dialog", "PROJET ID"))

        # label du nombre du projet.
        self.PROJET_LABEL.setText(_translate("Dialog", "PROJET"))

        # label du client.
        self.CLIENT_LABEL.setText(_translate("Dialog", "CLIENT"))

        # On assigne la liste de Client au Combo.
        for i, cl in enumerate(self.CL.CL):
            nomcl = "{}, {}".format(cl.NOM_CLIENT, cl.PRENOM_CLIENT)
            self.CLIENT_COMBO.addItem("")
            self.CLIENT_COMBO.setItemText(i, _translate("Dialog", nomcl))

        # Période (LABEL).
        self.PERIODE_LABEL.setText(_translate("Dialog", "PÉRIODE:"))
        self.DE_LABEL.setText(_translate("Dialog", "DE"))
        self.A_LABEL.setText(_translate("Dialog", "À"))

        # Valeurs du Combo pour le MOIS MINIMUM et MAXIMUM.
        MOIS = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
                'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre',
                'Décembre', '']
        for i, n in enumerate(MOIS):
            self.MOIS_MIN_COMBO.setItemText(i, _translate("Dialog", n))
            self.MOIS_MAX_COMBO.setItemText(i, _translate("Dialog", n))
        self.MOIS_MAX_COMBO.setCurrentIndex(12)

        # Label date de la facture.
        self.DATE_LABEL.setText(_translate("Dialog", "DATE DE LA FACTURE"))

        # Set value of tarif et choix du combo du tarif.
        self.TARIF_LABEL.setText(_translate("Dialog", "TARIF HORAIRE"))
        for i, j in enumerate(self.TL.TL):
            self.TARIF_COMBO.addItem("")
            self.TARIF_COMBO.setItemText(i, _translate("Dialog", str(j.TAUX)))

        # ListeWidget des activités.
        __sortingEnabled = self.ACTIVITE_LISTWIDGET.isSortingEnabled()
        self.ACTIVITE_LISTWIDGET.setSortingEnabled(False)
        self.ACTIVITE_LISTWIDGET.setSortingEnabled(__sortingEnabled)

        # Label
        self.DESCRIPTION_ACTIVITE_LABEL.setText(
            _translate("Dialog", "DESCRIPTION"))
        self.DATE_ACTIVITE_LABEL.setText(_translate("Dialog",
                                                    "DATE DE LA FACTURE"))
        self.ACTIVITE_LABEL.setText(_translate("Dialog",
                                               "ACTIVITÉS DE LA FACTURE"))
        self.NB_HEURES_LABEL.setText(_translate("Dialog",
                                                "NOMBRE D\'HEURES"))

        # Bouton pour ajouter et retirer des activités de la facture.
        self.AJOUTER_PUSH_BUTTON.setText(
            _translate("Dialog", "AJOUTER ACTIVITÉ DE LA FACTURE"))
        self.RETIRER_PUSH_BUTTON.setText(
            _translate("Dialog", "RETIRER ACTIVITÉ DE LA FACTURE"))

        # Voir/Créer la facture
        self.CREER_FACTURE_BUTTON.setText(
            _translate("Dialog", "CRÉER LA FACTURE PDF"))
        self.VOIR_FACTURE_PDF_BUTTON.setText(
            _translate("Dialog", "VOIR LA FACTURE PDF"))

        # Valeur et label du statut de la facture.
        self.STATUT_FACTURE_LABEL.setText(
            _translate("Dialog", "STATUT FACTURE"))
        self.STATUT_FACTURE_COMBO.setItemText(0,
                                              _translate("Dialog",
                                                         "EN ATTENTE"))
        self.STATUT_FACTURE_COMBO.setItemText(1,
                                              _translate("Dialog", "PAYÉ"))
        self.STATUT_FACTURE_COMBO.setItemText(2,
                                              _translate("Dialog", "ANNULÉ"))
        self.STATUT_FACTURE_COMBO.setItemText(3,
                                              _translate("Dialog",
                                                         "EN TRAITEMENT"))
