
#!/usr/bin/env python3

from collections import namedtuple

Point=namedtuple("Point","x y")
Triangle= namedtuple("Triangle", "p1 p2 p3")


def affiche_triangle(triangle):
    """ Affiche les trois points de triangle sur la sortie standard """
    print("Premier point : x=" + str(triangle.p1.x) + "y="+ str(triangle.p1.y))
    print("Deuxieme point : x=" + str(triangle.p2.x) + "y="+ str(triangle.p2.y))
    print("Troisième point : x=" + str(triangle.p3.x) + "y="+ str(triangle.p3.y))



p1=Point(50,0)
p2=Point(0,50)
p3=Point(50,50)

triangle= Triangle(p1,p2,p3)
affiche_triangle(triangle)
