from tkinter import *

def AnimationDeplacementPion(canvas,Image,ymaxGraphique):

    def deplacement():
        """ fonction qui prend le Pion jaune et le fait tomber jusqu'au ymaxGraphique"""
        CoordonneesImage=canvas.coords(Image)
        if CoordonneesImage[1] <= ymaxGraphique:
            canvas.move(Image, 0,10)
            canvas.after(17, deplacement) #appel de la fonction deplacement() apres 17 milliseconde

    deplacement()
