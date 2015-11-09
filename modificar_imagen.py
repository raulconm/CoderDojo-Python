
from PIL import Image           # USA LA LIBRERIA DE TRATAMIENTO DE IMÁGENES


img = Image.open("lapices.jpg") # CARGA LA IMAGEN EN MEMORIA
imagen = img.load()

filas, columnas = img.size    # DIMENSIONES EN PIXELS

print(columnas)
print (filas)

img.show()                   # MUESTRA LA IMAGEN ORIGINAL

for cada_fila in range(filas):
    for cada_columna in range(columnas):
        rojo, verde, azul = imagen[cada_columna, cada_fila]              # TOMA LOS COLORES DEL PIXEL
        imagen[cada_columna, cada_fila] = (rojo, verde, azul)      # GUARDA LOS COLORES DEL PIXEL 

        
img.show()                   # MUESTRA LA IMAGEN YA MODIFICADA     
        
        
        

