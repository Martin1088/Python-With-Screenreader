from flask import Flask, render_template, url_for, request, redirect 
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user  
from flask_sqlalchemy import SQLAlchemy
from sqlite3 import *
#from dotenv import load_dotenv 


#load_dotenv('.flaskenv')
login_manager = LoginManager()
db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True )
    #password = db.Column(db.String(30))
    #email = db.Column(db.String(50))

def create_app():
    app = Flask(__name__)
    #app.config.from_pyfile('config.cfg')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db-login.sqlite3' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secret'
    login_manager.init_app(app)
    db.init_app(app)
    login_manager.login_view = 'login'
    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/login', methods=['POST', 'GET'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username')
            user = User.query.filter_by(username = username).first()
            if not user:
                return 'Not load_user'
            login_user(user)
            return '<h2>Your login</h2>'
        return render_template('login.html') 

    @app.route('/profile')
    @login_required
    def profile():
        return f'<h1> Qour profile {current_user.username} </h1>'

    @app.route('/logout')
    @login_required 
    def logout():
        logout_user()
        return 'Logout'

    
    return app

