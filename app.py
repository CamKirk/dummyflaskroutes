from flask import Flask, url_for
import pymongo

app = Flask(__name__)


client = MongoClient("")
client = MongoClient(os.environ["MONGODB_URI"])

from routes.html import htmlroutes
from routes.api import apiroutes

app.register_blueprint(htmlroutes)
app.register_blueprint(apiroutes, url_prefix="/api")

app.run()