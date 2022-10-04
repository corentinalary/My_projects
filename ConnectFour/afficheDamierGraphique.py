########################## Import #####################
from tkinter import *

######################### Définition #################

def afficheDamierGraphique(damier, imagePionJaune,imagePionRouge, canvas):

    """ fonction qui parcourt le damier de la console et affiche dans le canvas soit une image de pion jaune si elle repère un 1 soit une image de pion rouge si elle repère un 2. Lorsqu'elles se créent ces images sont positionnées de sorte à parfaitement s'afficher dans les case de l'image du damier de programme Puissance4DuoGraphique.
    Paramètres :
        - damier qui correspond au damier dans la console que l'on étudie

        - imagePionJaune qui correspond à une image préalablement chargé avec PhotoImage de tkinter de pion jaune

        - imagePionRouge qui correspond à une image préalablement chargé avec PhotoImage de tkinter de pion rouge

        - canvas qui correspond au canvas que l'on étudie """

    for ligne in range(len(damier[0])-1,-1, -1):

        numColonne=-1
        for colonne in damier:
            numColonne+=1

            if colonne[ligne] == 1:
                canvas.create_image(414+113*numColonne,732-114*ligne , image=imagePionJaune)

            if colonne[ligne] ==2:
                canvas.create_image(414+113*numColonne,732-114*ligne, image=imagePionRouge)
