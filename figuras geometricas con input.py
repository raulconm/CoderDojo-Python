from turtle import *        # usa la libreria de tortugas
space = Screen()            # crea un espacio para la tortuga
maria = Turtle()              # crea una tortuga llamada maria
maria.setheading(90)          # apunta al norte
for sides in range(4):      # repite el bucle cuatro veces
    maria.forward(50)          # se mueve adelante
    maria.right(90)           # gira 90 grados

