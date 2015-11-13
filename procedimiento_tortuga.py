def cuadrado(tortuga):
    tortuga.forward(100)
    tortuga.right(90)
    tortuga.forward(100)
    tortuga.right(90)
    tortuga.forward(100)
    tortuga.right(90)
    tortuga.forward(100)
    tortuga.right(90)

from turtle import *     # utiliza la libreria turtle
espacio = Screen()         # crea el espacio para la tortuga
juanita = Turtle()       # crea la tortuga juanita
cuadrado(juanita)        # dibuja un cuadrado con la tortuga juanita

