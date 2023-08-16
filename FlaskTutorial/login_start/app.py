from flask import Flask
from flask_login import LoginManager, UserMixin, login_user, login_required  
from flask_sqlalchemy import SQLAlchemy
from sqlite3 import *
from dotenv import load_dotenv 


login_manager = LoginManager()
db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True )
    password = db.Column(db.String(30))
    email = db.Column(db.String(50))

def create_app():
    load_dotenv()
    app = Flask(__name__)
    #app.config.from_pyfile('config.cfg')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secret'
    login_manager.init_app(app)
    db.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/login')
    def login():
        user = User.query.filter_by(username = 'Merlin').first()
        login_user(user)
        return '<hi> Your are logged in! </h1>'

    @app.route('/profile')
    @login_required
    def profile():
        return '<h1> Qour profile </h1>'

    return app

