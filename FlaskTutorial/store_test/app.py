from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage 


db = SQLAlchemy()

## Product

def create_app():
    app = Flask(__name__)
    #app.config.from_pyfile('config.cfg')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trendy.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secret'
    db.init_app(app)
    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/product')
    def product():
        return render_template('view-product.html')

    @app.route('/cart')
    def cart():
        return render_template('cart.html')

    @app.route('/checkout')
    def checkout():
        return render_template('checkout.html')

    @app.route('/admin')
    def admin():
        return render_template('admin/index.html', admin=True)

    @app.route('/admin/add')
    def add():
        return render_template('admin/add-product.html', admin=True)

    @app.route('/admin/order')
    def order():
        return render_template('admin/view-order.html', admin=True)
    return app


