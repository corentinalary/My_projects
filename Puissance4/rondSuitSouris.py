from tkinter import *


largeur= 1500
hauteur=900



def Drag(event):
    """ Gestion de l'événement mouvement """
    X = event.x
    Y = event.y
    print(X,Y)

    if X>400 and X<1100 and Y<130 :

        # mise à jour de la position de l'objet (drag)

        canvas.coords(Image,X,Y)





#creer une premiere fenetre
fenetre=Tk()

#Personnaliser cette fenetre
fenetre.geometry("1500x900")

#creer une frame
frame=Frame(fenetre, bg='#095811', bd=0, relief=SUNKEN)

# Création d'un widget Canvas
canvas=Canvas(frame, width=largeur, height=hauteur, bg='#095811', highlightthickness=0)


#Chargement des images du damier, du pion jaune et du pion rouge
imageDamier=PhotoImage(file="Puissance4.3.png").zoom(5).subsample(5)
canvas.create_image(largeur/2, hauteur/2, image=imageDamier) #création du damier

imagePionJaune=PhotoImage(file="pion_jaune.png").zoom(6).subsample(5)
Image=canvas.create_image(400,50, image=imagePionJaune)


# Création d'un rond

canvas.bind('<Motion>',Drag)
canvas.focus_set()
canvas.pack(padx=10,pady=10)

#afficher la frame
frame.pack(expand=YES)

#afficher la fenetre
fenetre.mainloop()
