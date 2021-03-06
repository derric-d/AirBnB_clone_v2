#!/usr/bin/python3
"""ez flask app"""
from flask import Flask, abort, render_template
from models import storage


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


@app.route('/number_template/<n>')
def template_url(n):
    try:
        n = int(n)
    except ValueError:
        abort(404)
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<n>')
def odd_even_url(n):
    try:
        n = int(n)
    except ValueError:
        abort(404)
    t = 'odd'
    if n % 2 == 0:
        t = 'even'
    return render_template('6-number_odd_or_even.html', n=n, t=t)


@app.route('/states_list')
def get_all_states():
    """get all states and render"""
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states')
def get_all_states_cities():
    """get all states and render"""
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def do_teardown(self):
    """close storage"""
    storage.close()
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
