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

@app.route('/c/<text>')
def get_url(text):
    text = 'C ' + text.replace('_', ' ')
    return text

@app.route('/python/<text>/')
@app.route('/python')
def py_url(text='is cool'):
    text = 'Python ' + text.replace('_', ' ')
    return text

@app.route('/number/<n>')
def num_url(n):
    try:
        n = int(n)
    except ValueError:
        abort(404)
    text = str(n) + ' is a number'
    return text

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)
