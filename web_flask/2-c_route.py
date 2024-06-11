""" The web application listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by  value of the text variable
        (replace underscore _ symbols with a space )
And  must use the option strict_slashes=False in route definition"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """The function called through the / route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """The function called through the /hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """The function called through C followed by the value of the text"""
    text = text.replace('_', ' ')
    """It replaces "_" with space in text variable"""
    return f'C {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
