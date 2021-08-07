#!/usr/bin/env python3
##################################### Imports ##############################
from damier import *
from colonne_Clique import *
from nombre_pions import *
from tkinter import *
from VictoireOuNul import *
from joueTourComplet import *
from AnimationDeplacementPion import *

################################## Programme ###############################
damier= genereDamier(6,7) #damier représente le damier dans la console
nbPionsJoueur1 = nbPionsJoueur2 = nombre_pions(len(damier[0]),len(damier)) # nombre de pions à la disposition du joueur 1 ou 2 au cours d'une partie, une fois épuisé il ne peut plus jouer
partie_finie= False
match_nul=False
parite_joueur1,parite_joueur2=0,1 #joueur 1 est pair et joueur 2 est impair
nb_joueur1,nb_joueur2=1,2
tour =0
dy=2 # vitesse verticale à laquelle on va faire tomber le jeton dans l'animation suivante

def SuitPion(event):
   """fonction qui fait que la fleche jaune ou rouge au dessus du damier suive la souris quand elle est comprise dans les bords du damier.
      Paramètre : event qui correspond au deplacement de la souris dans l'interface de jeu"""
   X,Y= event.x,60
   global ImageFleche
   if X>400 and X<1150 :
      canvas.coords(ImageFleche,X,Y)

def ClicSurDamierGraphique(event):
   """ Fonction qui définit ce qu'il va se passer lorsqu'un joueur clique dans la fenetre de jeu
   Paramètres : event qui correspond au fait qu'un joeur clique dans la fenetre de jeu """
   X,Y=event.x,event.y # coordonnées X et Y de l'endroit ou a cliqué le joueur

   colonne_choisie=colonne_Clique(X,Y) # colonne_choisie correspond à la convertion de la colonne selectionné par le joueur dans la fenetre de jeu en colonne du damier de la console

   global partie_finie, match_nul, tour,nbPionsJoueur1, nbPionsJoueur2, tour, ImageFleche

   if not partie_finie and not match_nul and colonne_choisie!=float('inf') : #si la partie n'est pas finit, qu'il n'y a pas match nul et que le joueur a selectionné une colonne du damier :
      if tour == parite_joueur1 : # si tour est pair joueur 1 joue

         x0,y0,dernierCoup,ymaxGraphique,nbPionsJoueur1 = joueTourComplet(nb_joueur1,damier,colonne_choisie,nbPionsJoueur1) # x0,y0 corespondent au coordonnees de la case la plus haute de la colonne selectionnée dans le graphique par le joueur 1 ; dernierCoup à [colonne_choisie, ligne du dernier coup ] ; ymaxGraphique au y dans la fenetre de jeu sur lequel le pion jaune tombe quand un coup est joué
         Image=canvas.create_image(x0,y0, image=imagePionJaune) #affiche un Pion jaune en x0,y0
         canvas.lift(ImageDamier)#mettre damier au premier plan
         AnimationDeplacementPion(canvas,Image,ymaxGraphique)
         canvas.delete(ImageFleche)#On change la couleur de la fleche à chaque tour an suprrimant la fleche jaune et en creant la rouge
         ImageFleche=canvas.create_image(X,60, image=imageFlecheRouge)

         partie_finie, match_nul =VictoireOuNul(damier,dernierCoup,nb_joueur1,partie_finie,match_nul,nbPionsJoueur1,nbPionsJoueur2, canvasHaut) # Passe la valeur de partie_finie ou match_nul à True en cas de Victoire ou de match nul

      else:
         x0,y0,dernierCoup,ymaxGraphique,nbPionsJoueur2 = joueTourComplet(nb_joueur2,damier,colonne_choisie,nbPionsJoueur2)# x0,y0 corespondent au coordonnees de la case la plus haute de la colonne selectionnée dans le graphique par le joueur 2 ; dernierCoup à [colonne_choisie, ligne du dernier coup ] ; ymaxGraphique au y dans la fenetre de jeu sur lequel le pion rouge tombe quand un coup est joué
         Image=canvas.create_image(x0,y0, image=imagePionRouge) #affiche un Pion rouge en x0,y0
         canvas.lift(ImageDamier)#mettre damier au premier plan
         AnimationDeplacementPion(canvas,Image,ymaxGraphique)
         canvas.delete(ImageFleche)#On change la couleur de la fleche à chaque tour an suprrimant la fleche rouge et en creant la jaune
         ImageFleche=canvas.create_image(X,60, image=imageFlecheJaune)

         partie_finie, match_nul =VictoireOuNul(damier,dernierCoup,nb_joueur2,partie_finie,match_nul,nbPionsJoueur1,nbPionsJoueur2,canvasHaut) # Passe la valeur de partie_finie ou match_nul à True en cas de Victoire ou de match nul

      tour+=1
      tour=tour%2# A chaque coup joué on alterne la valeur de tour entre pair et impaire de telle façon à faire jouer alternativement le joueur 1 et 2

#création d'une fenetre
fenetre=Tk()
#Personnalisation cette fenetre
fenetre.title("Puissance 4") # Puissance 4 en Titre de la fenetre
fenetre.geometry("1500x900") #dimension de la fenetre
fenetre.config(background='#095811') #couleur de fond de la fenetre

#création d'une frame
frame=Frame(fenetre, bg='#095811', bd=0, relief=SUNKEN,highlightthickness=0)

# Création du canvas principale nommé canvas situé en dessous du canvas canvasHaut
largeur= 1500
hauteur=900
canvas=Canvas(frame, width=largeur, height=hauteur, bg='#095811', highlightthickness=0)

#Chargement des images du damier vide et de son fond, du pion jaune et rouge ainsi que des flèches jaunes et rouges
damierVide=PhotoImage(file="damierVide.png").zoom(5).subsample(5)
fondDamier=PhotoImage(file="fondDamier.png").zoom(5).subsample(5)
ImageDamier=canvas.create_image(largeur/2, hauteur/2, image=damierVide)
FondDamier=canvas.create_image(largeur/2, hauteur/2, image=fondDamier)
imagePionRouge=PhotoImage(file="pion_rouge.png").zoom(6).subsample(5)
imagePionJaune=PhotoImage(file="pion_jaune.png").zoom(6).subsample(5)
imageFlecheRouge=PhotoImage(file="imageFlecheRouge.png").zoom(1).subsample(3)
imageFlecheJaune=PhotoImage(file="imageFlecheJaune.png").zoom(1).subsample(3)
ImageFleche=canvas.create_image(400, 50, image=imageFlecheJaune)
canvas.bind('<Button-1>',ClicSurDamierGraphique) # On associe à l'évévement clic gauche la fonction ClicSurDamierGraphique
canvas.bind('<Motion>', SuitPion)
canvas.focus_set()
canvas.grid(row=1, column=0)

# Création du canvas canvasHaut situé au dessus du canvas principal
canvasHaut=Canvas(frame, width=200, height=30, bg='#095811', highlightthickness=0)
canvasHaut.grid(row=0, column=0,sticky='n')

#afficher la frame
frame.pack(expand=YES)
#afficher la fenetre
fenetre.mainloop()
