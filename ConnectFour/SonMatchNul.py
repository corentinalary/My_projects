##################### Import ############
import pygame

################### Définition ##########

def SonMatchNul():

    """ fonction qui lance un son d'applaudissement """

    pygame.mixer.init()

    SonApplaudissement=pygame.mixer.Sound("SonMatchNul.wav")
    SonApplaudissement.play() # Le son d'applaudissement est joué 1x
