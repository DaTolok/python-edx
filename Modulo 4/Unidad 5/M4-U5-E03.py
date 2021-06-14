# Ejemplo 2
import json
import googlemaps

# API Key
API_KEY = "API KEY"

# Latitude and Longitude
latitude = "19.4326"
longitude = "-99.1332"
location = "{},{}".format(latitude, longitude)

# Radius in meters
radius = "1000"

# Type
types = "restaurant"

# Request by using googlemaps client
gmaps = googlemaps.Client(key = API_KEY)
data = gmaps.places_nearby(location=location, radius = radius, type = 'restaurant')

# Retrieved Data
print("Response:")
print(data)

# Elements in the Response
print("Response JSON contains the following keys:")
print(data.keys(),"\n")

# Places Found
print("The found places are:")
for item in data["results"]:
    print(item["name"])