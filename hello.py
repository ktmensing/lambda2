from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birthday')
def birthday():
    return 'July 26, 1988'

@app.route('/greeting/<name>')
def say_hello(name):
    return 'Hello ' + name + '!'

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    total = a + b
    return str(total)

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    total = a * b
    return str(total)

@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    total = a - b
    return str(total)

@app.route('/favoritefoods')
def foods():
    myList = ['pizza', 'donuts', 'burgers']
    return jsonify(myList)
