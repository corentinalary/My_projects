########################## Imports ###########################
from BruitJetonQuiTombe import *
from YmaxGraphique import *
from PositionCentreHautColonne import *
from jouer_tour_graphique import *
from minimax import *
from afficheDamierGraphique import *
from jouer_tour_IA import *


######################## Définition ##########################

def JouerTourCompletIAGraphiquet(nb_joueur,damier,nbPionsJoueur):

        (meilleureColonne, scoreMinimax)=minimax(damier, 7, -float('inf'), float('inf') , True)

        dernierCoup=jouer_tour_graphique(nb_joueur,damier,meilleureColonne)
        nbPionsJoueur+=-1
        BruitJetonQuiTombe()

        ymax=dernierCoup[1]
        ymaxGraphique = YmaxGraphique(ymax)

        x0,y0=PositionCentreHautColonne(meilleureColonne)

        return x0,y0, dernierCoup, ymaxGraphique,nbPionsJoueur
