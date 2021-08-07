######################## Définition ##################################

def pions_successifs_direction(damier, xpion,ypion,directionx,directiony,numJoueur):

    """ fonction qui compte le nombre de pions successifs d'un joueur spécifié dans la direction d'une droite.
    Cette droite étant dirigé par le vecteur directionx en x et le vecteur directiony en y.
    De plus cette fonction se met à compter à partir d'un pion de coordonnées xpion,ypion et au sein d'un damier spécifié.
    Le pion en lui-même n'est pas compté.

    Paramètres :
        - damier correspond au damier dans la console que l'on étudie

        - xpion, ypion correspond aux coordonnees du pion à partir duquel on va regarder le nombre de pions successifs dans la direction donnée par directionx et directiony

        - directionx vaut -1, 0 ou 1 et représente le vecteur directeur selon x de la droite dans laquelle on va regarder le nombre de pions successifs

        - directiony vaut -1, 0 ou 1 et représente le vecteur directeur selon y de la droite dans laquelle on va regarder le nombre de pions successifs

        - numJoueur correspond au numero du joueur pour lequel on regarde le nombre de pions successifs i.e 1 si c'est oour le joueur 1 qu'on regarde et 2 si c'est pour le joueur 2 qu'on regarde. """

    compteur = 0

    while( (xpion+directionx)<(len(damier)) and (xpion+directionx)>=0 and (ypion+directiony)<len(damier[0]) and (ypion+directiony)>=0 and damier[xpion+directionx][ypion+directiony] == numJoueur )  :
        xpion = xpion+directionx
        ypion = ypion+directiony
        compteur = compteur+1


    return compteur
