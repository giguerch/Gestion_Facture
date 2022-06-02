### -*-       Coding: utf-8         -*-

### Interface pour gérer les clients.

##############################
## Base de données.         ##
##                          ##
##  - CLIENT                ##
##    + [ID]                ##
##    + [NOM_CLIENT]        ##
##    + [ID_ADRESSE]        ##
##                          ##
##############################

import sqlite3

class CLIENT:
    """Sert à creer un client individuel"""
    
    def __init__(self, ID = '', TITRE_CLIENT = '', PRENOM_CLIENT = '',
                 NOM_CLIENT = '', ID_ADRESSE = ''):
        """
           Initialise les attributs. Certains (ou tous les) attributs 
           peuvent être nuls ('')
        """
        self.ID            = ID
        self.TITRE_CLIENT  = TITRE_CLIENT 
        self.PRENOM_CLIENT = PRENOM_CLIENT
        self.NOM_CLIENT    = NOM_CLIENT
        self.ID_ADRESSE    = ID_ADRESSE

    def from_id(self, ID):
        if ID != None:
            conn = None
            try:
                conn = sqlite3.connect("FACTURE.sqlt")
            except Error as e:
                print(e)
            cur = conn.cursor()
            cur.execute("SELECT * FROM CLIENT WHERE ID = {}".format(ID))
            rows = cur.fetchall()
            self.ID            = ID
            self.TITRE_CLIENT  = rows[0][1]
            self.PRENOM_CLIENT = rows[0][2]
            self.NOM_CLIENT    = rows[0][3]
            self.ID_ADRESSE    = rows[0][4]

    def update(self, **kwargs):
        """You can update one or more of the 5 attributes of clients"""
        for key, value in kwargs.items():
            if "ID" == key:
                self.ID = value
            elif "TITRE_CLIENT" == key:
                self.TITRE_CLIENT = value
            elif "PRENOM_CLIENT" == key:
                self.PRENOM_CLIENT = value
            elif "NOM_CLIENT" == key:
                self.NOM_CLIENT = value
            elif "ID_ADRESSE" == key:
                self.ID_ADRESSE = value
        
    def print(self):
        """Affiche les valeurs du Client """
        print("{}, {} {} {}, {}".format(self.ID, self.TITRE_CLIENT,
                                        self.PRENOM_CLIENT, self.NOM_CLIENT,
                                        self.ID_ADRESSE))

    def __lt__(self, other):
        """ Fonction pour ordonner la liste de client par ordre alphabétique"""
        left  = str(self.NOM_CLIENT) + str(self.PRENOM_CLIENT)
        right = str(other.NOM_CLIENT) + str(other.PRENOM_CLIENT)
        return left < right


