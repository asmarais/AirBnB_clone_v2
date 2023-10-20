#!/usr/bin/python3
""" 3. Start a Flask web application with 4 views function"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ Returns Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns HBNB"""
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ replace text with variable. """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """ replace text with variable. """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
