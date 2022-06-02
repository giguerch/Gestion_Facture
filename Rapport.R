###     -*- Coding: utf-8 -*-          ###
### Analyste: Charles-Édouard Giguère  ###
###                              .~    ###
###  _\\\\\_                    ~.~    ###
### |  ~ ~  |                 .~~.     ###
### #--O-O--#          ==||  ~~.||     ###
### |   L   |        //  ||_____||     ###
### |  \_/  |        \\  ||     ||     ###
###  \_____/           ==\\_____//     ###
##########################################

require(dplyr, quietly = TRUE, warn.conflicts = FALSE)
require(ggplot2, quietly = TRUE, warn.conflicts = FALSE)
theme_set(theme_bw() + theme(legend.position = "bottom"))
require(CUFF, quietly = TRUE, warn.conflicts = FALSE)
require(RSQLite, quietly = TRUE, warn.conflicts = FALSE) 

con <- dbConnect(SQLite(),dbname = "./FACTURE.sqlt")
res <- dbGetQuery(con, '
SELECT A.ID, 
       (SELECT SUM(NB_HEURES)
        FROM FACTURE_ACTIVITE
        WHERE FACTURE_ACTIVITE.ID_FACTURE = A.ID) as HR,
       TAUX, 
       A.DATE
FROM FACTURE as A,  TARIF
WHERE ID_STATUT = 2 AND
      A.ID_TARIF = TARIF.ID')

res$DATE

res$MONTANT <- res$TAUX * res$HR
res$YEAR <- lubridate::year(res$DATE) 


res %>%
  group_by(YEAR) %>%
  summarise(MONTANT = sum(MONTANT))  %>%
  as.data.frame


ggplot(res %>%
  group_by(YEAR) %>%
    summarise(MONTANT = sum(MONTANT)) %>%
    filter(YEAR %in% 2014:2020),
  aes(YEAR, MONTANT, group = 1)) +
  geom_line() +
  geom_smooth(se = FALSE)

tail(res)

