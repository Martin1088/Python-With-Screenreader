# from sqlite3 import *

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import class_mapper

db = SQLAlchemy()


def getdb(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
        return db
