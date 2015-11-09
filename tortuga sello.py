from turtle import *

space = Screen()
maria = Turtle()
 
maria.pencolor("blue")           # Define el color de la tortuga
maria.shape("turtle")            # Define el aspecto de la tortuga

print(list(range(5, 60, 2)))    # Primero imprime todos los valores que va a tomar

maria.up()                       # Levanta el lapiz de la tortuga

for tamaño in range(5, 60, 2):  # comienza con tamaño 5 y crece de 2 en 2
    maria.stamp()                # imprime la forma de la toruga en el lienzo
    maria.forward(tamaño)        # mueve la tortuga hacia adelante
    maria.right(24)              # gira la tortuga a la derecha 
