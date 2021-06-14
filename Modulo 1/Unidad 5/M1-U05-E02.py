# Ejemplo 2
import urllib.request
 
url = 'http://textfiles.com/adventure/adventure.txt'
response = urllib.request.urlopen(url)
 
print(type(response))
print(response.read().decode())