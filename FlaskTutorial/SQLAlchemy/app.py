from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)
app.app_context().push()

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(300), nullable=False)
    postcode = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    solds = db.Relationship('Sold', backref='customer')

class Sold(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sold_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    shipped_date = db.Column(db.DateTime)
    delivered_date = db.Column(db.DateTime)
    coupon_code = db.Column(db.String(30))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

sold_product = db.Table('sold_product',
        db.Column(),
        db.Column())

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True, port = 5000)

