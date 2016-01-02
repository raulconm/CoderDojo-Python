# Agrega los módulos necesarios

import urllib
from urllib.request import urlopen


# Se conecta al origen de datos

u = urlopen('http://www.mc30.es/images/xml/EstimacionesTrafico.xml')
datos = u.read()


#Guarda el contenido en un archivo en mi disco duro

f = open('archivo.xml', 'wb')
f.write(datos)
f.close()




# importa en el módulo actual el método parse del módulo xml.etree.ElementTree

from xml.etree.ElementTree import parse



# guarda en la variable doc el contenido del archivo 'archivo.xml'

doc = parse('archivo.xml')                 



# recorre todo el archivo de datos XML

for estimacion in doc.findall('Estimacion'):
    for campo in estimacion.findall('campo'):
        variable = campo.findtext('variable')
        valor = campo.findtext('valor')
        if variable == 'entradas_m30.descripcion':
            entrada = valor
        if variable == 'salidas_m30.descripcion':
            salida = valor
        # Toma y muestra la duracion solo si entramos por la A-3 y salimos por la A-5
        if variable == 'duracion' and entrada == 'A-3' and salida == 'A-5':
            duracion = valor
            print('De '+entrada+' a '+salida+' tardaremos '+duracion)
            
        

        

    
