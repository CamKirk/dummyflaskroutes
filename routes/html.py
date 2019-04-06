from flask import Blueprint, jsonify, render_template

htmlroutes = Blueprint('htmlroutes',__name__)

@htmlroutes.route('/')
def homeroute():
    return "hello world"

@htmlroutes.route('/bananaroute')
def banana():
    return render_template("index.html")
