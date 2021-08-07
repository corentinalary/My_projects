###################### Import ###################################
from damier import *

##################### Définition ################################
def colonne_valide(choix_colonne,damier):

    """ fonction qui retourne True si la colonne spécifiée n'est pas remplie i.e si il y a des 0 dedans correspondant à des cases vides. Pour qu'elle retourne True il faut également que la colonne spécifié soit comprises entre 0 et le nombre de colonnes du damier choisi.
    Dans les autres cas cette fonction retourne False.

    Paramètres :
        - choix_colonne correspond à la colonne que l'on étudie

        - damier correspondant au damier dans la console que l'on étudie """

    if choix_colonne > len(damier) or choix_colonne<0:
        valide = False


    else :

        if damier[choix_colonne][len(damier[0])-1] !=0 :
            valide=False

        else:

            valide = True

    return valide
