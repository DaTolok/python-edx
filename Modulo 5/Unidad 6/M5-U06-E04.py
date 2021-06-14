# Ejemplo 4
import requests

response = requests.delete("http://127.0.0.1:5000/songs/5")
print(response.content.decode())


response = requests.get("http://127.0.0.1:5000/songs/all")
print(response.content.decode())