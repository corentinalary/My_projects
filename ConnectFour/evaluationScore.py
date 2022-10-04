############################## Définition #########################

def evaluationScore(action, nb_joueur):

    """ fonction qui évalue avec des valeurs arbitrairement choisies une action i.e une liste de 4 éléments d'un damier et en fonction du numéro du joueur.
    Si dans l'action la fonction répère 4 jetons portant le numéro nb_joueur alors le score augmente de 100, si c'est 3 jetons avec une case vide à coté il augmente de 40 et si c'est 2 jetons avec 2 cases vides à coté il augmente de 10.
    Si dans l'action la fonction répère 4 jetons portant le numéro de l'adversaire du joueur nb_joueur
alors le score baisse de 130, si c'est 3 jetons avec une case vide à coté il baisse de 110 et si c'est 2 jetons avec 2 cases vides à coté il baisse de 70.
A chaque fois on vérifié si il y a une case vide à coté car cela signifie que il y a plus tard possibilité d'aligner 4 jetons et donc de gagner.

    Paramètres :
        - action qui correspond à une liste d'éléments d'un damier i.e une liste de 4 éléments compris entre 0,1 et 2.

        - nb_joueur correspond au numéro du joueur pour lequel on évalue l'action i.e 1 si on évalue pour le joueur 1 et 2 si on évalue pour le joueur 2. """


    vide=0
    score=0
    nb_adversaire=1

    if nb_joueur ==1:
        nb_adversaire = 2

    # Score Pour l'attaque
    if action.count(nb_joueur)== 4 :

        score+=100

    if action.count(nb_joueur)==3 and action.count(vide)==1 :
        score+=5

    if action.count(nb_joueur)==2 and action.count(vide)==2:
        score+=2

    #score pour la defense

    if action.count(nb_adversaire)==3 and action.count(vide)==1 :
         score-= 4

    if action.count(nb_adversaire)==4 :
         score-= 150

    return score
