# -*-  Coding: utf-8 -*-
# Programme pour g�rer mes factures

# Classe qui g�re la base de donn�es facture.
# Ajouter
# Chercher
# Retirer
# Editer

############################
# Base de donn�es.         #
#                          #
#  - STATUT                #
#    + [ID]                #
#    + [DESCRIPTION]       #
#        (En attente/Pay�) #
#                          #
###########################

class STATUT:
    def __init__(self, ID=None, DESCRIPTION=None):
        self.ID = ID
        self.DESCRIPTION = DESCRIPTION

    description = "Objet contenant le type de statut"
    author = "Charles-�douard Gigu�re"
