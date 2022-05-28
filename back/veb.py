from crypt import methods
from sys import flags
from flask import Flask, jsonify, redirect
import flask
from flask import render_template, request
from flask_bootstrap import Bootstrap
from input import database

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index ():
    return redirect('login')

@app.route('/login', methods = ['GET', 'POST'])
def login ():
    if flask.request.method == 'POST':
        logini = flask.request.form.get("inputLogin")
        password = flask.request.form.get("inputPassword")
        checking = database.searching(logini, password)
        if checking == True:
            return redirect('/data')
        else:
            database.registraiton(logini, password)
            return redirect('/registered')
    return render_template('template1.html')

@app.route("/data")
def data():
    return render_template('template0.html', name = 'дорогой пользователь')

@app.route("/spreadsheet")
def tablisa():
    return render_template('template2.html')

@app.route("/registered")
def registered():
    return render_template('template3.html')

app.debug = True
app.run(host='0.0.0.0', port=8000)