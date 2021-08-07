####################### Import ####################
from pions_successifs_direction import *

###################### Définition ##################

def victoire (damier,dernierCoup, numJoueur, nbPionsSuccessifs ):

    """ fonction qui regarde à partir de la position du dernier pion joué dans toutes les directions le nombre de pions successifs portant le numéro du joueur spécifié.
    Si dans une ou plusieurs directions il y au moins nbPionsSuccessifs nombre de pions alors la fonction retourne True.
    Dans les autres cas la fonction retourne False. Cette fonction determine donc bien si le coup qui vient d'être joué à mener à la victoire (True) ou non (False).

    Paramètres :
        - damier correspond au damier dans la console que l'on étudie

        - dernierCoup correspond à [colonne du dernier coup joué, ligne du dernier coup joué]

        - numJoueur correspond au numéro du joueur pour lequel on regarde i.e 1 si on regarde pour le joueur 1 et 2 si on regarde pour le joueur 2

        - nbPionsSuccessifs correspond au nombre de pions alignés qu'il faut pour qu'il y ait une victoire """

    directions_possibles1=[ [-1,1], [1,-1] ]
    directions_possibles2=[ [1,1], [-1,-1] ]
    directions_possibles3=[ [-1,0], [1,0] ]
    directions_possibles4=[0,-1]

    compteur =0

    if damier[dernierCoup[0]][dernierCoup[1]]==numJoueur :
        compteur+=1

    for direction in directions_possibles1 :
        compteur+=pions_successifs_direction(damier, dernierCoup[0],dernierCoup[1],direction[0],direction[1],numJoueur)

    if compteur>=nbPionsSuccessifs:
        return True

    else:
        compteur =0

        if damier[dernierCoup[0]][dernierCoup[1]]==numJoueur :
            compteur+=1

        for direction in directions_possibles2 :
            compteur+=pions_successifs_direction(damier, dernierCoup[0],dernierCoup[1],direction[0],direction[1],numJoueur)

        if compteur>=nbPionsSuccessifs:
            return True

        else :
            compteur =0

            if damier[dernierCoup[0]][dernierCoup[1]]==numJoueur :
                compteur+=1

            for direction in directions_possibles3 :
                compteur+=pions_successifs_direction(damier,dernierCoup[0],dernierCoup[1],direction[0],direction[1],numJoueur)

            if compteur>=nbPionsSuccessifs:
                return True

            else:

                compteur=pions_successifs_direction(damier,dernierCoup[0],dernierCoup[1],directions_possibles4[0],directions_possibles4[1],numJoueur)


                if damier[dernierCoup[0]][dernierCoup[1]]==numJoueur :
                    compteur+=1

                if compteur>=nbPionsSuccessifs:
                    return True

                else:
                    return False
