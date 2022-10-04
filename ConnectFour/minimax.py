######################### Imports #########################
from prendColonneValide import *
from scoreDamier import *
from placer_pion import *
import copy
from random import *
from noeudTerminal import *
from detectionVictoireDamier import *

######################## Définition #######################
def minimax(damier, profondeur,alpha, beta, joueurMax):

    """ fonction qui se base sur l'algorithme Minimax avec élagage AlphaBeta pour déterminer la meilleure colonne sur laquelle jouer pour gagner.
    L'algorithme Minimax par du principe que le joueur va tout faire pour maximiser ses chances de gagner et son adversaire tout faire pour minimiser les chances du joueur.
    L'idée du Minimax est de faire un arbre avec toutes les possibilités comprennant : les coups possibles pour le joueur, les coups que l'adversaire pourrait répondre à ceux-ci , ceux que le joueur pourrait jouer en réaction à cette réponse etc...
    L'élagage AlphaBeta quand à lui est là pour accélerer le programme en ne considérant pas certaines branches de l'arbre des possibles du Minimax qui ne changent rien au résultat.
    Paramètres :
        - damier correspond au damier repésenter par une liste que l'on étudie

        - profondeur correspond au nombre de branches de notre arbre des possibles

        - alpha, beta :garde le fil du meilleur score que le joueur ou son adversaire peut atteindre en assumant que l'opposant joue le meilleur coup

        - joueurMax vaut True si on regarde pour le joueur qui veut maximiser ses chances et sinon False si on regarde du point de vue de l'adversaire """


    nb_IA=2
    nb_joueur1=1
    positions_valide =prendColonneValide(damier)

    noeud = noeudTerminal(damier)

    if profondeur== 0 or noeud ==True :

        if noeud==True :

            if detectionVictoireDamier(damier, nb_IA):
                return (None, 100000000000000)
            elif detectionVictoireDamier(damier, nb_joueur1):
                return (None, -10000000000000)


            #Partie finie aucun coup possible
            else :
                return (None,0)

        # profondeur vaut 0
        else :
            return (None, scoreDamier(damier, nb_IA))


    if joueurMax:
        valeur = -float('inf')
        Colonne=choice(positions_valide)

        for colonne in positions_valide :

            copieDamier=copy.deepcopy(damier)

            placer_pion(colonne,nb_IA,copieDamier)

            nouveauScore= minimax(copieDamier, profondeur-1,alpha,beta, False)[1]

            if nouveauScore > valeur :
                valeur =nouveauScore
                Colonne=colonne

            alpha=max(alpha, valeur)

            if alpha >=beta :
                break

        return Colonne, valeur

    #joueurMin
    else :
        valeur =float('inf')

        Colonne=choice(positions_valide)
        for colonne in positions_valide:

            copieDamier=copy.deepcopy(damier)
            placer_pion(colonne,nb_joueur1,copieDamier)

            nouveauScore=minimax(copieDamier, profondeur-1,alpha,beta, True)[1]


            if nouveauScore < valeur :
                valeur =nouveauScore
                Colonne=colonne

            beta= min(beta, valeur)

            if alpha >= beta :
                break

        return Colonne, valeur
