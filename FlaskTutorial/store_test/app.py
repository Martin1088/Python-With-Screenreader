from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
import os 


ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png', 'gif', 'JPG', 'JPEG'}
db = SQLAlchemy()

## Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    name = db.Column(db.String(50), unique=True )
    price =  db.Column(db.Integer)
    stock = db.Column(db.Integer)
    description = db.Column(db.String(500))
    image = db.Column(db.String(100))

## add Product here
class AddProduct(FlaskForm):
    name = StringField('Name')
    price = IntegerField('Price')
    stock = IntegerField('Stock')
    description = TextAreaField('Description')
    image = FileField('Image')


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.cfg')
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trendy.db'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secret'
    db.init_app(app)
    with app.app_context():
        db.create_all()

    def allowed_file(filename):
        return '.' in filename and \
                filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @app.route('/')
    def index():
        products = Product.query.all()
        ##products.image  
        return render_template('index.html', products = products)

    @app.route('/product/<id>')
    def product(id):
        product = Product.query.filter_by(id=id).first()

        return render_template('view-product.html', product = product )

    @app.route('/cart')
    def cart():
        return render_template('cart.html')

    @app.route('/checkout')
    def checkout():
        return render_template('checkout.html')

    @app.route('/admin')
    def admin():
        products = Product.query.all()
        product_in_stock = Product.query.filter(Product.stock > 0).count()
        return render_template('admin/index.html', admin=True, products = products, \
                product_in_stock = product_in_stock)

    @app.route('/admin/add', methods=['GET', 'POST'])
    def add():
        form = AddProduct()
        ##if form.validate_on_submit():
        if request.method == 'POST':
            print('POSTT')
            name = form.name.data 
            price = form.price.data 
            stock = form.stock.data 
            description = form.description.data
            image_url = None
            if 'image' not in request.files:
                flash('No file')
                print('No File')
                return redirect(request.url)
            image = request.files['image']
            if image.filename == '':
                flash('No selection')
                print('No selection')
                return redirect(request.url)
            if image and allowed_file(image.filename):
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_url = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            new_p = Product(name = name, price = price, stock = stock, description = description, image = image_url)
            db.session.add(new_p)
            db.session.commit()
            return redirect(url_for('admin'))
        return render_template('admin/add-product.html', admin=True, form = form )

    @app.route('/admin/order')
    def order():
        return render_template('admin/view-order.html', admin=True)
    return app


