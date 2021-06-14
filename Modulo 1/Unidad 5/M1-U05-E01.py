# Ejemplo 1
import urllib.request
 
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
response = urllib.request.urlopen(url)
 
print(type(response))
print(response.read())