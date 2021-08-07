################################ Import ############################

from prendColonneValide import *
from detectionVictoireDamier import *

############################### Définition ##########################

def noeudTerminal(damier):

    """ fonction qui retourne True si on la fonction détecte une victoire pour le joueur 1 ou une victoire pour l'IA ou encore si il n'y a plus de colonnes valide sur le damier ( i.e si il y a match nul ).
    Si aucune de ces conditions est remplie la fonction retourne False.

    Paramètres :
        - damier correspond au damier que l'on étudie i.e une liste composée de listes correspondant à des colonnes avec à l'intérieur des lignes """



    nb_joueur1=1
    nb_IA=2

    return detectionVictoireDamier(damier, nb_joueur1) or detectionVictoireDamier(damier, nb_IA) or len(prendColonneValide(damier)) == 0
