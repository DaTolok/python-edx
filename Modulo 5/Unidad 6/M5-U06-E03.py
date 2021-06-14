# Ejemplo 3
import requests

edited_song = {
    "Artista":"Kansas",
    "Nombre":"Dust in the wind (Remastered)"
}


response = requests.put("http://127.0.0.1:5000/songs/5", json=edited_song)
print(response.content.decode())

edited_info = {
    "Nombre":"Dust in the wind (Original)",
    "Fecha":1977
}

response = requests.patch("http://127.0.0.1:5000/songs/5", json=edited_info)
print(response.content.decode())