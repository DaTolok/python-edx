# Ejemplo 1
import json
import requests

def text_search(query, location, radius, key):
    """
    Function to search places given a query using text_search from Places API

    Parameters:

                - query: The text string on which to search.
                - location: location: The latitude/longitude around which to retrieve place
                            information. This must be specified as latitude,
                            longitude.
                - radius: Defines the distance (in meters) within which to bias place results.
                - key: Your application's API key. This key identifies your application.

    Return:
                - results: Response results as a Python Dictionary.

    """
    endpoint_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        'query': query,
        'location': location,
        'radius': radius,
        'key': key
    }

    response = requests.get(endpoint_url, params=params)
    results = json.loads(response.content)
    return results

# API Key
API_KEY = "API KEY"

# Query
query = "pizza"

# Latitude and Longitude
latitude = "19.4326"
longitude = "-99.1332"
location = "{},{}".format(latitude, longitude)

# Radius in meters
radius = "1000"

# Retrieved Data
data = text_search(query, location, radius, API_KEY)

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