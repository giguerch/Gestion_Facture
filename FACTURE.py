### -*-  coding: utf-8 -*-
### Auteur: Charles-Édouard Giguère 

### Classe pour gérer un objet de type FACTURE. 

##############################
## Base de données.         ##
##                          ##
##  - FACTURE               ##
##    + [ID]                ##
##    + [PERIODE_MIN]       ##
##    + [PERIODE_MAX]       ##
##    + [DATE]              ##
##    + [ID_CLIENT]         ##
##    + [ID_STATUT]         ##
##    + [ID_TARIF]          ##
##                          ##
##############################

import sqlite3

class FACTURE:
    """ Sert à créer un client individuel"""
    def __init__(self, ID = '', PROJET = '', PERIODE_MIN_MS = '',
                 PERIODE_MIN_YR = '', PERIODE_MAX_MS = '', PERIODE_MAX_YR = '',
                 DATE = '', ID_CLIENT = '', ID_STATUT = '', ID_TARIF = '',
                 FACTURE_PDF = ''):
        self.ID             = ID
        self.PROJET         = PROJET
        self.PERIODE_MIN_MS = PERIODE_MIN_MS
        self.PERIODE_MIN_YR = PERIODE_MIN_YR
        self.PERIODE_MAX_MS = PERIODE_MAX_MS
        self.PERIODE_MAX_YR = PERIODE_MAX_YR
        self.DATE           = DATE
        self.ID_CLIENT      = ID_CLIENT
        self.ID_STATUT      = ID_STATUT
        self.ID_TARIF       = ID_TARIF
        self.FACTURE_PDF    = FACTURE_PDF
        

    def from_id(self, ID):
        if ID != None:
            conn = None
            try:
                conn = sqlite3.connect("FACTURE.sqlt")
            except Error as e:
                print(e)
            cur = conn.cursor()
            cur.execute("SELECT * FROM FACTURE WHERE ID = {}".format(ID))
            rows = cur.fetchall()
            #print(rows)
            self.ID             = ID
            self.PROJET         = rows[0][1]
            self.PERIODE_MIN_MS = rows[0][2]
            self.PERIODE_MIN_YR = rows[0][3]
            self.PERIODE_MAX_MS = rows[0][4]
            self.PERIODE_MAX_YR = rows[0][5]
            self.DATE           = rows[0][6]
            self.ID_CLIENT      = rows[0][7]
            self.ID_STATUT      = rows[0][8]
            self.ID_TARIF       = rows[0][9]
            self.FACTURE_PDF    = rows[0][10]
            
    def update(self, sqlupdate = False, **kwargs):
        """You can update one or more of the 9 attributes of FACTURE"""
        for key, Value in kwargs.items():
            if "ID" == key:
                self.ID = Value
            if "PROJET" == key:
                self.PROJET = Value
            if "PERIODE_MIN_MS" == key:
                self.PERIODE_MIN_MS = Value
            if "PERIODE_MIN_YR" == key:
                self.PERIODE_MIN_YR = Value
            if "PERIODE_MAX_MS" == key:
                self.PERIODE_MAX_MS = Value
            if "PERIODE_MAX_YR" == key:
                self.PERIODE_MAX_YR = Value
            if "DATE" == key:
                self.DATE = Value
            if "ID_CLIENT" == key:
                self.ID_CLIENT = Value
            if "ID_STATUT" == key:
                self.ID_STATUT = Value
            if "ID_TARIF" == key:
                self.ID_TARIF = Value
            if "FACTURE_PDF" == key:
                self.FACTURE_PDF = Value

    def print(self):
        if self.PERIODE_MAX_MS != None:
            print(("#{}:\n\t{}\n\tPériode {}/{} - {}/{}" +
                   "\n\tDATE: {}\n\tCLIENT: {} STATUT: {} TARIF: {}" +
                   "\n\tPDF CRÉÉ: {}"
            ).format(self.ID,
                     self.PROJET,
                     self.PERIODE_MIN_MS,
                     self.PERIODE_MIN_YR,
                     self.PERIODE_MAX_MS,
                     self.PERIODE_MAX_YR,
                     self.DATE,
                     self.ID_CLIENT,
                     self.ID_STATUT,
                     self.ID_TARIF,
                     self.FACTURE_PDF))
        else:
            print(("#{}:\n\t{}\n\tPériode {}/{}" +
                   "\n\tDATE: {}\n\tCLIENT: {} STATUT: {} TARIF: {}" +
                   "\n\tPDF CRÉÉ: {}"
            ).format(self.ID,
                     self.PROJET,
                     self.PERIODE_MIN_MS,
                     self.PERIODE_MIN_YR,
                     self.DATE,
                     self.ID_CLIENT,
                     self.ID_STATUT,
                     self.ID_TARIF,
                     self.FACTURE_PDF))

    def __lt__(self, other):
        """ Fonction pour ordonner la liste de client par ordre alphabétique"""
        left  = str(self.ID) 
        right = str(other.ID)
        return left < right


