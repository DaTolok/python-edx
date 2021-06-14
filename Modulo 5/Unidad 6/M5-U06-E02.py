# Ejemplo 2
import requests

new_song = {
    "Artista":"Kansas",
    "Nombre":"Dust in the wind"
}

# Creates a new entry in the catalog
response = requests.post("http://127.0.0.1:5000/songs/new", json=new_song)
print(response.content.decode())

## Request the whole catalog
response = requests.get("http://127.0.0.1:5000/songs/all")
print("All catalog: \n", response.content.decode())