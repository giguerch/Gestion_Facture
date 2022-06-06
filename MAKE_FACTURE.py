# -*- Coding: utf-8 -*-
import jinja2
import os
from FACTURE import FACTURE
from CLIENT import CLIENT
from ADRESSE import ADRESSE
from FACTURE_ACTIVITE import FACTURE_ACTIVITE_LIST
from TARIF import TARIF_LIST
import glob
from re import split as rsplit


class FACTURE_PDF:
    """Sert à générer une facture en pdf initialisé avec le
       numéro de facture
    """

    def __init__(self, ID):
        # initialisation de l'environnement jinja2 pour latex.
        latex_jinja_env = jinja2.Environment(
           block_start_string='\\BLOCK{',
           block_end_string='}',
           variable_start_string='\\VAR{',
           variable_end_string='}',
           comment_start_string='\\#{',
           comment_end_string='}',
           line_statement_prefix='%%',
           line_comment_prefix='%#',
           trim_blocks=True,
           autoescape=False,
           loader=jinja2.FileSystemLoader(os.path.abspath('\\'))
        )

        template = latex_jinja_env.get_template(
            'c:/Charles/Contrat/Factures/' +
            'Facture_Python/Template.tex')

        F1 = FACTURE()
        F1.from_id(ID)
        C1 = CLIENT()
        C1.from_id(F1.ID_CLIENT)
        CA1 = ADRESSE()
        CA1.from_id(C1.ID_ADRESSE)
        FA1 = FACTURE_ACTIVITE_LIST()
        FA1.by_id(ID)
        total = 0
        for a in FA1.FAL:
            total = total + a.NB_HEURES
        T1 = TARIF_LIST()
        tarif = 0
        for t in T1.TL:
            if t.ID == F1.ID_TARIF:
                tarif = t.TAUX

        options = {"Name": "{}".format(ID),
                   "CLIENT": self.bloc_adresse(C1, CA1),
                   "PROJET": F1.PROJET,
                   "PERIODE": self.periode(F1),
                   "DATE": F1.DATE,
                   "ACTIVITES": self.activites(FA1),
                   "TARIF": "%.2f" % float(tarif),
                   "TOTAL": "%.2f" % float(total),
                   "TOTALTARIF": "%.2f" % (float(tarif)*float(total))}

        renderer_template = template.render(**options)
        with open("result.tex", "w", encoding='utf-8') as f:
            f.write(renderer_template)
        os.system("pdflatex {}".format("result.tex"))

        TEST = glob.glob("FACTURES/FACTURE_{}*".format(ID))
        if(len(TEST) == 1):
            TEST2 = glob.glob("FACTURES/ARCHIVES/FACTURE_{}*".format(ID))
            TEST2.sort(reverse=True)
            print(TEST2)
            if(len(TEST2) == 0):
                os.system(("mv FACTURES/FACTURE_{}.pdf "
                           "FACTURES/ARCHIVES/"
                           "FACTURE_{}_1.pdf").format(ID, ID))
            else:
                for t in TEST2:
                    TS = int(rsplit("_|[.]", t)[2])
                    os.system(("mv FACTURES/ARCHIVES/"
                               "FACTURE_{}_{}.pdf FACTURES/"
                               "ARCHIVES/FACTURE_{}_{}.pdf").format(ID, TS,
                                                                    ID, TS+1))
                os.system("mv FACTURES/FACTURE_{}.pdf "
                          "FACTURES/ARCHIVES/FACTURE_{}_1.pdf".format(ID, ID))

        os.system("cp result.pdf FACTURES/FACTURE_{}.pdf".format(ID))

    def nom_prenom(self, C):
        CLIENT = "\\tab "
        if C.TITRE_CLIENT != "":
            CLIENT = CLIENT + "{} ".format(C.TITRE_CLIENT)
        CLIENT = CLIENT + "{} {} \\\\".format(C.PRENOM_CLIENT, C.NOM_CLIENT)
        return(CLIENT)

    def adresse(self, CA):
        CLIENT_ADRESSE = "\\tab {}, \\\\".format(CA.NOM.replace("&", "\\&"))
        if CA.LIEU1 != "":
            CLIENT_ADRESSE = CLIENT_ADRESSE + \
                "\n\\tab {}, \\\\".format(CA.LIEU1)
        if CA.LIEU2 != "":
            CLIENT_ADRESSE = CLIENT_ADRESSE + \
                "\n\\tab {}, \\\\".format(CA.LIEU2)
        if CA.ADRESSE != "":
            CLIENT_ADRESSE = CLIENT_ADRESSE + \
                "\n\\tab {}, \\\\".format(CA.ADRESSE.replace("&", "\\&"))
        CLIENT_ADRESSE = CLIENT_ADRESSE + \
            "\n\\tab {}, {}, {} \\\\".format(CA.VILLE,
                                             CA.PROVINCE,
                                             CA.CP)
        return(CLIENT_ADRESSE)

    def bloc_adresse(self, C, CA):
        return(self.nom_prenom(C) + "\n" + self.adresse(CA))

    def periode(self, F):
        MOIS = ("Jan", u"Fév", u"Mar", u"Avr",
                "Mai", "Juin", "Juil", u"Août",
                "Sep", "Oct", "Nov", u"Déc")
        if F.PERIODE_MAX_MS == 0 or F.PERIODE_MAX_MS is None:
            return("{} {}".format(MOIS[F.PERIODE_MIN_MS - 1],
                                  F.PERIODE_MIN_YR))
        else:
            if F.PERIODE_MAX_YR == F.PERIODE_MIN_YR:
                return("{} - {} {}".format(MOIS[F.PERIODE_MIN_MS - 1],
                                           MOIS[F.PERIODE_MAX_MS - 1],
                                           F.PERIODE_MIN_YR))
            else:
                return("{} {} - {} {}".format(MOIS[F.PERIODE_MIN_MS - 1],
                                              F.PERIODE_MIN_YR,
                                              MOIS[F.PERIODE_MAX_MS - 1],
                                              F.PERIODE_MAX_YR))

    def activites(self, FA):
        total = 0.0
        BLOC = ""
        for a in FA.FAL:
            total = total + a.NB_HEURES
            BLOC = BLOC + "{} & {} & {} heures\\\\\n".format(a.DATE,
                                                             a.DESCRIPTION,
                                                             a.NB_HEURES)
        BLOC = BLOC + ("\\hline\nTotal   & & "
                       "{} heures \\\\\n\\hline").format(total)
        return(BLOC)