class FACTURE_LIST:
    """Liste d'adresse de la BD"""
    
    def __init__(self):
        """Initialise la liste d'adresse en allant chercher dans la BD"""
        self.FL = list()
        self.FLF = list()
        conn = None
        try:
            conn = sqlite3.connect("FACTURE.sqlt")
        except Error as e:
            print(e)
        cur = conn.cursor()
        cur.execute("SELECT * FROM FACTURE ORDER BY DATE DESC")
        rows = cur.fetchall()
        for row in rows:
            row = list(row)
            for i,r in enumerate(row, start = 0):
                if r == None:
                    row[i] = ''
            self.FL.append(FACTURE(row[0], row[1], row[2], row[3],
                                   row[4], row[5], row[6], row[7],
                                   row[8], row[9], row[10]))
            self.FLF.append(True)
        for i,j in enumerate(self.FLF):
            self.FLF[i] = True            
        self.FL.sort(reverse = True)
        conn.close()

    def add(self, ID, PROJET = '', PERIODE_MIN_MS = '',
            PERIODE_MIN_YR = '', PERIODE_MAX_MS = '', PERIODE_MAX_YR = '',
            DATE = '', ID_CLIENT = '', ID_STATUT = '', ID_TARIF = '',
            FACTURE_PDF = ''):
        """
        Ajout d'une nouvelle facture. L'ID doit être spécifié.
        """

        self.FL.append(FACTURE(ID, PROJET, PERIODE_MIN_MS, PERIODE_MIN_YR,
                               PERIODE_MAX_MS, PERIODE_MAX_YR, DATE, ID_CLIENT,
                               ID_STATUT, ID_TARIF, FACTURE_PDF))
        self.FLF.append(True)
        for i, v in enumerate(self.FLF):
            self.FLF[i] = True
        conn = None
        try:
            conn = sqlite3.connect("FACTURE.sqlt")
        except Error as e:
            print(e)
        cur = conn.cursor()
        if PERIODE_MAX_MS == '':
            PERIODE_MAX_MS = "Null"
        if PERIODE_MAX_YR == '':
            PERIODE_MAX_YR = "Null"
        sqlstr = ("INSERT INTO FACTURE(ID, PROJET, PERIODE_MIN_MS, " +
                  "PERIODE_MIN_YR, PERIODE_MAX_MS, PERIODE_MAX_YR, " +
                  "DATE, ID_CLIENT, ID_STATUT, ID_TARIF, FACTURE_PDF) VALUES " +
                  " ({}, \'{}\', {}, {}, {}, {}," +
                  "\'{}\', {}, {}, {}, {})").format(ID,
                                                    PROJET.replace("'", "''"),
                                                    PERIODE_MIN_MS,
                                                    PERIODE_MIN_YR,
                                                    PERIODE_MAX_MS,
                                                    PERIODE_MAX_YR,
                                                    DATE, ID_CLIENT,
                                                    ID_STATUT, ID_TARIF,
                                                    FACTURE_PDF)
        cur.execute(sqlstr)
        conn.commit()
        conn.close()
        self.FL.sort(reverse = True)
    
    def update(self, ID, **kwargs):
        """Update d'un client. Un ID doit être spécifié pour que ça marche """
        for i in self.FL:
            if i.ID == ID:
                conn = None
                try:
                    conn = sqlite3.connect("FACTURE.sqlt")
                except Error as e:
                    print(e)
                i.update(**kwargs)
                cur = conn.cursor()
                sqlstr = ("UPDATE FACTURE SET PROJET  = \'{}\'," +
                          "PERIODE_MIN_MS = {}," +
                          "PERIODE_MIN_YR = {},"
                          "PERIODE_MAX_MS = {}," +
                          "PERIODE_MAX_YR = {}," +
                          "DATE           = \'{}\'," + 
                          "ID_CLIENT      = {}," +
                          "ID_STATUT      = {},"+
                          "ID_TARIF       = {},"+
                          "FACTURE_PDF    = {} " +
                          "WHERE ID   = {}")
                sqlstr = sqlstr.format(i.PROJET.replace("'","''"),
                                       i.PERIODE_MIN_MS,
                                       i.PERIODE_MIN_YR,
                                       i.PERIODE_MAX_MS,
                                       i.PERIODE_MAX_YR,
                                       i.DATE, i.ID_CLIENT,
                                       i.ID_STATUT, i.ID_TARIF,
                                       i.FACTURE_PDF,
                                       i.ID)
                print(sqlstr)
                cur.execute(sqlstr)
                conn.commit()
                conn.close()
        self.FL.sort(reverse = True)
    
    def delete(self, ID):
        for i,v in enumerate(self.FL):            
            if v.ID == ID:
                self.FL.pop(i)                
                self.FLF.pop(i)
                conn = None
                try:
                    conn = sqlite3.connect("FACTURE.sqlt")
                except Error as e:
                    print(e)
                cur = conn.cursor()
                cur.execute("DELETE FROM FACTURE WHERE ID = {}".format(ID))
                conn.commit()
                conn.close()
    
    def print(self):
        """Affichage de la liste de client dans la console"""
        for i, r in enumerate(self.FL):
            if self.FLF[i]:
                r.print()
    
    def max_id(self):
        """ Trouver le numéro d'identité"""
        max = 0 
        for i in self.FL:
            if max < i.ID:
                max = i.ID
        return(max)
                       
    def filter(self, filter):
        """ Filter les participants """
        max = 0
        for i, row in enumerate(self.FL):
            if row.PROJET.lower().find(filter.lower()) == -1:
                self.FLF[i] = False
            else:
                self.FLF[i] = True


    
            
if __name__ == "__main__":
    ### FAC1 = FACTURE()
    ### FAC1.from_id(8739926)
    ### FAC1.print()
    FL1 = FACTURE_LIST()
    FL1.print()
    ### print(FL1.max_id())
    ### FL1.filter("prof")
    ### FL1.print()
    ### FL1.filter("")
    ### FL1.print()
    ### FL1.add(8739928, 'Honoraire professionel',
    ###         6, 2014, '', '', '2014-06-25', 6, 2, 1, 0)
