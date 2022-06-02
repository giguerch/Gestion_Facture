### -*-       Coding: utf-8         -*-


### Interface pour gérer les adresses.

##############################
## Base de données.         ##
##                          ##
##  - ADRESSE               ##
##    + [ID]                ##
##    + [NOM]               ##
##    + [LIEU1]             ##
##    + [LIEU2]             ##
##    + [ADRESSE]           ##
##    + [VILLE]             ##
##    + [PROVINCE]          ##
##    + [CP]                ##
##                          ##
##############################


import sqlite3

class ADRESSE:
    """Sert à creer une adresse individuelle"""
    
    def __init__(self,
                 ID = 0,      NOM = '',   LIEU1 = '',    LIEU2 = '',
                 ADRESSE = '', VILLE = '', PROVINCE = '', CP = ''   ):
        """
           Initialise les attributs. Certains (ou tous les) attributs 
           peuvent être nuls ('')
        """
        self.ID       = ID
        self.NOM      = NOM
        self.LIEU1    = LIEU1
        self.LIEU2    = LIEU2
        self.ADRESSE  = ADRESSE
        self.VILLE    = VILLE
        self.PROVINCE = PROVINCE
        self.CP       = CP

    def from_id(self, ID):
        if ID != None:
            conn = None
            try:
                conn = sqlite3.connect("FACTURE.sqlt")
            except Error as e:
                print(e)
            cur = conn.cursor()
            cur.execute("SELECT * FROM ADRESSE WHERE ID = {}".format(ID))
            rows = cur.fetchall()
            self.ID       = ID
            self.NOM      = rows[0][1]
            self.LIEU1    = rows[0][2]
            self.LIEU2    = rows[0][3]
            self.ADRESSE  = rows[0][4]
            self.VILLE    = rows[0][5]
            self.PROVINCE = rows[0][6]
            self.CP       = rows[0][7]            
            conn.close()
        
    def update(self, sqlupdate = False, **kwargs):
        """You can update one or more of the 5 attributes of clients"""        
        for key, value in kwargs.items():
            if "ID" == key:
                self.ID = value
            elif "NOM" == key:
                self.NOM = value
            elif "LIEU1" == key:
                self.LIEU1 = value
            elif "LIEU2" == key:
                self.LIEU2 = value
            elif "ADRESSE" == key:
                self.ADRESSE = value
            elif "VILLE" == key:
                self.VILLE = value
            elif "PROVINCE" == key:
                self.PROVINCE = value
            elif "CP" == key:
                self.CP = value
        if sqlupdate:
            conn = None
            try:
                conn = sqlite3.connect("FACTURE.sqlt")
            except Error as e:
                print(e)
            cur = conn.cursor()
            sqlstr = ("UPDATE ADRESSE SET NOM = \'{}\'," +
                      "LIEU1     = \'{}\'," +
                      "LIEU2     = \'{}\'," +
                      "ADRESSE   = \'{}\'," +
                      "VILLE     = \'{}\'," +
                      "PROVINCE  = \'{}\'," +
                      "CP        = \'{}\'"
                      "WHERE ID = {}")
            sqlstr = sqlstr.format(self.NOM.replace("'","''"),
                                   self.LIEU1.replace("'","''"),
                                   self.LIEU2.replace("'","''"),
                                   self.ADRESSE.replace("'","''"),
                                   self.VILLE.replace("'","''"),
                                   self.PROVINCE.replace("'","''"),
                                   self.CP.replace("'","''"),
                                   self.ID)
            print(sqlstr)
            cur.execute(sqlstr)
            conn.commit()
            conn.close()
        
    def print(self):
        """Affiche les valeurs du Client """
        print(("{}:\n\t{}\n\t{}\n\t{}" +
               "\n\t{}\n\t{}\n\t{}\n\t{}").format(self.ID,
                                                  self.NOM,
                                                  self.LIEU1,
                                                  self.LIEU2,
                                                  self.ADRESSE,
                                                  self.VILLE,
                                                  self.PROVINCE,
                                                  self.CP))
        
    def __lt__(self, other):
        """ Fonction pour ordonner la liste de client par ordre alphabétique"""
        left  = str(self.NOM) 
        right = str(other.NOM)
        return left < right




