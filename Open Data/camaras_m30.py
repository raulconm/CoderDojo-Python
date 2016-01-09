import urllib
import webbrowser

from urllib.request import urlopen
u = urlopen('http://www.mc30.es/components/com_hotspots/datos/camaras.xml')
data = u.read()
f = open('camaras_m30.xml', 'wb')
f.write(data)
f.close()

from xml.etree.ElementTree import parse
doc = parse('camaras_m30.xml')

direccion = 'https://maps.googleapis.com/maps/api/staticmap?'
for camara in doc.findall('Camara'):
    for posicion in camara.findall('Posicion'):
        lat = float(posicion.findtext('Latitud'))
        lon = float(posicion.findtext('Longitud'))
        direccion = direccion+'&markers=color:purple|label:S|'+str(lat)+','+str(lon)
    url = camara.findtext('URL')
    webbrowser.open(url)  # Abre la foto más actualizada de la cámara
        
        

webbrowser.open(direccion+'&zoom=13&size=1300x600&key=AIzaSyAOkV93yK7uleG9MHPevRNzhsKE_PQ6KmA')
#webbrowser.open('https://maps.googleapis.com/maps/api/staticmap?'+'markers=color:purple|label:C|'+str(lat)+','+str(lon)+'&zoom=13&size=1300x600&key=AIzaSyAOkV93yK7uleG9MHPevRNzhsKE_PQ6KmA')

