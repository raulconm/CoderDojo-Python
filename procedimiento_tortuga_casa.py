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

espacio = Screen()            # crea una pantalla de tortuga (espacio)

juanita = Turtle()             # crea una tortuga llamada juanita
casa(juanita, 90)
casa(juanita,10)
casa(juanita, 200)
           
