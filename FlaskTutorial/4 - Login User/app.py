from flask import Flask 
from flask_login import LoginManager, UserMixin, login_required, login_user
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    login_manager.init_app(app)
    db.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/profile')
    @login_required
    def profile():
        return '<h1>You are in the profile.</h1>'

    @app.route('/login')
    def login():
        user = User.query.filter_by(username='Anthony').first()
        login_user(user)
        return '<h1>You are now logged in!</h1>'

    return app