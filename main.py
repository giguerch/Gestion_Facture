# -*- Coding: utf-8 -*-
"""
Programme principal du traitement de facture.

Auteur: Charles-Edouard
Cree le 2020-04-22
"""

import sys
from PyQt5 import QtWidgets
from MAIN_WINDOW_UI import Ui_MainWindow

# We starts the main window.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QMainWindow()
    prog = Ui_MainWindow()
    prog.show()
    sys.exit(app.exec_())
