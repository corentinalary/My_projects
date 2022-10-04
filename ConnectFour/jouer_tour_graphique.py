############################### Imports ############################

from colonne_valide import *
from placer_pion import *

############################## Définition ##########################

def jouer_tour_graphique(numero_joueur,damier,colonne_choisie):

    """ fonction qui ajoute le pion du joueur numero_joueur dans la colonne colonne_choisie seulement si celle-ci est valide. Enfin cette fonction retourne la liste dernierCoup qui correspond à [colonne_choisie, ligne du dépôt du jeton].

    Paramètres :
        - numero_joueur correspond au numéro du joueur qui veut déposer un pion i.e 1 si c'est le joueur 1 qui dépose un pion et 2 si c'est le joueur 2 qui dépose un pion

        - colonne_choisie correspond à la colonne ou le joueur veut déposer un pion, c'est donc un entier compris entre 0 et le nombre de colonnes du damier -1

        - damier correspond au damier que l'on étudie i.e une liste composée de listes correspondant à des colonnes avec à l'intérieur des lignes"""

    colonne=colonne_valide(colonne_choisie,damier)

    if colonne == True :
        dernierCoup = placer_pion(colonne_choisie,numero_joueur,damier)

        return dernierCoup
