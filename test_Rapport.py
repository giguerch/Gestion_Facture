import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

CON = sqlite3.Connection(("C:/Users/gigc2/Dropbox/PERSONNEL/Contrat/" 
                    "Factures/Facture_Python/FACTURE.sqlt"))

REQ1 = """
SELECT A.ID, 
       (SELECT SUM(NB_HEURES) FROM FACTURE_ACTIVITE WHERE FACTURE_ACTIVITE.ID_FACTURE = A.ID) as HR,
       TAUX, 
       A.DATE
FROM FACTURE as A,  TARIF
WHERE ID_STATUT = 2 AND
      A.ID_TARIF = TARIF.ID;
"""
      
FAC_df = pd.read_sql(REQ1, CON)

FAC_df.head()


FAC_df["YEAR"] = FAC_df.DATE.str[:4].astype(np.int64)
FAC_df["YR"] = FAC_df.DATE.str[:4].astype(np.int64)
FAC_df['MONTANT'] = FAC_df.HR * FAC_df.TAUX
FAC_df.head()

FAC_df_GB = FAC_df[['YEAR','MONTANT']].groupby("YEAR").sum().reset_index()

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

scaler = StandardScaler()
scaler.fit(FAC_df_GB[['YEAR']])
X_scale = scaler.transform(FAC_df_GB[['YEAR']])
X_train = pd.DataFrame()
X_train['X'] = X_scale.reshape([7])
X_train['X2'] = X_scale.reshape([7])**2

fit1 = LinearRegression().fit(X = X_train, y = FAC_df_GB.MONTANT)
FAC_df_GB['MONTANT_FIT'] = fit1.predict(X_train)


### Graphique du montant (par année).

plt.style.use('seaborn-whitegrid')
fig1 = plt.figure()
fig1.set_size_inches(w = 10, h = 5)
ax = plt.axes()
plt.plot(FAC_df_GB.YEAR, FAC_df_GB.MONTANT, linewidth = 4)
plt.plot(FAC_df_GB.YEAR, FAC_df_GB.MONTANT_FIT, 
         linewidth = 4, color = "red", linestyle= "--")
plt.xlabel("year", size=12)
plt.ylabel("Montant", size = 12)
plt.ylim((0, 20000))
path1 = ("c:/Users/gigc2/Dropbox/PERSONNEL/Contrat/"
         "Factures/Facture_Python/Fig.png")
plt.savefig(path1, dpi = 400)
