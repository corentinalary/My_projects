########################## Imports ###########################
from BruitJetonQuiTombe import *
from YmaxGraphique import *
from PositionCentreHautColonne import *
from jouer_tour_graphique import *

######################## Définition ##########################

def joueTourComplet(nb_joueur,damier,colonne_choisie,nbPionsJoueur):

    """ fonction joue un tour complet d'un joueur i.e qui place le jeton du joueur dans la colonne qu'il a selectionné sur le damier dans la fenetre de jeu  , qui prend baisse de 1 le nombre de Pions à jouer du joueur et qui lance un bruit de jeton qui tombe.
    Cette fonction retourne les coordonnées x0,y0 de la case la plus haute de la colone selectionné, la liste dernier coup qui correspond à la colonne et la ligne ou est placé le jeton dans le damier de la console.
    Elle retourne également ymaxGraphique i.e la coordonnée y dans la fenetre de jeu ou le jeton est placé ainsi que nbPionsjoueur i.e le nouveau nombre de pions à jouer du joueur.

    Paramètres :
        - nb_joueur vaut nb_joueur1 si c'est le joueur 1 qui joue et nb_joueur2 si c'est le joueur 2 qui joue

        - damier qui correspond au damier dans la console que l'on étudie

        - colonne_choisie qui correspond à la colonne dans le damier étudié qui à été choisie par le joueur

        - nbPionsJoueur corresponds à nbPionsJoueur1 si c'est le joueur 1 qui joue et nbPionsJoueur2 si c'est le joueur 2 qui joue i.e c'est le nombre de pions restant à jouer pour le joueur qui joue """


    dernierCoup=jouer_tour_graphique(nb_joueur,damier,colonne_choisie)
    nbPionsJoueur+=-1
    BruitJetonQuiTombe()

    ymax=dernierCoup[1]
    ymaxGraphique = YmaxGraphique(ymax)

    x0,y0=PositionCentreHautColonne(colonne_choisie)

    return x0,y0, dernierCoup, ymaxGraphique,nbPionsJoueur
