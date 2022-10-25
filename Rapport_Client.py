# -*-  Coding: utf-8 -*-

# Interface pour faire un rapport par client.
import sqlite3


class RESUME_CLIENT:
    """Sert à creer une adresse individuelle."""

    def __init__(self,
                 NOM='', N_FACTURE=0, MIN_YEAR='',
                 MAX_YEAR='', MONTANT=0):
        """
           Initialise les attributs. Certains (ou tous les) attributs
           peuvent être nuls ('')
        """

        self.NOM = NOM
        self.N_FACTURE = N_FACTURE
        self.MIN_YEAR = MIN_YEAR
        self.MAX_YEAR = MAX_YEAR
        self.MONTANT = MONTANT

    def update(self, **kwargs):
        """You can update one or more of the 5 attributes of clients"""
        for key, value in kwargs.items():
            if "NOM" == key:
                self.NOM = value
            elif "N_FACTURE" == key:
                self.N_FACTURE = value
            elif "MIN_YEAR" == key:
                self.MIN_YEAR = value
            elif "MAX_YEAR" == key:
                self.MAX_YEAR = value
            elif "MONTANT" == key:
                self.MONTANT = value

    def print(self):
        """Affiche les valeurs du Client """
        print(("{}:\n\t{} factures de {} à {}" +
               "\n\tMontant total: {}$").format(self.NOM,
                                                self.N_FACTURE,
                                                self.MIN_YEAR,
                                                self.MAX_YEAR,
                                                self.MONTANT))

    def __lt__(self, other):
        """ Fonction pour ordonner la liste de client par ordre de montant"""
        left = self.MONTANT
        right = other.MONTANT
        return left < right


class RESUME_CLIENT_LIST:
    """Liste d'adresse de la BD"""

    def __init__(self):
        """Initialise la liste d'adresse en allant chercher dans la BD."""
        self.RCL = list()
        conn = None
        try:
            conn = sqlite3.connect("FACTURE.sqlt")
        except sqlite3.Error as e:
            print(e)
        cur = conn.cursor()
        cur.execute("""SELECT TITRE_CLIENT ||
                            IIF(TITRE_CLIENT = '', '', ' ') ||
                            PRENOM_CLIENT || IIF(NOM_CLIENT = '', '',' ') ||
                            NOM_CLIENT,
                            COUNT() as N_FACTURE,
                            MIN(PERIODE_MIN_YR) as MIN_YEAR,
                            MAX(IIF(PERIODE_MAX_YR is Null, PERIODE_MIN_YR,
                                   PERIODE_MAX_YR)) as MAX_YEAR,
                            (SELECT SUM(NB_HEURES*TAUX)
                             FROM FACTURE_ACTIVITE, FACTURE, TARIF
                             WHERE FACTURE_ACTIVITE.ID_FACTURE = FACTURE.ID AND
                             FACTURE.ID = FACTURE_ACTIVITE.ID_FACTURE AND
                             FACTURE.ID_TARIF = TARIF.ID AND
                             FACTURE.ID_CLIENT = F.ID_CLIENT
                             GROUP BY ID_CLIENT) AS MONTANT
                     FROM FACTURE AS F, CLIENT AS C, TARIF AS T
                     WHERE  C.ID = F.ID_CLIENT AND
                            F.ID_TARIF = T.ID
                     GROUP BY F.ID_CLIENT
                     ORDER BY MONTANT DESC;""")
        rows = cur.fetchall()
        for row in rows:
            row = list(row)
            for i, r in enumerate(row, start=0):
                if r is None:
                    row[i] = ''
            self.RCL.append(RESUME_CLIENT(row[0], row[1], row[2], row[3], row[4]))
        self.RCL.sort(reverse=True)
        conn.close()

    def add(self, NOM='', N_FACTURE=0, MIN_YEAR='',
            MAX_YEAR='', MONTANT=0):
        """
        Ajout d'un nouveau client. L'ID doit être spécifié.
        """

        self.RCL.append(RESUME_CLIENT(NOM, N_FACTURE, MIN_YEAR,
                                      MAX_YEAR, MONTANT))
        self.RCL.sort(reverse=True)

    def update(self, ID, **kwargs):
        """Update d'un client. Un ID doit être spécifié pour que ça marche """
        for i in self.RCL:
            if i.ID == ID:
                i.update(**kwargs)
                break
        self.RCL.sort(reverse=True)

    def delete(self, ID):
        for i, v in enumerate(self.RCL):
            if v.ID == ID:
                self.RCL.pop(i)
                break

    def print(self):
        """Affichage de la liste de client dans la console"""
        for i, r in enumerate(self.RCL):
            r.print()


if __name__ == "__main__":
    test = RESUME_CLIENT_LIST()
