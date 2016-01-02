import json
import urllib
import webbrowser

from urllib.request import urlopen
u = urlopen('https://data.nasa.gov/resource/9g7e-7hzz.json')
data = u.read()
f = open('nasa.json', 'wb')
f.write(data)
f.close()

with open('nasa.json') as archivo_datos:    
    datos = json.load(archivo_datos)
print(datos)