class CLIENT_LIST:
    """Liste de client dans la BD"""
    
    def __init__(self):
        """Initialise la liste de Client en allant chercher dans la BD"""
        self.CL = list()
        self.CLF = list()
        conn = None
        try:
            conn = sqlite3.connect("FACTURE.sqlt")
        except Error as e:
            print(e)
        cur = conn.cursor()
        cur.execute("SELECT * FROM CLIENT")
        rows = cur.fetchall()
        for row in rows:
            row = list(row)
            for i,r in enumerate(row, start = 0):
                if r == None:
                    row[i] = ''
            self.CL.append(CLIENT(row[0], row[1], row[2], row[3], row[4]))
            self.CLF.append(True)
        for i,j in enumerate(self.CLF):
            self.CLF[i] = True            
        self.CL.sort()
        conn.close()
        
    def add(self, ID, TITRE_CLIENT = '', PRENOM_CLIENT = '',
            NOM_CLIENT = '', ID_ADRESSE = ''):
        """Ajout d'un nouveau client. L'ID doit être spécifié.
        """
        self.CL.append(CLIENT(ID, TITRE_CLIENT, PRENOM_CLIENT,
                              NOM_CLIENT, ID_ADRESSE))
        self.CLF.append(True)
        for i, v in enumerate(self.CLF):
            self.CLF[i] = True
        conn = None
        try:
            conn = sqlite3.connect("FACTURE.sqlt")
        except Error as e:
            print(e)
        cur = conn.cursor()
        if ID_ADRESSE == '':
            cur.execute("INSERT INTO CLIENT(ID, TITRE_CLIENT, PRENOM_CLIENT," +
                        " NOM_CLIENT) VALUES " +
                        "({},\'{}\',\'{}\',\'{}\')".format(ID,
                                                           TITRE_CLIENT,
                                                           PRENOM_CLIENT,
                                                           NOM_CLIENT))
            conn.commit()
        else:
            cur.execute("INSERT INTO CLIENT(ID, TITRE_CLIENT, PRENOM_CLIENT," +
                        " NOM_CLIENT, ID_ADRESSE) VALUES " +
                        "({},\'{}\',\'{}\',\'{}\',{})".format(ID,
                                                              TITRE_CLIENT,
                                                              PRENOM_CLIENT,
                                                              NOM_CLIENT,
                                                              ID_ADRESSE))
            conn.commit()
        conn.close()
        self.CL.sort()

    def update(self, ID, **kwargs):
        """Update d'un client. Un ID doit être spécifié pour que ça marche """
        for i in self.CL:
            if i.ID == ID:
                conn = None
                try:
                    conn = sqlite3.connect("FACTURE.sqlt")
                except Error as e:
                    print(e)
                i.update(**kwargs)                
                cur = conn.cursor()
                if i.ID_ADRESSE != '':
                    sqlstr = ("UPDATE CLIENT SET TITRE_CLIENT  = \'{}\'," +
                              "PRENOM_CLIENT = \'{}\'," +
                              "NOM_CLIENT    = \'{}\',"
                              "ID_ADRESSE    = {} " +
                              "WHERE ID = {}")
                    sqlstr = sqlstr.format(i.TITRE_CLIENT,
                                           i.PRENOM_CLIENT,
                                           i.NOM_CLIENT,
                                           i.ID_ADRESSE,
                                           i.ID)
                    cur.execute(sqlstr)
                else:
                    sqlstr = ("UPDATE CLIENT SET TITRE_CLIENT  = \'{}\'," +
                              "PRENOM_CLIENT = \'{}\'," +
                              "NOM_CLIENT    = \'{}\' "
                              "WHERE ID = {}")
                    sqlstr = sqlstr.format(i.TITRE_CLIENT,
                                           i.PRENOM_CLIENT,
                                           i.NOM_CLIENT,
                                           i.ID)
                    cur.execute(sqlstr)
                conn.commit()
                conn.close()
        self.CL.sort()

    def delete(self, ID):
        for i,v in enumerate(self.CL):            
            if v.ID == ID:
                self.CL.pop(i)                
                self.CLF.pop(i)
                conn = None
                try:
                    conn = sqlite3.connect("FACTURE.sqlt")
                except Error as e:
                    print(e)
                cur = conn.cursor()
                cur.execute("DELETE FROM CLIENT WHERE ID = {}".format(ID))
                conn.commit()
                conn.close()
                                    
    def print(self):
        """Affichage de la liste de client dans la console"""
        for i, r in enumerate(self.CL):
            if self.CLF[i]:
                r.print()

    def max_id(self):
        """ Trouver le numéro d'identité"""
        max = 0 
        for i in self.CL:
            if max < i.ID:
                max = i.ID
        return(max)
                       
    def filter(self, filter):
        """ Filter les participants """
        max = 0
        for i, row in enumerate(self.CL):
            str_row = "{} {} {}".format(row.TITRE_CLIENT, row.PRENOM_CLIENT, row.NOM_CLIENT)
            if (str_row.lower().find(filter.lower()) == -1):
                self.CLF[i] = False
            else:
                self.CLF[i] = True
                

if __name__ == "__main__":
    CL1 = CLIENT_LIST()
    CL1.print()
    CL1.filter("lupien")
    print("\n")
    CL1.print()
    CL1.filter("")
    print("\n")
    CL1.print()

    
