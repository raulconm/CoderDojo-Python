from turtle import *        # usa la libreria de tortugas
space = Screen()            # crea un espacio para la tortuga
maria = Turtle()              # crea una tortuga llamada maria
maria.setheading(90)          # apunta al norte
lados = int(input("¿Cuántos lados? "))
for sides in range(lados):      # repite el bucle cuatro veces
    maria.forward(50)          # se mueve adelante
    maria.right(360/lados)           # gira 90 grados

