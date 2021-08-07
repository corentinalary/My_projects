######################## Définition ###########################

def placer_pion(choix_colonne,numero_joueur,damier):

    """ fonction qui ajoute le pion portant le numéro numero_joueur dans la colonne choix_colonne du damier
    dans la première ligne présentant une case vide i.e un 0.
    Cette fonction retourne également une liste [choix_colonne, ligne] avec ligne  qui correspond à ligne ou le pion a été déposé.

    Paramètres :
        - choix_colonne qui correspond à la colonne du damier ou l'on souhaite déposer le pion, c'est donc un entier compris entre 0 et nombre de colonne du damier -1

        - numero_joueur qui correspond au numéro du joueur pour lequel on dépose un pion i.e 1 si c'est le joueur 1 qui dépose un pion et 2 si c'est le joueur 2 qui dépose un pion

        - damier qui correspond au damier que l'on étudie i.e une liste composée de listes correspondant à des colonnes avec à l'intérieur des lignes. """

    nb_lignes=6
    ligne=0

    while damier[choix_colonne][ligne] != 0 and ligne <nb_lignes:
        ligne+=1


    damier[choix_colonne][ligne]=numero_joueur

    return [choix_colonne, ligne]
