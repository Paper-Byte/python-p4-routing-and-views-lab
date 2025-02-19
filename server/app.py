#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:parameter_string>')
def print_string(parameter_string):
    print(f'{parameter_string}')
    return parameter_string


@app.route('/count/<int:target>')
def count(target):
    return (str(num) + '\n' for num in range(target))


@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if (operation == '+'):
        return str(num1 + num2)
    elif (operation == '-'):
        return str(num1 - num2)
    elif (operation == '*'):
        return str(num1 * num2)
    elif (operation == '%'):
        return str(num1 % num2)
    else:
        return str(num1 / num2)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
