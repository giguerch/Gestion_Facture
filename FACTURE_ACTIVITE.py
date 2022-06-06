# -*-  coding: utf-8 -*-
# Auteur: Charles-Édouard Giguère

# Classe pour gérer un objet de type FACTURE.

############################
# Base de données.         #
#                          #
#  - FACTURE               #
#    + [ID]                #
#    + [ID_FACTURE]        #
#    + [DATE]              #
#    + [DESCRIPTION]       #
#    + [NB_HEURES]         #
#                          #
############################

import sqlite3


class FACTURE_ACTIVITE:
    """ Sert à créer un client individuel"""

    def __init__(self, ID='', ID_FACTURE='', DATE='',
                 DESCRIPTION='', NB_HEURES=''):
        self.ID = ID
        self.ID_FACTURE = ID_FACTURE
        self.DATE = DATE
        self.DESCRIPTION = DESCRIPTION
        self.NB_HEURES = NB_HEURES

    def update(self, sqlupdate=False, **kwargs):
        """You can update one or more of the 9 attributes of FACTURE"""
        for key, Value in kwargs.items():
            if "ID" == key:
                self.ID = Value
            if "ID_FACTURE" == key:
                self.ID_FACTURE = Value
            if "DATE" == key:
                self.DATE = Value
            if "DESCRIPTION" == key:
                self.DESCRIPTION = Value
            if "NB_HEURES" == key:
                self.NB_HEURES = Value

    def print(self):
        print("{} {} {} {} {}".format(self.ID,
                                      self.ID_FACTURE,
                                      self.DATE,
                                      self.DESCRIPTION,
                                      self.NB_HEURES))

    def __lt__(self, other):
        """ Fonction pour ordonner la liste de client par ordre alphabétique"""
        left = str(self.ID)
        right = str(other.ID)
        return left < right


class FACTURE_ACTIVITE_LIST:
    """Liste d'adresse de la BD"""

    def __init__(self):
        """Initialise la liste d'adresse en allant chercher dans la BD"""
        self.FAL = list()

    def by_id(self, ID_FACTURE):
        self.FAL.clear()
        self.ID_FACTURE = ID_FACTURE
        conn = None
        try:
            conn = sqlite3.connect("FACTURE.sqlt")
        except sqlite3.Error as e:
            print(e)
        cur = conn.cursor()
        instruct = ("SELECT * FROM FACTURE_ACTIVITE " +
                    "WHERE ID_FACTURE = {}").format(self.ID_FACTURE)
        cur.execute(instruct)
        rows = cur.fetchall()
        if len(rows) > 0:
            for row in rows:
                row = list(row)
                for i, r in enumerate(row, start=0):
                    if r is None:
                        row[i] = ''
                self.FAL.append(FACTURE_ACTIVITE(row[0], row[1],
                                                 row[2], row[3], row[4]))
        self.FAL.sort()
        conn.close()

    def add(self, ID, ID_FACTURE='', DATE='',
            DESCRIPTION='', NB_HEURES=''):
        """
        Ajout d'une nouvelle facture. L'ID doit être spécifié.
        """

        self.FAL.append(FACTURE_ACTIVITE(ID, ID_FACTURE, DATE,
                                         DESCRIPTION, NB_HEURES))

        conn = None
        try:
            conn = sqlite3.connect("FACTURE.sqlt")
        except sqlite3.Error as e:
            print(e)
        cur = conn.cursor()
        sqlstr = ("INSERT INTO FACTURE_ACTIVITE(ID, ID_FACTURE, DATE, " +
                  "DESCRIPTION, NB_HEURES) VALUES " +
                  " ({}, {}, \'{}\', \'{}\', {})"
                  ).format(ID,
                           ID_FACTURE,
                           DATE,
                           DESCRIPTION.replace("'", "''"),
                           NB_HEURES)
        cur.execute(sqlstr)
        conn.commit()
        conn.close()
        self.FAL.sort()

    def update(self, ID, **kwargs):
        """ Update d'un client. Un ID doit être spécifié pour que ça marche """
        for i in self.FAL:
            if i.ID == ID:
                conn = None
                try:
                    conn = sqlite3.connect("FACTURE.sqlt")
                except sqlite3.Error as e:
                    print(e)
                i.update(**kwargs)
                cur = conn.cursor()
                sqlstr = ("UPDATE FACTURE_ACTIVITE SET ID_FACTURE  = {}," +
                          "DATE = \'{}\'," +
                          "DESCRIPTION = \'{}\'," +
                          "NB_HEURES = {} " +
                          "WHERE ID   = {}")
                sqlstr = sqlstr.format(i.ID_FACTURE,
                                       i.DATE,
                                       i.DESCRIPTION,
                                       i.NB_HEURES,
                                       i.ID)
                cur.execute(sqlstr)
                conn.commit()
                conn.close()
        self.FAL.sort()

    def delete(self, ID):
        for i, v in enumerate(self.FAL):
            if v.ID == ID:
                self.FAL.pop(i)
                conn = None
                try:
                    conn = sqlite3.connect("FACTURE.sqlt")
                except sqlite3.Error as e:
                    print(e)
                cur = conn.cursor()
                cur.execute(("DELETE FROM FACTURE_ACTIVITE"
                             " WHERE ID = {}").format(ID))
                conn.commit()
                conn.close()

    def print(self):
        """Affichage de la liste des activités de facture dans la console"""
        for i, r in enumerate(self.FAL):
            r.print()

    def max_id(self):
        """ Trouver le numéro d'identité"""
        conn = None
        try:
            conn = sqlite3.connect("FACTURE.sqlt")
        except sqlite3.Error as e:
            print(e)
        cur = conn.cursor()
        cur.execute("SELECT MAX(ID) FROM FACTURE_ACTIVITE")
        rows = cur.fetchall()
        return(int(rows[0][0]))


if __name__ == "__main__":
    FAL1 = FACTURE_ACTIVITE_LIST()
    FAL1.by_id(8739927)
    print("LISTE 1:")
    FAL1.print()
    FAL1.update(6, DESCRIPTION="Description des tâches")
    FAL1.print()
