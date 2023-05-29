from flask import Flask, jsonify
from movies import marvel_movies
import random

app = Flask(__name__)

@app.route("/api/marvel")
def serve_marvel_movies():
    quotes = marvel_movies()
    nr_of_movies = len(quotes)
    selected_movie = quotes[random.randint(0, nr_of_movies - 1)]
    return jsonify(selected_movie)


if __name__ == "__main__":
    app.run(port=5000)
