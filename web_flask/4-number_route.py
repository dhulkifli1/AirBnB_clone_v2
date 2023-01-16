#!/usr/bin/python3
'''Starts a Flask web application'''

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''Returns “Hello HBNB!”'''

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Returns "HBNB"'''

    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_var(text):
    '''Returns C plus variable text'''

    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/(<text>)', strict_slashes=False)
def python_route(text="is cool"):
    '''Displays “Python ”, followed by the value of the text variable'''

    return "Python " + text.replace("_", " ")


@app.route('/number/<n>', strict_slashes=False)
def is_number(n):
    '''Display “n is a number” only if n is an integer'''

    if (type(n) == int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
