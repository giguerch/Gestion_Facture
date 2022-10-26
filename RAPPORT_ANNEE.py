# -*-  Coding: utf-8 -*-

# Interface pour faire un rapport par client.
import sqlite3


class RESUME_ANNEE:
    """Sert à creer une adresse individuelle."""

    def __init__(self,
                 YEAR=0, N_FACTURE=0, MONTANT=0):
        """
           Initialise les attributs. Certains (ou tous les) attributs
           peuvent être nuls ('')
        """

        self.YEAR = YEAR
        self.N_FACTURE = N_FACTURE
        self.MONTANT = MONTANT

    def update(self, **kwargs):
        """You can update one or more of the 5 attributes of clients"""
        for key, value in kwargs.items():
            if "NOM" == key:
                self.NOM = value
            elif "N_FACTURE" == key:
                self.N_FACTURE = value
            elif "MONTANT" == key:
                self.MONTANT = value

    def print(self):
        """Affiche les valeurs du Client """
        print(("{}:\n\t{} factures" +
               "\n\tMontant total: {}$").format(self.YEAR,
                                                self.N_FACTURE,
                                                self.MONTANT))

    def __lt__(self, other):
        """ Fonction pour ordonner la liste de client par ordre de montant"""
        left = self.YEAR
        right = other.YEAR
        return left < right


class RESUME_ANNEE_LIST:
    """Liste d'adresse de la BD"""

    def __init__(self):
        """Initialise la liste d'adresse en allant chercher dans la BD."""
        self.RAL = list()
        conn = None
        try:
            conn = sqlite3.connect("FACTURE.sqlt")
        except sqlite3.Error as e:
            print(e)
        cur = conn.cursor()


        
        cur.execute("""SELECT strftime('%Y', F.DATE) AS Day,
                              COUNT() as N_FACTURE,
                              (SELECT SUM(NB_HEURES*TAUX)
                               FROM FACTURE_ACTIVITE, FACTURE, TARIF
                               WHERE FACTURE_ACTIVITE.ID_FACTURE = FACTURE.ID AND
                               FACTURE.ID = FACTURE_ACTIVITE.ID_FACTURE AND
                               FACTURE.ID_TARIF = TARIF.ID AND
                               strftime('%Y', FACTURE.DATE) = strftime('%Y', F.DATE)
                               GROUP BY strftime('%Y', FACTURE.DATE)) AS MONTANT
                       FROM FACTURE as F
                       GROUP BY Day;
        """)
        rows = cur.fetchall()
        for row in rows:
            row = list(row)
            for i, r in enumerate(row, start=0):
                if r is None:
                    row[i] = ''
            self.RAL.append(RESUME_ANNEE(row[0], row[1], row[2]))
        self.RAL.sort(reverse=True)
        conn.close()

    def add(self, NOM='', N_FACTURE=0, MIN_YEAR='',
            MAX_YEAR='', MONTANT=0):
        """
        Ajout d'un nouveau client. L'ID doit être spécifié.
        """

        self.RAL.append(RESUME_ANNEE(NOM, N_FACTURE, MIN_YEAR,
                                      MAX_YEAR, MONTANT))
        self.RAL.sort(reverse=True)

    def update(self, ID, **kwargs):
        """Update d'un client. Un ID doit être spécifié pour que ça marche """
        for i in self.RAL:
            if i.ID == ID:
                i.update(**kwargs)
                break
        self.RAL.sort(reverse=True)

    def delete(self, ID):
        for i, v in enumerate(self.RAL):
            if v.ID == ID:
                self.RAL.pop(i)
                break

    def print(self):
        """Affichage de la liste de client dans la console"""
        for i, r in enumerate(self.RAL):
            r.print()


if __name__ == "__main__":
    test = RESUME_ANNEE_LIST()
