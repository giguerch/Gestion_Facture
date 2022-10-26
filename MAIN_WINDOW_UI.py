# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MAIN_WINDOW.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
# -*- Encoding: utf-8 -*-
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QDialog
from APROPOS_UI import Ui_APROPOS
from CLIENT_UI import Ui_CLIENT
from FACTURE import FACTURE_LIST
from FACTURE_ADD_UI import FACTURE_ADD_UI
from FACTURE_MOD_UI import FACTURE_MOD_UI
from RAPPORT_CLIENT_UI import Ui_RAPPORT_CLIENT
from RAPPORT_ANNEE_UI import Ui_RAPPORT_ANNEE
import sys


# Declaration of the main window class of the apps.
# It contains a list of the invoice with the latest on top.
class Ui_MainWindow(QMainWindow):
    def __init__(self):
        # Disposition of the many widgets.
        super(Ui_MainWindow, self).__init__()
        self.setObjectName("Gestionnaire de facture")
        self.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 10, 750, 521))
        self.listWidget.setObjectName("listWidget")
        self.AjouterBouton = QtWidgets.QPushButton(self.centralwidget)
        self.AjouterBouton.setGeometry(QtCore.QRect(800, 50, 141, 31))
        self.AjouterBouton.setObjectName("AjouterBouton")
        self.RetirerBouton = QtWidgets.QPushButton(self.centralwidget)
        self.RetirerBouton.setGeometry(QtCore.QRect(800, 100, 141, 31))
        self.RetirerBouton.setObjectName("pushButton_2")
        self.ModifierBouton = QtWidgets.QPushButton(self.centralwidget)
        self.ModifierBouton.setGeometry(QtCore.QRect(800, 150, 141, 31))
        self.ModifierBouton.setObjectName("pushButton_3")

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuClient = QtWidgets.QMenu(self.menubar)
        self.menuClient.setObjectName("menuClient")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        self.menuRapport = QtWidgets.QMenu(self.menubar)
        self.menuRapport.setObjectName("menuRapport")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(self)
        self.actionExit.setObjectName("actionExit")
        self.action_propos = QtWidgets.QAction(self)
        self.action_propos.setObjectName("action_propos")
        self.actionG_rer_les_clients = QtWidgets.QAction(self)
        self.actionG_rer_les_clients.setObjectName("actionG_rer_les_clients")
        self.actionPar_client = QtWidgets.QAction(self)
        self.actionPar_client.setObjectName("actionPar_client")
        self.actionPar_ann_e = QtWidgets.QAction(self)
        self.actionPar_ann_e.setObjectName("actionPar_ann_e")
        self.actionVisionner_les_factures = QtWidgets.QAction(self)
        self.actionVisionner_les_factures.setObjectName(
            "actionVisionner_les_factures")
        self.actionCr_er_une_facture = QtWidgets.QAction(self)
        self.actionCr_er_une_facture.setObjectName("actionCr_er_une_facture")
        self.menuFichier.addAction(self.actionExit)
        self.menuClient.addAction(self.actionG_rer_les_clients)
        self.menuAide.addAction(self.action_propos)
        self.menuRapport.addAction(self.actionPar_client)
        self.menuRapport.addAction(self.actionPar_ann_e)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuClient.menuAction())
        self.menubar.addAction(self.menuRapport.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        # Closing the main window.
        self.actionExit.triggered.connect(lambda: self.close())
        # Create the invoice list
        self.FL = FACTURE_LIST()
        # Function to initialize contents of invoice list.
        self.Reload_Item()
        # Function addFacture (add invoice) is linked to button AjouterBouton.
        self.AjouterBouton.clicked.connect(self.addFacture)
        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)
        # Call the apropos windows (MENU)
        self.action_propos.triggered.connect(self.apropos)
        # Call the client management window (MENU)
        self.actionG_rer_les_clients.triggered.connect(self.GClient)
        # See stats on clients
        self.actionPar_client.triggered.connect(self.RClient)
        # See stats on year
        self.actionPar_ann_e.triggered.connect(self.RYear)
        # Remove an invoice.
        self.RetirerBouton.clicked.connect(self.remFacture)
        # modify an invoice by clicking modify button or by double clicking
        # on invoice.
        self.ModifierBouton.clicked.connect(self.modFacture)
        self.listWidget.doubleClicked.connect(self.modFacture)

    # Function that calls the stats on client window.
    def RClient(self):
        dial = QDialog()
        Ui_RAPPORT_CLIENT(dial)

    def RYear(self):
        dial = QDialog()
        Ui_RAPPORT_ANNEE(dial)

    # Function that calls the modification window
    def modFacture(self):
        if(len(self.listWidget.selectedIndexes()) > 0):
            dial = QDialog()
            dial.FL = self.FL
            dial.ID = int(self.listWidget.selectedIndexes()[0].row())
            FACTURE_MOD_UI(dial)
            self.Reload_Item()

    # Function that removes an invoice.
    def remFacture(self):
        i = int(self.listWidget.selectedIndexes()[0].row())
        self.FL.delete(ID=self.FL.FL[i].ID)
        self.Reload_Item()

    # Function that calls the "add an invoice" window.
    def addFacture(self):
        dial = QDialog()
        dial.FL = self.FL
        dial.F = None
        FACTURE_ADD_UI(dial)
        self.Reload_Item()

    # Function that displays the apropos window.
    def apropos(self):
        dial = QtWidgets.QDialog()
        Ui_APROPOS(dial)

    # Function that starts the client manager.
    def GClient(self):
        dial = QDialog()
        Ui_CLIENT(dial)

    # Function that reload the lists of invoice everytime a changes is
    # made.
    def Reload_Item(self):
        self.listWidget.clear()
        for i, fl in enumerate(self.FL.FL):
            if self.FL.FLF[i]:
                item = QtWidgets.QListWidgetItem("{}-[{}] {}".format(
                    fl.ID,
                    fl.DATE,
                    fl.PROJET))
                if fl.ID_STATUT == 1:
                    pass
                elif fl.ID_STATUT == 2:
                    item.setForeground(Qt.blue)
                elif fl.ID_STATUT == 3:
                    item.setForeground(Qt.red)
                elif fl.ID_STATUT == 4:
                    item.setForeground(Qt.darkGreen)
                self.listWidget.addItem(item)

    # This is where the name of the widgets are set.
    # The names are in french because I am :)
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.AjouterBouton.setText(_translate("MainWindow",
                                              "Ajouter une facture"))
        self.RetirerBouton.setText(_translate("MainWindow",
                                              "Retirer une facture"))
        self.ModifierBouton.setText(_translate("MainWindow",
                                               "Modifier une facture"))
        self.setWindowTitle(_translate("MainWindow",
                                       "Gestionnaire de facture"))
        self.menuFichier.setTitle(_translate("MainWindow",
                                             "Fichier"))
        self.menuClient.setTitle(_translate("MainWindow",
                                            "Client"))
        self.menuAide.setTitle(_translate("MainWindow", "Aide"))
        self.menuRapport.setTitle(_translate("MainWindow", "Rapport"))
        self.actionExit.setText(_translate("MainWindow", "Quitter"))
        self.action_propos.setText(_translate("MainWindow", "À propos"))
        self.actionG_rer_les_clients.setText(_translate("MainWindow",
                                                        "Gérer les clients"))
        self.actionPar_client.setText(_translate("MainWindow", "Par client"))
        self.actionPar_ann_e.setText(_translate("MainWindow", "Par année"))


# optional argument if this module is called directly.
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QMainWindow()
    prog = Ui_MainWindow()
    prog.show()
    sys.exit(app.exec_())
