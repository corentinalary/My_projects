######################### Import #########################

from colonne_valide import *

######################## Définition ######################

def prendColonneValide(damier):

    """ fonction qui analyse le damier et retourne les colonnes qui ne sont pas complètement remplis.

    Paramètre :
        - damier correspond au damier que l'on étudie i.e à une liste composée de listes correspondants à des colonnes avec à l'intérieur des lignes """

    positions_valide=[]

    for colonne in range(len(damier)):

        if colonne_valide(colonne,damier)==True:

            positions_valide.append(colonne)

    return positions_valide
