from turtle import *     # usa la libreria tortuga
from sys import *        # usa la libreria del sistema

space = Screen()         # crea espacio para la tortuga
zoe = Turtle()           # crea la tortuga zoe
zoe.setheading(90)       # apunta al norte

for repeticiones in range(20):   # repite el patrón 20 veces
    zoe.forward(10)                 # avanza un poco la tortuga
    zoe.right(18)                   # y gira un poco a la derecha

    # Dibuja el pentágono
    for lados in range(5):    # repite 5 veces
        zoe.forward(50)         # se mueve adelante 50 unidades
        zoe.right(72)           # gira 72 grados
