#!/usr/bin/python3

"""The web application listening on 0.0.0.0, port 5000
- Use storage for fetching data from the storage engine:
  (FileStorage or DBStorage) => from models import storage and storage.all(...)
- After each request, the current SQLAlchemy Session must be removed:
  - Declare a method to handle @app.teardown_appcontext
  - Call in this method storage.close()
Routes:
    - /states_list: display a HTML page: (inside the tag BODY)
      - H1 tag: “States”
      - UL tag: with the list of all State objects present in DBStorage
        sorted by name (A->Z)
        - LI tag: description of one State: <state.id>: <B><state.name></B>
And use the option strict_slashes=False in your route definition"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displaying a HTML page with a list of states"""
    sorted_states = sorted(list(storage.all("State").
                                values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown(exception):
    """Removing the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
