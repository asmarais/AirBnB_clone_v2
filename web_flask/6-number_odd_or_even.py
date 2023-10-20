#!/usr/bin/python3
""" 4. Start a Flask web application with 5 views function"""


from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ Returns Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ replace text with variable. """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/(<text>)', strict_slashes=False)
def python_text(text="is cool"):
    """ replace text with variable. """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_number_int(n):
    """ display “n is a number” only if n is an integer"""
    number = str(n)
    return '{} is a number'.format(number)


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_num(n):
    """ display html if n is int. """
    n = str(n)
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    """ display html if n is int and specify if it is odd or even"""
    if n % 2 == 0:
        text = "even"
    else:
        text = "odd"
    n = str(n)
    return render_template('6-number_odd_or_even.html', n=n, text=text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
