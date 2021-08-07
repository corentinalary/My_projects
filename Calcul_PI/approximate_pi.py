#!/usr/bin/env python3
""" Representation visuel de notre simulation de PI avec simulator.py """


import subprocess
import sys
import cv2
from simulator import simulateur, tronque_nb



def converti_coordonnees(abscisse, ordonnee, taille_image):
    """ Converti les coordonnees d'un point du repere carre de dimension un
    en point dans le repere de l'image """

    if abscisse >= 0:
        abscisse_convertie = int(taille_image/2 +abscisse*taille_image/2)

    else:
        abscisse_convertie = int((1+abscisse)*taille_image/2)

    if ordonnee >= 0:
        ordonnee = int((1-ordonnee)*taille_image/2)

    else:
        ordonnee = int(taille_image/2+taille_image/2*(-ordonnee))

    return (abscisse_convertie, ordonnee)


########################################PROGRAMME####################################""


def generate_ppm_file(taille_image, nb_chiffres_apres_virgule, num_image,
                      liste_pi, liste_points_dans_cercle, liste_points_hors_cercle, liste_ppm):

    """ Genere image ppm representant l'etat de la simulation quand
        on a tire num_image dixieme des points """

    points_dans_cercle = liste_points_dans_cercle[num_image]
    points_hors_cercle = liste_points_hors_cercle[num_image]
    nombre_pi = liste_pi[num_image]
    nombre_pi = str(tronque_nb(nombre_pi, nb_chiffres_apres_virgule))

    #Ajout de 0 dans le cas où après la virgule il n'ordonnee a que des 0
    while len(nombre_pi) < 2 + nb_chiffres_apres_virgule:
        nombre_pi += '0'


    for (abscisse, ordonnee) in points_dans_cercle:
        (abscisse_convertie, ordonnee_convertie) = converti_coordonnees(abscisse, ordonnee,
                                                                        taille_image)
        liste_ppm[(abscisse_convertie-1)*taille_image+ordonnee_convertie] = (0, 0, 255)


    for (abscisse, ordonnee) in points_hors_cercle:
        (abscisse_convertie, ordonnee_convertie) = converti_coordonnees(abscisse, ordonnee,
                                                                        taille_image)
        liste_ppm[(abscisse_convertie-1)*taille_image+ordonnee_convertie] = (255, 0, 0)






    nombre_pi = nombre_pi.replace(".", "-")

    fichier = open("img{}_{}.ppm".format(num_image, nombre_pi), "wb")

    fichier.write(b"P6\n")
    fichier.write(bytes((str(taille_image) + " "+str(taille_image) + "\n").encode()))
    fichier.write(b"255\n")

    for tupple in liste_ppm:
        fichier.write(bytes([tupple[0]]))
        fichier.write(bytes([tupple[1]]))
        fichier.write(bytes([tupple[2]]))

    fichier.close()









    #############################Affichage nombre #########


    img = cv2.imread("img{}_{}.ppm".format(num_image, nombre_pi), cv2.IMREAD_COLOR)

    nombre_pi = nombre_pi.replace("-", ".")

    taille_police = int(taille_image* 4/1000 + 1)
    couleur_police = (0, 0, 0)
    epaisseur_police = int(taille_image* 4/1000 + 1)

    (hauteur_texte, largeur_texte), _ = cv2.getTextSize(nombre_pi, cv2.FONT_HERSHEY_SIMPLEX,
                                                        taille_police, epaisseur_police)
    font = cv2.FONT_HERSHEY_SIMPLEX
    centre = (int(taille_image/2 - hauteur_texte/2), int(taille_image/2 + largeur_texte/2))


    cv2.putText(img, nombre_pi, centre, font, taille_police, couleur_police, epaisseur_police)


    nombre_pi = nombre_pi.replace(".", "-")

    cv2.imwrite("img{}_{}.ppm".format(num_image, nombre_pi), img)



def main():
    """ fonction main """
    if len(sys.argv) != 4:

        raise IndexError("utilisation : "+ sys.argv[0]
                         + " TAILLE_IMAGE "+" NOMBRES_POINTS_SIMULES "
                         + " NB_CHIFFRES_APRES_VIRGULE")


    if not sys.argv[1].isdigit():
        raise ValueError("TAILLE_IMAGE (le 2eme argument) doit être un entier positif ")

    if not sys.argv[2].isdigit():
        raise ValueError("NOMBRES_POINTS_SIMULES (le 3eme argument) doit être un entier positif ")

    if not sys.argv[3].isdigit():
        raise ValueError("NB_CHIFFRES_APRES_VIRGULE ( 4eme argument) doit être un entier positif ")

    taille_image = int(sys.argv[1])
    nombre_points_simules = int(sys.argv[2])
    nb_chiffres_apres_virgule = int(sys.argv[3])



    liste_pi, liste_points_dans_cercle, liste_points_hors_cercle = simulateur(nombre_points_simules)



    liste_ppm = []
    for abscisse in range(taille_image):
        for ordonnee in range(taille_image):
            liste_ppm.append((255, 255, 255))

    for k in range(10):

        generate_ppm_file(taille_image, nb_chiffres_apres_virgule,
                          k, liste_pi, liste_points_dans_cercle,
                          liste_points_hors_cercle, liste_ppm)

    fichier_a_convertir = "*.ppm"
    gif_en_sortie = "output.gif"
    subprocess.call("convert -delay 100 -loop 5 " + fichier_a_convertir
                    + " " + gif_en_sortie, shell=True)




if __name__ == "__main__":
    main()
