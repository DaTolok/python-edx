# Ejemplo 1
import requests

url = "https://api.sunrise-sunset.org/json?lat=19.4326&lng=99.1332&date=2021-05-10"

results = requests.get(url)

print("Status Code: ", results.status_code)

data = results.json()
print("JSON: \n", data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print("Sunrise: ", sunrise, ", Sunset: ", sunset)