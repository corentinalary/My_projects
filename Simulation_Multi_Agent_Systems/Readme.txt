Projet Java :

  Notre projet est constituté des packages suivants, dans lesquels nous avons
  regroupé les classes ayant un fonctionnement similaire / complémentaire :
    - event
    - simulableObjects (les objets simulables comme ball, cell...)
    - simulableObjSets (les ensembles d'objets simulables)
    - simulator
    - tests

  Pour compiler les sources, vous pouvez utiliser le makefile fourni :
    make compile_Balls / compile_Conway / compile_Immigration / compile_Schelling / compile_Boids

  Pour compiler et exécuter un programme :
    make Balls / Conway / Immigration / Schelling / Boids
    
  Compiler toutes les sources :
    make all
    
  Supprimer tous les fichiers compilés :
    make clean
    
