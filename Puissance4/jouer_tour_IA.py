###################### Import #########################

from placer_pion import *

##################### Définition ######################

def jouer_tour_IA(choix_colonne,damier) :

    """ fonction qui place le jeton dans la colonne que l'IA choisit, affiche cette colonne avec un message  et retourne la liste dernierCoup qui vaut [colonne joué, ligne de dépôt du pion]. Le tout se faisant au sein d'un damier spécifié.

    Paramètres :
        - choix_colonne correspond à la colonne que choisit l'IA, c'est donc un entier compris entre 0 et le nombre de colonne du damier -1

        - damier correspond au damier que l'on étudie i.e une liste composée de listes correspondant à des colonnes avec à l'intérieur des lignes """

    nb_IA=2

    print("")

    dernierCoup = placer_pion(choix_colonne,nb_IA,damier)

    print("")

    print("l'IA joue la colonne", dernierCoup[0]+1)

    return dernierCoup
