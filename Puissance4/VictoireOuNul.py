################## Imports ###########################
from Applaudir import *
from victoire import *
from tkinter import *
from afficheDamierGraphique import *
import tkinter.font as tkFont
from SonMatchNul import *

################# Définition #######################

def VictoireOuNul(damier,dernierCoup,nb_joueur,partie_finie,match_nul,nbPionsJoueur1,nbPionsJoueur2,canvasHaut):

    """ fonction qui passe partie_finie en True en cas de victoire, passe match_nul en True en cas de match nul, qui affiche un message en cas de victoire ou de nul et enfin qui retourne partie_finie, match_nul. De plus cette fonction lance un son d'applaudissement en cas de victoire ou un son particulier en cas de match nul.

    Paramètres :
        - damier qui correspond au damier dans la console

        - dernierCoup qui correspond à [colonne du dernier coup joué, ligne du dernier coup joué]

        - nb_joueur qui vaut soit 1 si on utilise la fonction pour le joueur 1 soit 2 si on utilise la fonction pour le joueur 2

        - partie_finie qui vaut partie_finie (c'est-à-dire False tant que il n'y a pas de victoire )

        - match_nul qui vaut match_nul (c'est-à-dire False tant que il n'y a pas de match nul )

        - nbPionsJoueur1 qui vaut nbPionsJoueur1 ( c'est-à-dire le nombre de pions à la disposition du joueur 1 )

        - nbPionsJoueur2 qui vaut nbPionsJoueur2 ( c'est-à-dire le nombre de pions à la disposition du joueur 2 )

        - canvasHaut qui correspond au canvas canvasHaut """

    nbPionSuccessifs=4

    nb_joueur1=1
    nb_joueur2=2

    fontStyle = tkFont.Font(family="Arial", size=30)

    if victoire(damier,dernierCoup,nb_joueur,nbPionSuccessifs)== True :

        if nb_joueur == nb_joueur1 :

            MessageVictoire=Label(canvasHaut, text='Victoire du joueur 1 ! Bravo !', bg='#095811', foreground='white', font=fontStyle)

        else :
            MessageVictoire=Label(canvasHaut, text='Victoire du joueur 2 ! Bravo !', bg='#095811', foreground='white', font=fontStyle)

        MessageVictoire.pack(expand=YES)
        Applaudir()

        partie_finie = True

        return partie_finie, match_nul



    if nbPionsJoueur1==0 and nbPionsJoueur2==0 :

        MessageNul=Label(canvasHaut, text='Match nul !', bg='#095811', foreground='white', font=fontStyle)

        MessageNul.pack(expand=YES)
        SonMatchNul()

        match_nul =True

        return partie_finie, match_nul

    else :
        return partie_finie, match_nul
