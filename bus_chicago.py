import urllib
import webbrowser

from urllib.request import urlopen
u = urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()
f = open('rt22.xml', 'wb')
f.write(data)
f.close()

from xml.etree.ElementTree import parse
doc = parse('rt22.xml')

direccion = 'https://maps.googleapis.com/maps/api/staticmap?'
for bus in doc.findall('bus'):
    id = bus.findtext('id')
    lat = float(bus.findtext('lat'))
    lon = float(bus.findtext('lon'))
    direccion = direccion+'&markers=color:purple|label:'+id+'|'+str(lat)+','+str(lon)

webbrowser.open(direccion+'&zoom=13&size=1300x600&key=AIzaSyAOkV93yK7uleG9MHPevRNzhsKE_PQ6KmA')
#webbrowser.open('https://maps.googleapis.com/maps/api/staticmap?'+'markers=color:purple|label:'+d+'|'+str(lat)+','+str(lon)+'&zoom=13&size=1300x600&key=AIzaSyAOkV93yK7uleG9MHPevRNzhsKE_PQ6KmA')


