import urllib
import webbrowser
from xml.etree.ElementTree import parse

from urllib.request import urlopen

u = urlopen('http://servicios.emtmadrid.es:8080/rss/emtrss.xml')
datos = u.read()
archivo = open('servicios_emt.xml', 'wb')
archivo.write(datos)
archivo.close()



documento = parse('servicios_emt.xml')

for channel in documento.findall('channel'):
    titulo_general = channel.findtext('title')
    print(titulo_general)
    for item in channel.findall('item'):
        titulo_2 = item.findtext('title')
        descripcion = item.findtext('description')
        print(titulo_2+'\n----\n'+descripcion+'\n\n')
        
        

