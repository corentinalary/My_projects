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
from random import *
from jouer_tour_IA import *
from minimax import *

##########Programme########
def modeMonoJoueur():

   """ fonction qui simule une partie de puissance 4 contre l'ordinateur.
   En début de partie on demande qui commence et ça sera donc le joueur choisi qui commencera à jouer.
   Tant qu'il n'y a pas de match nul ou de victoire la partie continue.
   La fonction alterne les tours entre le joueur 1 et l'IA.
   Quand c'est au tour du joueur 1 la fonction lui demande de choisir une colonne et si elle est valide  place le jeton du joueur 1 dans la colonne choisie du damier.
   Quand c'est au tour de l'IA elle place son jeton dans le colonne déterminé par la fonction minimax et affiche la colonne qu'elle a choisi avec un message.
   A la fin de Chaque tour on affiche le damier puis on regarde si il y a victoire ou match nul auquel cas on affiche un message.
   Après un match nul ou une victoire entrainant la fin de partie on demande au joueur si il souhaite refaire une partie auquel cas on relance la fonction , sinon on l'arrête. """

   damier=genereDamier(6,7)

   afficheDamier(damier)

   nb_joueur1=1
   nb_IA=2

   print("")
   parite_joueur1=int(input("Taper 1 si c'est le joueur 1 sinon taper 2 si c'est l'IA qui commence : "))-1

   parite_IA= 1-parite_joueur1

   partie_finie= False

   match_nul=False

   tour =0

   nbPionsJoueur1=nombre_pions(len(damier[0]),len(damier))
   nbPionsIA=nombre_pions(len(damier[0]),len(damier))



   while not partie_finie and not match_nul:



      if tour == parite_joueur1 :
         dernierCoup=jouer_tour(nb_joueur1,damier)
         nbPionsJoueur1+=-1
         afficheDamier(damier)


         if victoire(damier,dernierCoup,nb_joueur1,4)== True :
            print("")
            print("joueur 1 bravo vous avez gagné la partie !")
            partie_finie = True

         if nbPionsJoueur1==0 and nbPionsIA==0 :
            print("match nul il n'y a pas de gagnant !'")
            match_nul =True


      else:

         meilleureColonne, score_minimax=minimax(damier, 6, -float('inf'), float('inf') , True)

         dernierCoup=jouer_tour_IA(meilleureColonne,damier)

         nbPionsIA+=-1
         afficheDamier(damier)

         if victoire(damier,dernierCoup,nb_IA,4)== True :
            print("")
            print("IA bravo vous avez gagné la partie !")
            partie_finie = True

         if nbPionsJoueur1==0 and nbPionsIA==0 :
            print("match nul il n'y a pas de gagnant !'")
            match_nul =True

      tour+=1
      tour=tour%2

   refaire_partie=int(input("Voulez-vous refaire une partie ? taper 1 si oui , taper 2 sinon : "))

   if refaire_partie == 1 :
      modeMonoJoueur()

modeMonoJoueur()
