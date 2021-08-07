############################# Imports ###########################

from placer_pion import *
from colonne_valide import *
from damier import *

########################### Définition ##########################

def jouer_tour(numero_joueur,damier):

        """ fonction qui demande d'abord au joueur numero_joueur de choisir une colonne. Tant que celle-ci n'est pas valide répète la demande. Ensuite la fonction place le pion dans la colonne choisie par le joueur et au sein du damier spécifié. Enfin elle retourne la liste dernierCoup qui vaut [colonne choisie, ligne de dépôt du jeton]

        Paramètres :
                - damier correspond au damier que l'on étudie i.e une liste composée de listes correspondant à des colonnes avec à l'intérieur des lignes

                - numero_joueur correspond au numéro du joueur pour lequel on dépose un pion i.e 1 si c'est le joueur 1 qui joue et 2 si c'est le joueur 2 qui joue """

        print("")
        print("""Joueur""", numero_joueur,"""c'est à vous de jouer""")

        choix_colonne = input("Joueur"+ " "+str(numero_joueur)+" "+"choisissez une colonne:")

        while len(choix_colonne)==0 or len(choix_colonne)>1:

                print("Vous n'avez pas saisi une colonne valide")

                choix_colonne = input("Joueur"+ " "+str(numero_joueur)+" "+"choisissez une colonne:")

        colonne_possibles =['0','1','2','3','4','5','6','7']

        while choix_colonne not in colonne_possibles :
                print("Vous n'avez pas saisi une colonne valide")
                choix_colonne = input("Joueur"+ " "+str(numero_joueur)+" "+"choisissez une colonne:")

        choix_colonne=int(choix_colonne)-1

        colonne=colonne_valide(choix_colonne,damier)

        while colonne == False :
            print("La colonne saisie n'est pas valide")
            choix_colonne = int(input("Joueur" + " " + str(numero_joueur) + " " + " choisissez une colonne:"))-1
            colonne=colonne_valide(choix_colonne,damier)

        dernierCoup = placer_pion(choix_colonne,numero_joueur,damier)

        return dernierCoup
