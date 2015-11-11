def cuadrado(tortuga, lado):
    tortuga.forward(lado)           
    tortuga.right(90)              
    tortuga.forward(lado)           
    tortuga.right(90)              
    tortuga.forward(lado)           
    tortuga.right(90)              
    tortuga.forward(lado)           
    tortuga.right(90)

def triangulo(tortuga, lado):
    tortuga.forward(lado)           
    tortuga.right(120)             
    tortuga.forward(lado)           
    tortuga.right(120)              
    tortuga.forward(lado)

def casa(juanita, lado):
    cuadrado(juanita, lado)
    juanita.left(60)
    triangulo(juanita, lado)    

from turtle import *        # usa la libreria turtle
from random import randrange # usa la función randrange de la librería de números aleatorios


espacio = Screen()            # crea una pantalla de tortuga (espacio)
juanita = Turtle()             # crea una tortuga llamada juanita

for veces in range(10):
    juanita.setpos(randrange(300),randrange(200))   #posicióna la tortuga en doordenadas x e y aleatorias
    casa(juanita, randrange(30))    # dibuja una tortuga de tamaño aleatorio



           
