# Ejemplo 1
import requests
## Request the whole catalog
response = requests.get("http://127.0.0.1:5000/songs/all")
print("All catalog: \n", response.content.decode())
## Request an entry by an id
response = requests.get("http://127.0.0.1:5000/songs/1")
print("Song (ID): \n", response.content.decode())
# Request all songs with the same name
response = requests.get("http://127.0.0.1:5000/songs/search/Bohemian")
print("Song (name): \n", response.content.decode())