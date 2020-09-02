#!/usr/bin/python3
"""ez flask app"""
from flask import Flask, abort, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters(id=None):
    """get all states and cities by id"""
    states = storage.all('State')
    am = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', states = states,  am=am)


@app.teardown_appcontext
def do_teardown(self):
    """close storage"""
    storage.close()
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
