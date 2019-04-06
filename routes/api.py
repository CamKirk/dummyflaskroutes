from flask import Blueprint, jsonify, render_template

apiroutes = Blueprint("apiroutes", __name__)

@apiroutes.route("/")
def instructions():
    return jsonify({
        "error": "Try sending a request to /api/<fruit>"
    })

@apiroutes.route("/<fruit>")
def slicer(fruit):
    return jsonify({
        "fruit": fruit,
        "sliced": "sliced " + fruit,
        "pysliced": fruit[:3]
    })

@apiroutes.route("/<year>")
def heatmaps(year):
    # go and find things in the mongo db