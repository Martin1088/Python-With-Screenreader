from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
#from sqlite3 import *
from datetime import datetime

app = Flask(__name__)
#app.config.from_pyfile('config.cfg')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#app.app_context().push()

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(300), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    postcode = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    solds = db.relationship('Sold', backref='customer')

sold_product = db.Table('sold_product',
        db.Column('sold_id', db.Integer, db.ForeignKey('sold.id', primary_key=True)), 
        db.Column('product_id', db.Integer, db.ForeignKey('product.id', primary_key=True)),
        )

class Sold(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sold_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    shipped_date = db.Column(db.DateTime)
    delivered_date = db.Column(db.DateTime)
    coupon_code = db.Column(db.String(30))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    products = db.relationship('Product', secondary=sold_product)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True, port = 5000)

