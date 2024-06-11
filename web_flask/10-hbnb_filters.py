#!/usr/bin/python3
"""The Flask web application
- Use storage for fetching data from the storage engine
- After each request, the current SQLAlchemy Session must be removed:
  - Declares a method to handle @app.teardown_appcontext
  - Calling in this method storage.close()
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displaying the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """Removing the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
