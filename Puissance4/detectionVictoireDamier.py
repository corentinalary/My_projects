###################### Définition ##########################

def detectionVictoireDamier(damier, nb_joueur):

    """ fonction qui analyse tout le damier et déterminer si le joueur portant le nombre nb_joueur à gagné.
    Pour ce faire la fonction regarde dans la direction verticale, horizontale puis diagonale montante et enfin diagonale descendante si il y a 4 pions alignés.
    En cas de victoire la fonction retourne True.

    Paramètres :
        - damier correspond au damier dans la console que l'on étudie

        - nb_joueur correspond au nombre du joueur pour lequel on regarde si il y a victoire ou non i.e 1 si on regarde pour le joueur 1 et 2 si on regarde pour le joueur 2. """

    nb_colonnes=7
    nb_lignes=6

    """ On regarde dans la direction horizontale si y a 4 pions du nb_joueur alignés """

    for colonne in range(nb_colonnes-3):
        for ligne in range(nb_lignes):

            if damier[colonne][ligne] == nb_joueur and damier[colonne+1][ligne] == nb_joueur and damier[colonne+2][ligne] == nb_joueur and damier[colonne+3][ligne] == nb_joueur:

                return True

    """ On regarde dans la direction verticale si y a 4 pions du nb_joueur alignés """

    for colonne in range(nb_colonnes):

        for ligne in range(nb_lignes-3):

            if damier[colonne][ligne] == nb_joueur and damier[colonne][ligne+1] == nb_joueur and damier[colonne][ligne+2] == nb_joueur and damier[colonne][ligne+3] == nb_joueur:

                return True

    """ On regarde dans les diagonales montantes si y a 4 pions du nb_joueur alignés """

    for colonne in range(nb_colonnes-3):

        for ligne in range(nb_lignes-3):

            if damier[colonne][ligne] == nb_joueur and damier[colonne+1][ligne+1] == nb_joueur and damier[colonne+2][ligne+2] == nb_joueur and damier[colonne+3][ligne+3] == nb_joueur:

                return True

    """ On regarde dans les diagonales descendantes si y a 4 pions du nb_joueur alignés """

    for colonne in range(nb_colonnes-3):

        for ligne in range(3, nb_lignes):

            if damier[colonne][ligne] == nb_joueur and damier[colonne+1][ligne-1] == nb_joueur and damier[colonne+2][ligne-2] == nb_joueur and damier[colonne+3][ligne-3] == nb_joueur:

                return True
