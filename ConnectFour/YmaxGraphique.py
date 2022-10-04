###################### Définition ######################

def YmaxGraphique(ligne):

    """ fonction qui convertit la ligne d'un damier en coordonnée y de l'image du damier sur le canvas du programme Puissance4DuoGraphique.
    Cette coordonnée y est au centre de la case de l'image du damier.

    Paramètre :
        - ligne qui correspond à la ligne d'un damier de 6 lignes, c'est donc un entier compris entre 0 et 5. """


    if ligne ==0 :
        y=725

    if ligne ==1 :
        y=610

    if ligne ==2 :
        y=495

    if ligne ==3 :
        y=385

    if ligne ==4 :
        y=265

    if ligne ==5 :
        y=150

    return y
