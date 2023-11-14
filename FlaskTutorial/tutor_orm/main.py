from flask import Flask
from model import Product, getdb

app = Flask(__name__)
# app.config.from_pyfile('config.cfg')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = getdb(app)
