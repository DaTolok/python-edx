# Ejemplo 1
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Credentials
client_ID = "e5f77bc4867e478daad69b1c610af08a"
client_secret = "35d921b1e3f74a3b97fbd9552886ab4d"

# Authentication
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_ID,
                                                                              client_secret=client_secret))
# Search for songs with "rock"
results = spotify.search(q="rock", limit=20, type="track", market=None)

print('Keys for results:')
print(results.keys(), "\n")

print('Keys for results["tracks"]:')
print(results["tracks"].keys(), "\n")

print('Keys for results["tracks"]["items"][0]:')
print(results["tracks"]["items"][0].keys(), "\n")

print('Keys for results["tracks"]["items"][0]["artists"][0]:')
print(results["tracks"]["items"][0]["artists"][0].keys(), "\n")

for item in results["tracks"]["items"]:
    track_name = item["name"]
    track_id = item["id"]

    artist_name = item["artists"][0]["name"]
    artist_id = item["artists"][0]["id"]

    if len(track_name) >= 40:
        track_name = track_name[:37]
        track_name += "..."

    print("{:40s} - {} - {:20s} - {}".format(track_name, track_id, artist_name, artist_id))
