############################### Import ###########################
from evaluationScore import *

############################### Définition #######################

def scoreDamier(damier, nb_joueur):

    """ fonction qui analyse le damier entier et attribue un score au damier en tenant compte du numéro du joueur.
    Pour ce faire la fonction analyse le damier ligne par ligne, colonne par colonne, chacune des diagonale montante droite et enfin chacune des diagonale descendante droite.
    A chaque fois que la fonction parcoure une de ces directions elle regarde par paquet de 4 combien de jetons et de quel numéro s'y trouve.
    Elle augmente le score si des numéros du joueur nb_joueur s'y trouve et le baisse si le numéro de l'adversaire s'y trouve.
    Par exemple : la fonction va regarder à un moment sur la première ligne les 4 premiers jetons puis va se decaler d'un jeton sur la ligne  et regarder les 4 jetons suivant ce jeton etc... jusqu'au bout de la ligne.
    La fonction va ensuite en fonction des numéros de jetons qui s'y trouvent augmenter ou baisser le score.
    La fonction retourne à la fin la valeur du score.

    Paramètres :
        - damier qui correspond au damier que l'on étudie i.e à la liste composée de liste représentant des colonnes avec à l'intérieur des lignes

        - nb_joueur correspond au numéro du joueur pour lequel on va évaluer le score du damier , 1 si on évalue le damier pour le joueur 1 et 2 si on évalue le damier pour le joueur 1."""

    nb_ligne=6
    nb_colonne=7
    score=0

    # Score colonne au centre

    liste_colonne_centrale=damier[nb_colonne//2]
    JetonsAuCentre= liste_colonne_centrale.count(nb_joueur)
    score+= JetonsAuCentre *3


    # Score Horizontale

    for ligne in range(nb_ligne):

        liste_ligne=[]

        for colonne in damier :

            liste_ligne.append(colonne[ligne])

        for colonne in range(nb_colonne - 3):

            ligneDe4= []

            for i in range(4):
                ligneDe4.append(liste_ligne[colonne+ i])

            score+=evaluationScore(ligneDe4, nb_joueur)

    # Score Verticale

    for colonne in range(nb_colonne):

        liste_colonne=[]

        for ligne in damier[colonne] :

            liste_colonne.append(ligne)

        for ligne in range(nb_ligne - 3):

            colonneDe4= []

            for i in range(4):
                colonneDe4.append(liste_colonne[ligne+ i])

            score+=evaluationScore(colonneDe4, nb_joueur)

    # Score diagonale montante droite

    for ligne in range(nb_ligne -3):

        for colonne in range(nb_colonne -3):

            diagonaleGDe4=[]

            for i in range(4):
                diagonaleGDe4.append(damier[colonne+i][ligne+i])

            score+=evaluationScore(diagonaleGDe4, nb_joueur)

    # Score diagonale descendante droite

    for ligne in range(nb_ligne-1, nb_ligne-3,-1):

        for colonne in range(nb_colonne -3):

            diagonaleDDe4=[]

            for i in range(4):
                diagonaleDDe4.append(damier[colonne+i][ligne-i])

            score+=evaluationScore(diagonaleDDe4, nb_joueur)


    return score