class ADRESSE_LIST:
    """Liste d'adresse de la BD"""
    
    def __init__(self):
        """Initialise la liste d'adresse en allant chercher dans la BD"""
        self.CL = list()
        self.CLF = list()
        conn = None
        try:
            conn = sqlite3.connect("FACTURE.sqlt")
        except Error as e:
            print(e)
        cur = conn.cursor()
        cur.execute("SELECT * FROM ADRESSE")
        rows = cur.fetchall()
        for row in rows:
            row = list(row)
            for i,r in enumerate(row, start = 0):
                if r == None:
                    row[i] = ''
            self.CL.append(ADRESSE(row[0], row[1], row[2], row[3],
                                   row[4], row[5], row[6], row[7]))
            self.CLF.append(True)
        for i,j in enumerate(self.CLF):
            self.CLF[i] = True            
        self.CL.sort()
        conn.close()

    def add(self, ID, NOM = '', LIEU1 = '', LIEU2 = '', ADR = '',
            VILLE = '', PROVINCE = '', CP = ''):
        """
        Ajout d'un nouveau client. L'ID doit être spécifié.
        """

        self.CL.append(ADRESSE(ID, NOM, LIEU1, LIEU2,
                               ADR, VILLE, PROVINCE,
                               CP = CP))
        self.CLF.append(True)
        for i, v in enumerate(self.CLF):
            self.CLF[i] = True
        conn = None
        try:
            conn = sqlite3.connect("FACTURE.sqlt")
        except Error as e:
            print(e)
        cur = conn.cursor()
        cur.execute(("INSERT INTO ADRESSE(ID, NOM, LIEU1, LIEU2," +
                     " ADRESSE, VILLE, PROVINCE, CP) VALUES " +
                     "({},\'{}\',\'{}\',\'{}\',\'{}\',\'{}\'," +
                     "\'{}\',\'{}\')").format(ID,
                                              NOM.replace("'","''"),
                                              LIEU1.replace("'","''"),
                                              LIEU2.replace("'","''"),
                                              ADR.replace("'","''"),
                                              VILLE.replace("'","''"),
                                              PROVINCE.replace("'","''"),
                                              CP.replace("'","''")))
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
                sqlstr = ("UPDATE ADRESSE SET NOM  = \'{}\'," +
                          "LIEU1      = \'{}\'," +
                          "LIEU2      = \'{}\',"
                          "ADRESSE    = \'{}\'," +
                          "VILLE      = \'{}\'," +
                          "PROVINCE   = \'{}\'," +
                          "CP         = \'{}\' " +
                          "WHERE ID   = {}")
                sqlstr = sqlstr.format(i.NOM.replace("'","''"),
                                       i.LIEU1.replace("'","''"),
                                       i.LIEU2.replace("'","''"),
                                       i.ADRESSE.replace("'","''"),
                                       i.VILLE.replace("'","''"),
                                       i.PROVINCE.replace("'","''"),
                                       i.CP.replace("'","''"),
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
                cur.execute("DELETE FROM ADRESSE WHERE ID = {}".format(ID))
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
            if row.NOM.lower().find(filter.lower()) == -1:
                self.CLF[i] = False
            else:
                self.CLF[i] = True


    

if __name__ == "__main__":
    AL1 = ADRESSE_LIST()
    #AL1.print()
    #AL1.delete(3)
    #AL1.add((AL1.max_id() + 1), "Département d'ophtalmologie",
    #        "Faculté de Médecine", "Université de Montréal",
    #        "C.P. 6128, Succ. Centre-Ville", "Montréal",
    #        "Québec", "H3C3J7")
    #AL1.print()
    #AL1.update(2, ADRESSE = "5415, boul. l'Assomption", VILLE = "Montréal")
    #AL1.update(1, LIEU1 = "Centre de recherche de l'institut universitaire en santé mentale de Montréal", LIEU2 = "Pavillon Fernand-Séguin", ADRESSE = "7331, rue Hochelaga", VILLE = "Montréal")
    #AL1.filter("OPHT")
    AL1.filter("Mai")
    AL1.print()

    
