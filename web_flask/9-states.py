#!/usr/bin/python3

"""The web application listening on 0.0.0.0, port 5000
- Use storage for fetching data from the storage engine:
  (FileStorage or DBStorage) => from models import storage and storage.all(...)
- After each request, the current SQLAlchemy Session must be removed:
  - Declare a method to handle @app.teardown_appcontext
  - Call in this method storage.close()
Routes:
    - /states: display a HTML page: (inside the tag BODY)
      - H1 tag: “States”
      - UL tag: with the list of all State objects present in DBStorage
        sorted by name (A->Z)
        - LI tag: description of one State: <state.id>: <B><state.name></B>
    - /states/<id>: display a HTML page: (inside the tag BODY)
      - H1 tag: “State: <state.name>”
      - UL tag: with the list of City objects linked to the State
        sorted by name (A->Z)
        - LI tag: description of one City: <city.id>: <B><city.name></B>
And use the option strict_slashes=False in your route definition"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Removing the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def state():
    """Displaying a HTML page with states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """Displaying a HTML page with cities of that state"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
    return render_template('9-states.html', states=state, mode='none')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
