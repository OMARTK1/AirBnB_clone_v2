#!/usr/bin/python3

""" It modules the script and starts a Flask web application
listening on 0.0.0.0 and port 5000 and use the option
strict_slashes=False in the route definition
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """the function called through the / route"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
