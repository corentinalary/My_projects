########################### Import ################
import pygame

########################## Définition ################

def BruitJetonQuiTombe():

    """ fonction qui lance un bruit de jeton qui tombe """

    pygame.mixer.init()

    JetonQuiTombe=pygame.mixer.Sound("JetonQuiTombe.wav")
    JetonQuiTombe.play() # Le son du jeton qui tombe est joué 1x
