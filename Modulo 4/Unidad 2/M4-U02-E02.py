# Ejemplo 2
from datetime import datetime
import json
 
# Archivo JSON
fileJSON = '''{"message": "success",
           	"iss_position": {"longitude": "124.1861",
                                "latitude": "-0.6813"},
           	"timestamp": 1621242026
       	}'''
 
# Conversion JSON a Objeto de Python
data = json.loads(fileJSON)
 
# Extracción de longitud, latitud y tiempo
lon = data["iss_position"]["longitude"]
lat = data["iss_position"]["latitude"]
timestamp = data["timestamp"]
timestamp = datetime.fromtimestamp(timestamp)
 
print("ISS Current Position:")
print(f'lon: {lon}, lat: {lat}, time: {timestamp} \n')
 
# Creación de JSON
newJSON = json.dumps(data)
print(type(newJSON))
print(newJSON)
