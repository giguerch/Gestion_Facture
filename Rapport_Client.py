# -*-  Coding: utf-8 -*-

# Interface pour faire un rapport par client.
import sqlite3

# Variable Client_id.
CLIENT_ID = 1


conn = None
try:
    conn = sqlite3.connect("FACTURE.sqlt")
except sqlite3.Error as e:
    print(e)
cur = conn.cursor()
sqlstr = ("""
SELECT A.ID,
       (SELECT SUM(NB_HEURES) FROM FACTURE_ACTIVITE
        WHERE FACTURE_ACTIVITE.ID_FACTURE = A.ID) as HR,
       TAUX,
       A.DATE
FROM FACTURE as A,  TARIF
WHERE ID_STATUT = 2 AND
      A.ID_TARIF = TARIF.ID;
""")

print(sqlstr)
cur.execute(sqlstr)
conn.commit()
conn.close()
