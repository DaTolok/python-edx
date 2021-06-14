# Ejemplo 1
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

song_db = [
    {
    "id": 0,
    "Artista": "Air Supply",
    "Nombre": "Making Love Out of Nothing at All"
    },
    {
    "id": 1,
    "Artista": "Bonnie Tyle",
    "Nombre": "Total Eclipse Of The Heart"
    },
    {
    "id": 2,
    "Artista": "George Michael",
    "Nombre": "Careless Whisper"
    },
    {
    "id": 3,
    "Artista": "Berlin",
    "Nombre": "Take My Breath Away"
    },
    {
    "id": 4,
    "Artista": "Queen",
    "Nombre": "Bohemian Rhapsody"
    }
]


## GET | returns the whole catalog
@app.route("/songs/all", methods = ["GET"])
def get_all():
    return jsonify(song_db), 200

## GET | returns an entry by an id
@app.route("/songs/<int:song_id>", methods = ["GET"])
def get_song(song_id):
    song_result = next((song for song in song_db if song["id"] == song_id), None)
    
    if song_result:
        return (jsonify(song_result), 200)
    else:
        return "404 Not Found", 404

## GET | returns all songs with the same name
@app.route("/songs/search/<string:song_name>", methods = ["GET"])
def search_song(song_name):
    songs = [song for song in song_db if song_name in song["Nombre"]]
    
    if songs:
        return (jsonify(songs), 200)
    else:
        return "404 Not Found", 404

## POST | creates a new entry in the catalog
@app.route("/songs/new", methods = ["POST"])
def post_song():

    if request.data:
        song_data = json.loads(request.data)
        
        song_id = max([song['id'] for song in song_db])+1
        song_artist = song_data["Artista"]
        song_name = song_data["Nombre"]
        
        new_song = {
            "id": song_id,
            "Artista": song_artist,
            "Nombre": song_name
        }
        
        song_db.append(new_song)
        
        return jsonify(new_song), 200
    else:
        return "400 Bad Request",400

## DELETE | deletes an entry in the catalog by an id
@app.route("/songs/<int:song_id>", methods = ["DELETE"])
def delete_song(song_id):
    
    for idx, song in enumerate(song_db):
        if song["id"] == song_id:
            song_db.pop(idx)
            
            return "Register Deleted", 200
    
    return "Not Found", 404

## PUT | replaces an entry in the catalog, creates a new entry if it doesn't exist
@app.route("/songs/<int:song_id>", methods = ["PUT"])
def put_song(song_id):
    if request.data:
        song_data = json.loads(request.data)
        
        song_artist = song_data["Artista"]
        song_name = song_data["Nombre"]
        
        edit_song = {
            "id": song_id,
            "Artista": song_artist,
            "Nombre": song_name
        }
        
        for idx, song in enumerate(song_db):
            if song["id"] == song_id:
                song_db[idx] = edit_song
                
                return (jsonify(edit_song), 200)
                
        edit_song["id"] = max([song['id'] for song in song_db])+1               
        song_db.append(edit_song)
                
        return (jsonify(edit_song), 200)
    else:
        return "Bad Request", 400
    

## PATCH | edits an entry in the catalog, fails if it doesn't exist
@app.route("/songs/<int:song_id>", methods = ["PATCH"])
def patch_song(song_id):
    if request.data:
        for idx, song in enumerate(song_db):
            if song["id"] == song_id:
                song_data = json.loads(request.data)
                
                for edit_key in song_data:
                    song[edit_key] = song_data[edit_key]
                
                return (jsonify(song), 200)
        
        return "Not Found", 404
    else:
        return "Bad Request", 400

if __name__ == "__main__":
    app.run(debug = True)




