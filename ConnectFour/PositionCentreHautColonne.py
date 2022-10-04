####################### Définition ###########################

def PositionCentreHautColonne(colonne_choisie):

    """ fonction qui prend en paramètre une colonne d'un damier qui retourne pour la colonne qui lui correspond sur l'image du damier dans le programme Puissance4DuoGraphique, les coordonnées x0,y0 de la case la plus haute de cette denière colonne.

    Paramètre :
        - colonne_choisie correspond à la colonne d'un damier i.e un entier compris entre 0 et le nombre de colonnes du damier-1 """

    y0=165

    if colonne_choisie == 0 :
        x0=410

    if colonne_choisie == 1 :
        x0=525

    if colonne_choisie == 2 :
        x0=640

    if colonne_choisie == 3 :
        x0=755

    if colonne_choisie == 4 :
        x0=870

    if colonne_choisie == 5 :
        x0=985

    if colonne_choisie == 6 :
        x0=1100

    return x0,y0
