#!/usr/bin/python3
"""ez flask app"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_holberton():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    return 'HBNB'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
