from flask import Flask, jsonify, request, Response
import json

app = Flask(__name__)

musics = [
    {
        'title': 'Just the way you are',
        'artist': 'Bruno Mars',
        'released date': 2010
    },
    {
        'title': 'Firework',
        'artist': 'Katy Perry',
        'released date': 2010
    },
    {
        'title': 'The Story of My Life',
        'artist': 'One Direction',
        'released date': 2013
    }
]

@app.route("/")
def welcome():
    return "<p>Welcome to my page! Andrew!</p>"

@app.route("/musics")
def get_musics():
    return jsonify({'musics': musics})

@app.route("/musics/<artist>")
def get_music_by_artist(artist):
    return_value = {}
    for music in musics:
        if music["artist"] == artist:
            return_value = {
                'title': music["title"],
                'released date': music["released date"]
            }
    return jsonify(return_value)

@app.route("/musics", methods=['POST'])
def add_music():
    request_data = request.get_json()
    new_music = {
        "title": request_data["title"],
        "artist": request_data["artist"],
        "released date": request_data["released date"]
    }
    musics.append(new_music)
    response = Response("", 201, mimetype="application/json")
    response.headers['Location'] = "/musics/" + request_data['artist']
    return response

@app.route("/musics/<artist>", methods=["PUT"])
def replace_music(artist):
    request_data = request.get_json()
    updated_music = {
        "title": request_data["title"],
        "artist": artist,
        "released date": request_data["released date"]
    }
    for music in musics:
        if music["artist"] == artist:
            music.update(updated_music)
            return Response("", status=204)
    return Response("", status=404)

@app.route("/musics/<artist>", methods=["PATCH"])
def update_music(artist):
    request_data = request.get_json()
    updated_music = {}
    if "title" in request_data:
        updated_music["title"] = request_data["title"]
    if "released date" in request_data:
        updated_music["released date"] = request_data["released date"]
    for music in musics:
        if music["artist"] == artist:
            music.update(updated_music)
    response = Response("", status=204)
    response.headers["Location"] = "/musics/" + artist
    return response

@app.route("/musics/<artist>", methods=["DELETE"])
def delete_music(artist):
    for music in musics:
        if music["artist"] == artist:
            musics.remove(music)
            response = Response("", status=204)
            return response
    invalidMusicObjectErrorMsg = {
        "error": "Music with the provided artist was not found"
    }
    response = Response(json.dumps(invalidMusicObjectErrorMsg), status=404, mimetype="application/json")
    return response

if __name__ == "__main__":
    app.run(debug=True)
