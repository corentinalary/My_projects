############# Définition ###############

def nombre_pions(nombre_rangees, nombre_colonnes):

    """ fonction qui donne le nombre de pions qu'il est possible de jouer par joueur au cours d'une partie dans un damier de dimensions données.
    Paramètres :
        - nombre_rangees correspond au nombre de rangées du damier étudié

        - nombre_colonnes correspond au nombre de colonnes du damier étudié """

    nombre_pions= (nombre_rangees*nombre_colonnes)/2

    return int(nombre_pions)
