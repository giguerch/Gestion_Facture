-- -*- Coding: utf-8 -*-

-- Création des tables pour le programme de facturation.  

-- Table décrivant la facture avec la période de facturation,
-- la date de facturation et l'identification du client et le
-- statut de la facture. 

CREATE TABLE IF NOT EXISTS FACTURE(
       ID             INTEGER PRIMARY KEY,
       PROJET         TEXT,
       PERIODE_MIN_MS INTEGER,
       PERIODE_MIN_YR INTEGER,
       PERIODE_MAX_MS INTEGER,
       PERIODE_MAX_YR INTEGER,
       DATE           DATE,
       ID_CLIENT      INTEGER,
       ID_STATUT      INTEGER,
       ID_TARIF       INTEGER,
       FACTURE_PDF    INTEGER
);

INSERT INTO FACTURE (ID, PROJET, PERIODE_MIN_MS, PERIODE_MIN_YR,
                     PERIODE_MAX_MS, PERIODE_MAX_YR, DATE,
		     ID_CLIENT, ID_STATUT, ID_TARIF, FACTURE_PDF)
       VALUES (8739926, 'Consultation', 02, 2014, Null, Null,
               '2014-02-15', 4, 2, 1, 0),
	      (8739927, 'Honoraire professionel', 06, 2014, Null, Null,
               '2014-06-10', 5, 2, 1, 0);

-- Table décrivant les activités associées à chaque facture.
-- Ex: Analyse statistiques 2 heures.

CREATE TABLE IF NOT EXISTS FACTURE_ACTIVITE(
       ID          INTEGER PRIMARY KEY,
       ID_FACTURE  INTEGER,
       DATE        DATE,
       DESCRIPTION TEXT,
       NB_HEURES   REAL
);


INSERT INTO FACTURE_ACTIVITE (ID, ID_FACTURE, DATE, DESCRIPTION, NB_HEURES)
       VALUES (1, 8739926, '2014-02-15', 'Préparation d''une mise en situation',
               1.0),
	      (2, 8739926, '2014-02-15', 'Consultation (problème informatique)',
               1.0),
	      (3, 8739927, '2014-06-10', 'Formation',
	       2.0),
	      (4, 8739927, '2014-06-10', 'Création de scripts pour automatiser l''installation de programmes',
	       2.0),
	      (5, 8739927, '2014-06-10', 'Installation d''un programme pour faire des entrevues téléphoniques',
	       1.5);

-- Table d'identification Statut de la facture.

CREATE TABLE IF NOT EXISTS STATUT(
       ID     INTEGER PRIMARY KEY,
       STATUT TEXT);

INSERT INTO STATUT (ID, STATUT)
       VALUES (1, 'EN ATTENTE'),
              (2, 'PAYÉ'),
	      (3, 'ANNULÉ');

-- Table d'identification des clients.
-- Titre client réfère à Dr, Dre, etc. Sinon on laisse vide.

CREATE TABLE IF NOT EXISTS CLIENT(
       ID            INTEGER PRIMARY KEY,
       TITRE_CLIENT  TEXT,
       PRENOM_CLIENT TEXT,
       NOM_CLIENT    TEXT,
       ID_ADRESSE    TEXT
);

INSERT INTO CLIENT (ID, TITRE_CLIENT, PRENOM_CLIENT, NOM_CLIENT, ID_ADRESSE)
       VALUES (1, 'Dre', 'Isabelle', 'Brunette', 2),
       	      (2, 'Dre', 'Sonia', 'Lupien', 1),
	      (3, 'Dr', 'Stéphane', 'Potvin', 4),
	      (4, '', 'Hélène', 'Beaumont', 5),
	      (5, '', 'Sandra', 'Favret', 5);

-- Adresse de facturation. La table est associé au client.
CREATE TABLE IF NOT EXISTS ADRESSE(
       ID       INTEGER PRIMARY KEY, 
       NOM      TEXT,
       LIEU1    TEXT,
       LIEU2    TEXT,
       ADRESSE  TEXT,
       VILLE    TEXT,
       PROVINCE TEXT, 
       CP       TEXT
);


INSERT INTO ADRESSE (ID, NOM, LIEU1, LIEU2, ADRESSE, VILLE, PROVINCE, CP)
       VALUES (1, 'Centre d''études sur le stress humain',
                  'Centre de recherche de l''institut universitaire en santé mentale de Montréal',	    
		  'Pavillon Fernand-Séguin', '7331, rue Hochelaga', 'Montréal', 'Québec', 'H1N-3V2'),
              (2, 'Département d''ophtalmologie', 'Centre de recherche', 'Hôpital Maisonneuve-Rosemont',
                  '5415, boul. l''Assomption', 'Montréal', 'Québec', 'H1T-2M4'),
              (3, 'Département d''ophtalmologie', 'Faculté de Médecine', 'Université de Montréal',
                  'C.P. 6128, Succ. Centre-Ville', 'Montréal', 'Québec', 'H3C-3J7'),
              (4, 'Centre de recherche', 'Institut universitaire en santé mentale de Montréal', '',
                  '7331, rue Hochelaga', 'Montréal', 'Québec', 'H1N-3V2'),
              (5, 'GRIP', 'Université de Montréal', '', '3050, Édouard-Montpetit',
	          'Montréal', 'Québec', 'H3T-1J7');

-- Table décrivant les tarifs. 
CREATE TABLE IF NOT EXISTS TARIF(
       ID      INTEGER,
       TAUX    REAL,
       DATE_CREATION DATE
);

INSERT INTO TARIF (ID, TAUX, DATE_CREATION)
       VALUES (1, 50.00, '2014-02-15'),
              (2, 75.00, '2015-10-28'),
              (3, 55.00, '2018-09-25');
	      
