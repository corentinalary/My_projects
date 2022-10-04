#!/usr/bin/env python3
#################Imports##########################

from damier import *
from colonne_valide import *
from random import *
from placer_pion import *
from jouer_tour import *
from nombre_pions import *
from pions_successifs_direction import *
from victoire import *

##########Programme########

def Puissance4Duo():

   """ fonction qui simule un Puissance 4. Dans un premier temps elle demande lequel des joueurs veut commencer et le premier tour est donc joué par le joueur choisie.
   Puis par la suite tant qu'il n'y a pas victoire ou match nul on alterne les tours entre le joueur 1 et le joueur 2.
   A chaque tour on demande au joueur quelle colonne il veut jouer et si elle est valide on place le jeton dans la colonne qu'il a choisi.
   Ensuite on affiche le damier et on regarde si il y a victoire ou match nul.
   A la fin d'une partie la fonction demande si les joueurs veulent recommencer une partie et dans ce cas relance une partie sinon s'arrête. """

   damier=genereDamier(6,7)

   afficheDamier(damier)

   nb_joueur1=1
   nb_joueur2=2

   print("")
   parite_joueur1=int(input("Taper 1 si c'est le joueur 1 qui commence sinon taper 2 si c'est la joueur 2 qui commence : ")) -1

   parite_joueur2= 1-parite_joueur1

   partie_finie= False

   match_nul=False

   tour =0

   nbPionsJoueur1=nombre_pions(len(damier[0]),len(damier))
   nbPionsJoueur2=nombre_pions(len(damier[0]),len(damier))



   while not partie_finie and not match_nul:

      if tour == parite_joueur1 :
         dernierCoup=jouer_tour(nb_joueur1,damier)
         nbPionsJoueur1+=-1
         afficheDamier(damier)


         if victoire(damier,dernierCoup,nb_joueur1,4)== True :
            print("")
            print("joueur 1 bravo vous avez gagné la partie !")
            partie_finie = True

         if nbPionsJoueur1==0 and nbPionsJoueur2==0 : # correspond à un match nul
            print("")
            print("match nul il n'y a pas de gagnant !'")
            match_nul =True



      else:

         dernierCoup=jouer_tour(nb_joueur2,damier)
         nbPionsJoueur2+=-1
         afficheDamier(damier)

         if victoire(damier,dernierCoup,nb_joueur2,4)== True :
            print("")
            print("joueur 2 bravo vous avez gagné la partie !")
            partie_finie = True

         if nbPionsJoueur1==0 and nbPionsJoueur2==0 :
            print("match nul il n'y a pas de gagnant !'")
            match_nul =True

      tour+=1
      tour=tour%2

   refaire_partie=int(input("Voulez-vous refaire une partie ? taper 1 si oui , taper 2 sinon : "))

   if refaire_partie == 1 :
      Puissance4Duo()
