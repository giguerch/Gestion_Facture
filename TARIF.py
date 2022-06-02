### -*-       Coding: utf-8         -*-
### Programme pour gérer mes factures.

##############################
## Base de données.         ##
##                          ##
##  - TARIF                 ##
##    + [ID]                ##
##    + [TAUX]              ##
##    + [DATE_CREATION]     ##
##                          ##
##############################

import sqlite3


class TARIF:
    """Sert à creer un tarif individuel"""
    
    def __init__(self, ID = '', TAUX = '', DATE_CREATION = ''):
        """
           Initialise les attributs. Certains (ou tous les) attributs 
           peuvent être nuls ('')
        """
        self.ID            = ID
        self.TAUX          = TAUX 
        self.DATE_CREATION = DATE_CREATION

    def update(self, **kwargs):
        """You can update one or more of the 5 attributes of clients"""
        for key, value in kwargs.items():
            if "ID" == key:
                self.ID = value
            elif "TAUX" == key:
                self.TAUX = value
            elif "DATE_CREATION" == key:
                self.DATE_CREATION = value
        
    def print(self):
        """Affiche les valeurs du Client """
        print("{}, {}, {}".format(self.ID, self.TAUX, self.DATE_CREATION))

    def __lt__(self, other):
        """ Fonction pour ordonner la liste de client par ordre alphabétique"""
        left  = str(self.TAUX) + str(self.TAUX)
        right = str(other.TAUX) + str(other.TAUX)
        return left < right


class TARIF_LIST:
    """Liste de tarif dans la BD"""
    
    def __init__(self):
        """Initialise la liste de tarif en allant chercher dans la BD"""
        self.TL = list()
        conn = None
        try:
            conn = sqlite3.connect("FACTURE.sqlt")
        except Error as e:
            print(e)
        cur = conn.cursor()
        cur.execute("SELECT * FROM TARIF")
        rows = cur.fetchall()
        for row in rows:
            row = list(row)
            for i,r in enumerate(row, start = 0):
                if r == None:
                    row[i] = ''
            self.TL.append(TARIF(row[0], row[1], row[2]))
        self.TL.sort()
        conn.close()

    def add(self, ID, TAUX = '', DATE_CREATION = ''):
        """Ajout d'un nouveau tarif. L'ID doit être spécifié.
        """
        self.TL.append(TARIF(ID, TAUX, DATE_CREATION))
        conn = None
        try:
            conn = sqlite3.connect("FACTURE.sqlt")
        except Error as e:
            print(e)
        cur = conn.cursor()
        cur.execute("INSERT INTO TARIF(ID, TAUX, DATE_CREATION) VALUES " +
                    "({},\'{}\',\'{}\')".format(ID, TAUX, DATE_CREATION))
        conn.commit()
        conn.close()
        self.TL.sort()

    def update(self, ID, **kwargs):
        """Update d'un client. Un ID doit être spécifié pour que ça marche """
        for i in self.TL:
            if i.ID == ID:
                conn = None
                try:
                    conn = sqlite3.connect("FACTURE.sqlt")
                except Error as e:
                    print(e)
                i.update(**kwargs)                
                cur = conn.cursor()

                sqlstr = ("UPDATE TARIF SET TAUX  = \'{}\'," +
                          "DATE_CREATION = \'{}\' " + 
                          "WHERE ID = {}")
                sqlstr = sqlstr.format(i.TAUX,
                                       i.DATE_CREATION,
                                       i.ID)
                cur.execute(sqlstr)
                conn.commit()
                conn.close()
                break
        self.TL.sort()

    def delete(self, ID):
        for i,v in enumerate(self.TL):            
            if v.ID == ID:
                self.TL.pop(i)                
                conn = None
                try:
                    conn = sqlite3.connect("FACTURE.sqlt")
                except Error as e:
                    print(e)
                cur = conn.cursor()
                cur.execute("DELETE FROM TARIF WHERE ID = {}".format(ID))
                conn.commit()
                conn.close()
                                    
    def print(self):
        """Affichage de la liste de client dans la console"""
        for i, r in enumerate(self.TL):
            r.print()

    def max_id(self):
        """ Trouver le numéro d'identité"""
        max = 0 
        for i in self.TL:
            if max < i.ID:
                max = i.ID
        return(max)
                            
if __name__ == "__main__":
    TL1 = TARIF_LIST()
    TL1.print()

