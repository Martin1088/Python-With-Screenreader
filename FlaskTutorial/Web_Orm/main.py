from operator import ge

from flask import Flask
from model import Product, getdb

app = Flask(__name__)
# app.config.from_pyfile('config.cfg')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = getdb(app)
