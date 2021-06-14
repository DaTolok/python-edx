# Ejemplo 1
import json
data = '''
{
	"number": 7,
	"message": "success",
	"people": [{"name": "Mark Vande Hei", "craft": "ISS"},
           	{"name": "Oleg Novitskiy", "craft": "ISS"},
           	{"name": "Pyotr Dubrov", "craft": "ISS"},
           	{"name": "Thomas Pesquet", "craft": "ISS"},
           	{"name": "Megan McArthur", "craft": "ISS"},
           	{"name": "Shane Kimbrough", "craft": "ISS"},
           	{"name": "Akihiko Hoshide", "craft": "ISS"}
           	]
}
'''
 
info = json.loads(data)
 
print(f'keys: \n {list(info.keys())}')
 
print(f'number: \n {info["number"]}')
 
print(f'people: \n {info["people"]}')
 
print("Astronauts:")
for astro in info["people"]:
	name  = astro["name"]
	craft = astro["craft"]
	print(f' name: {name}, craft: {craft}')