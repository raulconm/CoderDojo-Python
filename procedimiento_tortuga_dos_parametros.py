def cuadrado(tortuga, largo):
    tortuga.forward(largo)
    tortuga.right(90)
    tortuga.forward(largo)
    tortuga.right(90)
    tortuga.forward(largo)
    tortuga.right(90)
    tortuga.forward(largo)
    tortuga.right(90)

from turtle import *     # usa la libreria tortuga
space = Screen()         # crea una pantalla para la tortuga
juanita = Turtle()       # crea una tortuga llamada juanita
pepita = Turtle()
pepita.pencolor("blue")
cuadrado(juanita,100)       # dibuja un cudrado de largo 100
cuadrado(juanita,75)        # dibuja un cudrado de largo 75
cuadrado(pepita,50)        # dibuja un cudrado de largo 50

