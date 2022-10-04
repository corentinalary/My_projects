##################### Import ############
import pygame

################### Définition ##########

def Applaudir():

    """ fonction qui lance un son d'applaudissement """

    pygame.mixer.init()

    SonApplaudissement=pygame.mixer.Sound("SonApplaudissement.wav")
    SonApplaudissement.play() # Le son d'applaudissement est joué 1x
