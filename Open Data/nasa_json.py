import urllib
import json
from urllib.request import urlopen

# Guarda en datos el contenido de la página
datos = urlopen("https://api.nasa.gov/neo/rest/v1/feed?start_date=2016-01-01&end_date=2016-01-05&api_key=VSKTLrP55m8FmLhCnRZb29oVcUPv2x9D7bwMrBuF")

# Lo convierte a texto y lo guarda en datos_json
datos_json = json.loads(datos.readall().decode('utf-8'))

print(datos_json)

archivo = open('asteroides.json','w')

#contenido = json.dump(datos_json)

#print(contenido)
#archivo.write(contenido)
archivo.close()



