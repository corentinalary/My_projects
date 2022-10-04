##Programmation du moteur de Jeu
from plateauJeu import *
from interfaceJeu import *

def valeurPionVoisin(plateau, xpion, ypion, directionx, directiony, valeurpionref):
    """Cette fonction permet de voir si il y a un enchainement de même pions pour une direction donnée.
        Pour chaques pions que l'on enchaine, on incrémente un compteur de 1 afin de faire un compte à la fin.
    Paramètres :
        plateau représente le plateau étudié
        xpion représente la ligne du pion de référence
        ypion représente la colonne du pion de référence
        directionx représente la direction niveau des lignes du pion qui sera étudié
        directiony représente la direction niveau des colonnes du pion qui sera étudié
        valeurpionref représente la valeur des pion du joueur (Ex: vapeurpionref=1 veut dire qu'on étudie les pions du
        premier joueur
    """
    ref = plateau[xpion][ypion]
    compteur = 0
    while ((xpion+directionx)<(len(plateau[0])-1)) and ((xpion+directionx)>=0) and ((ypion+directiony)<=len(plateau)) and ((ypion+directiony)>=0) and (plateau[xpion+directionx][ypion+directiony] == valeurpionref)  :
        xpion = xpion+directionx
        ypion = ypion+directiony
        compteur = compteur+1


    return compteur

def detectionVictoire(plateau,coup, joueur, tailleLignePourGagner):
    """On essaye de détecter si on a une ligne ou colonne ou diagonale de 4 fois le meme chiffre
        Par exemple le schéma [0,0,0,0,0,0,0]
                              [0,0,0,0,0,0,0]
                              [0,0,0,0,1,0,0]
                              [0,0,0,0,1,0,1]
                              [0,0,0,0,1,0,2]
                              [2,0,2,0,1,0,2] doit permettre de detecter une victoire du Joueur 1
        donc que si on considère les pions par les coordonées p[i][j] avec i la ligne
                                                                           j la colonne
        que p[6][5], p[5][5], p[4][5], p[3][5] ont pour valeur 1
        En cas de match nul, le jeu s'arrête.
        Paramètres :
            plateau représente le tableau à étudier
            coup représente le dernier coup joué afin de savoir quel coup on étudie
            joueur a pour valeur 1 ou 2 en fonction du joueur qui joue
            tailleLignePourGagner correspond au nombre de pions alignés à avoir pour gagner entre 3 et 5
                                                                           """
    x = 0
    y = 0
    for i in range(len(plateau)):
        if plateau[i][coup-1] != 0 :
            x = i
            y = coup-1
            break
#Detection
    if (valeurPionVoisin(plateau, x, y, 1, 0, joueur)+valeurPionVoisin(plateau, x, y, -1, 0, joueur) >= tailleLignePourGagner) or (valeurPionVoisin(plateau, x, y, 0, 1, joueur)+valeurPionVoisin(plateau, x, y, 0, -1, joueur) >= tailleLignePourGagner) or (valeurPionVoisin(plateau, x, y, -1, 1, joueur)+valeurPionVoisin(plateau, x, y, 1, -1, joueur) >= tailleLignePourGagner) or (valeurPionVoisin(plateau, x, y, -1, -1, joueur)+valeurPionVoisin(plateau, x, y, 1, 1, joueur) >= tailleLignePourGagner) :
        print("vous avez gagné joueur", joueur)
        affichageConsole(plateau)
        return 1
    else:
        matchnul=1
        for j in range(len(plateau[0])):
            matchnul=matchnul*plateau[0][j]
        if matchnul !=0 :
            print("match nul !")
            affichageConsole(plateau)
            return 1
        else:
            return 0

def jouer(nombreLignes, nombreColonnes, tailleGagnant, joueur):
    """Cette fonction permet de choisir ses paramètres afin de jouer
    le nombre de ligne * le nombre de colonne doit être pair
    le nombre de jetons par joueurs est de nombre de ligne * nombre de colonnes / 2
    Paramètres :
    nombreLignes est le nombre de lignes sur le damier
    nombreColonnes est le nombre colonnes du damier
    tailleGagnant est le nombre de jetons à aligner pour gagner
    joueur est le joueur qui commence
    """
    if (nombreLignes*nombreColonnes)%2 == 0:
        damier= plateauJeuTout(nombreLignes, nombreColonnes)
    else:
        print("Votre plateau n'est pas valide")
        return 0

    flag = 0
    while flag == 0:
        plateauPhysique(damier, nombreLignes,nombreColonnes)
        affichageConsole(damier)
        if flag != 0:
            break
        if joueur == 1 :
            #coup = int(input("Au tour de joueur "+ str(joueur)+ " chosissez votre colonne" ))
            #coup = rd.randint(1,nombreColonnes)
            coup = repondre()
        else:
            #coup = rd.randint(1,nombreColonnes)
            #coup = int(input("Au tour de joueur "+ str(joueur)+ " chosissez votre colonne" ))
            coup = repondre()
        if jeu(damier, coup, joueur) == 1 or coup > len(damier[0]) :
            print("Ce coup n'est pas possible !")
            #flag = detectionVictoire(damier,coup, joueur, tailleGagnant-1)

        else :
            flag = detectionVictoire(damier,coup, joueur, tailleGagnant-1)
            joueur = 3-joueur
