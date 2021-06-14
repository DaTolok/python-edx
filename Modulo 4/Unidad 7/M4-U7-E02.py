# Ejemplo 2
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Credentials
client_ID = "CLIENT ID"
client_secret = "CLIENT SECRET"

# Authentication
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_ID,
                                                                              client_secret=client_secret))
# Artist ID
artist_ID = "1dfeR4HaWDbWqFHLkxsg1d"

results = spotify.artist_top_tracks(artist_ID)

print('Keys for results["tracks"][0]:')
print(results["tracks"][0].keys(), "\n")

print('Keys for results["tracks"][0]["album"]:')
print(results["tracks"][0]["album"].keys(), "\n")

for track in results['tracks'][:10]:
    track_name = track['name']
    album_name = track["album"]["name"]

    if len(track_name) >= 40:
        track_name = track_name[:37]
        track_name += "..."

    print("{:40s} - {:20s}".format(track_name, album_name))
