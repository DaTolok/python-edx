# Ejemplo 3
import urllib.request
 
url = 'http://textfiles.com/adventure/adventure.txt'
response = urllib.request.urlopen(url)
 
for line in response:
    print(line.decode().strip())