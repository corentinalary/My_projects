############## Définition ###########################

def colonne_Clique(X,Y):

    """ fonction qui prend les coordonnées du clique du joueur dans une des colonnes dans la fenetre de jeu en coordonnees du damier de la console ou qui retourne l'infini si le joueur a cliqué ailleurs que dans une colonne
    Paramètres :
        X,Y qui correspondent aux coordonnées du clique dans l'interface graphique """

    if X> 365 and X<455 and Y>45 and Y<770:
        choix_colonne=0
        return choix_colonne

    if X> 480 and X<590 and Y>45 and Y<770:
        choix_colonne=1
        return choix_colonne

    if X> 615 and X<705 and Y>45 and Y<770:
        choix_colonne=2
        return choix_colonne

    if X> 730 and X<820 and Y>45 and Y<770:
        choix_colonne=3
        return choix_colonne

    if X> 845 and X<935 and Y>45 and Y<770:
        choix_colonne=4
        return choix_colonne

    if X> 960 and X<1050 and Y>45 and Y<770:
        choix_colonne=5
        return choix_colonne

    if X> 1075 and X<1165 and Y>45 and Y<770:
        choix_colonne=6
        return choix_colonne

    else :
        return float("inf")
