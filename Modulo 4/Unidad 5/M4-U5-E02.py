# Ejemplo 2
import json
import requests


def places_nearby(location, radius, types, key):
    """
    Function to search places nearby given location and radius using nearby_places from Places API

    Parameters:

                - location: location: The latitude/longitude around which to retrieve place
                            information. This must be specified as latitude,
                            longitude.
                - radius: Defines the distance (in meters) within which to bias place results.
                - types: Types of places to be searched.
                - key: Your application's API key. This key identifies your application.



    Return:
                - results: Response results as a JSON.

    """
    endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': location,
        'radius': radius,
        'types': types,
        'key': key
    }

    res = requests.get(endpoint_url, params=params)
    results = json.loads(res.content)
    return results

# API Key
API_KEY = "API KEY"

# Latitude and Longitude
latitude = "19.4326"
longitude = "-99.1332"
location = "{},{}".format(latitude, longitude)

# Radius in meters
radius = "1000"

# Types
types = "restaurant"

# Retrieved Data
data = places_nearby(location, radius, types, API_KEY)

# Response Data
print("Response:")
print(data)

# Elements in the Response
print("Response JSON contains the following keys:")
print(data.keys(),"\n")

# Places Found
print("The found places are:")
for item in data["results"]:
    print(item["name"])