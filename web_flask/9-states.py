#!/usr/bin/python3
"""ez flask app"""
from flask import Flask, abort, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def all_states_and_cities(id=None):
    """get all states and cities by id"""
    states = storage.all('State')
    if id:
        key = 'State.' + id
        if key in states:
            states = states[key]
        else:
            states = Nobe
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def do_teardown(self):
    """close storage"""
    storage.close()
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
