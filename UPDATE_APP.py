# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 21:10:59 2022.

@author: Charles-Édouard Giguère
"""

import tkinter
from tkinter import filedialog
import os
import shutil


# On part un processus tk mais on ne l'affiche pas.
root = tkinter.Tk()
root.withdraw()  # use to hide tkinter window

# On part une fenêtre pour choisir un répertoire
currdir = os.getcwd()
tempdir = filedialog.askdirectory(parent=root,
                                  initialdir=currdir,
                                  title='Please select a directory')


test = os.listdir()
test.remove('.git')
test.remove('.gitignore')
test.remove('__pycache__')
test.remove('FACTURES')
test.remove('SQLCREATE')
test.remove('USER_INTERFACE')
test.remove('FACTURE.sqlt')

for t in test:
    shutil.copyfile(currdir + "\\" + t,
                    tempdir + "\\" + t)
