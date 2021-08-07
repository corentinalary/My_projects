#!/usr/bin/env python3

def genereDamier(nbLignes, nbColonnes):
    """ fonction qui génère un damier à la console c'est-à-dire une liste composée de
    plusieurs listes représentant chacune une colonne du damier avec
    à l'intérieur différents éléments qui correspondent aux lignes du damier
    Paramètres :
        - nbLignes qui correspond au nombre de lignes que doit présenter notre damier

        - nbColonnes qui correspond au nombre de colonnes que doit présenter notre damier """

    damier_genere=[]
    for i in range(nbColonnes):
        colonne=[0]*nbLignes
        damier_genere.append(colonne)

    return damier_genere




def afficheDamier(damier_genere):

    """ fonction qui affiche le damier prit en paramètre de la façon suivante :
    Chaque 0 s'affiche comme une case vide, chaque 1 s'affiche avec un X et chaque 2 s'affiche avec un O.
    Paramètre :
        - damier_genere qui correspond au damier que l'on souhaite afficher """


    motifs=[' ','X','O']
    for index in range(len(damier_genere[0])-1,-1, -1):
        for colonne in damier_genere:

            print('|'+str(motifs[colonne[index]]),end='')
        print('|')

    for i in range(1,len(damier_genere)+1):

        print("--", end='')
    print('-')

    for i in range(1,len(damier_genere)+1):

        print('',i, end='')

afficheDamier(genereDamier(6,7))
