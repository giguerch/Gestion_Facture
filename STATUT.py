# -*-  Coding: utf-8 -*-
# Programme pour gérer mes factures

# Classe qui gère la base de données facture.
# Ajouter
# Chercher
# Retirer
# Editer

############################
# Base de données.         #
#                          #
#  - STATUT                #
#    + [ID]                #
#    + [DESCRIPTION]       #
#        (En attente/Payé) #
#                          #
###########################

class STATUT:
    def __init__(self, ID=None, DESCRIPTION=None):
        self.ID = ID
        self.DESCRIPTION = DESCRIPTION

    description = "Objet contenant le type de statut"
    author = "Charles-Édouard Giguère"
