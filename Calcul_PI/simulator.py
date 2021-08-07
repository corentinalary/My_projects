#!/usr/bin/env python3
""" Simulation du nombre pi a partir de l'algorithme de Monte-Carlo"""
import sys
import random
import math


def est_dans_cercle(abscisse, ordonnee):
    """ retourne True si le point de coordonnees (abscisse,ordonnee)
    appartient au disque de centre (0,0) et de raordonneeon 1, retourne False sinon """

    if math.sqrt(abscisse**2 + ordonnee**2) <= 1:
        return True

    return False

def genere_points_aleatoire(nb_points, intervale):
    """ Genere nb_points points aleatoire dans l'intervale compris entre
    intervale[0] et intervale[1] ou intervale est un tuple,
    et retourne ceux-ci sous forme d'une liste de tuples """

    liste_points_aleatoire = []
    for indice in range(nb_points):
        ordonnee = random.uniform(intervale[0], intervale[1])
        abscisse = random.uniform(intervale[0], intervale[1])
        liste_points_aleatoire.append((abscisse, ordonnee))

    return liste_points_aleatoire

def tronque_nb(nb_a_tronquer, nb_chiffres_apres_virgule):
    """ Tronque nb_a_tronquer apres la virgule au nb_chiffres_apres_virgule ieme chiffre """
    nb_a_tronquer = nb_a_tronquer*(10**nb_chiffres_apres_virgule)
    nb_a_tronquer = int(nb_a_tronquer)
    nb_a_tronquer = nb_a_tronquer/(10**nb_chiffres_apres_virgule)
    return nb_a_tronquer

def simulateur(nb_points_a_simuler):
    """ Simule n points , retourne une liste de pi,
    une liste liste_points_dans_cercle , une liste liste_points_hors_cercle,
    correspondant respectivement et lorsque un dixieme des points a ete tire en plus
    a chaque nouveau pi, chaque nouvelle liste de points dans le cercle
    et a chaque nouvelle liste de points hors cercle """

    compteur = 0
    liste_points_aleatoire = genere_points_aleatoire(nb_points_a_simuler, (-1, 1))
    liste_points_dans_cercle = []
    liste_points_hors_cercle = []
    dixieme_nb_points_a_simuler = nb_points_a_simuler//10
    liste_pi = []


    for i in range(10):

        points_dans_cercle = []
        points_hors_cercle = []

        for point in range(i*dixieme_nb_points_a_simuler, (i+1)*dixieme_nb_points_a_simuler):

            if est_dans_cercle(liste_points_aleatoire[point][0], liste_points_aleatoire[point][1]):
                compteur += 1
                points_dans_cercle.append(liste_points_aleatoire[point])


            else:
                points_hors_cercle.append(liste_points_aleatoire[point])



        proba = compteur/(dixieme_nb_points_a_simuler*(i+1))
        pi_indice = 4*proba
        liste_points_dans_cercle.append(points_dans_cercle)
        liste_points_hors_cercle.append(points_hors_cercle)
        liste_pi.append(pi_indice)


    return liste_pi, liste_points_dans_cercle, liste_points_hors_cercle



def main():
    """ fonction main """
    if len(sys.argv) != 2:
        print("utilisation :", sys.argv[0], "nb_points_simulation")
        sys.exit(1)
    nb_points_simulation = int(sys.argv[1])
    print(simulateur(nb_points_simulation)[0][9])

if __name__ == "__main__":
    main()
