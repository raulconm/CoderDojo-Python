def dibuja_figura(tortuga, x, y, lados, largo):
    tortuga.penup()
    girar_grados = 360 / lados    # calcula los grados que debe girar
    tortuga.setpos(x,y)
    tortuga.pendown()
    for cuenta in range(lados):
        tortuga.forward(largo)
        tortuga.right(girar_grados)
    tortuga.penup()


from turtle import *
from random import randrange # usa la función randrange de la librería de números aleatorios

espacio = Screen()
ancho_pantalla=1290
alto_pantalla=972

espacio.screensize(ancho_pantalla,alto_pantalla,"white")
federica = Turtle()
federica.speed(0)
federica.color("blue", "green")
federica.begin_fill()



for numero_de_figuras in range(500):
    federica.pensize(randrange(1,8))
    coord_x = randrange(ancho_pantalla)
    coord_y = randrange(alto_pantalla)
    lados = randrange(3,7)
    tamanio = randrange(20,40)
    dibuja_figura(federica, coord_x, coord_y, lados, tamanio)
