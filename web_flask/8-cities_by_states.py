#!/usr/bin/python3

"""The web application listening on 0.0.0.0, port 5000
- Use storage for fetching data from the storage engine:
  (FileStorage or DBStorage) => from models import storage and storage.all(...)
- After each request, the current SQLAlchemy Session must be removed:
  - Declare a method to handle @app.teardown_appcontext
  - Call in this method storage.close()
Routes:
    - /cities_by_states: display a HTML page: (inside the tag BODY)
      - H1 tag: “States”
      - UL tag: with the list of all State objects present in DBStorage
        sorted by name (A->Z)
        - LI tag: description of one State: <state.id>: <B><state.name></B>
        - UL tag: list of City objects linked to the State,sorted by name(A->Z)
        - LI tag: description of one City: <city.id>: <B><city.name></B>
And use the option strict_slashes=False in your route definition"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Removing the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displaying a HTML page with a list of States and Cities"""
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
