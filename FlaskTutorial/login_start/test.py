from flask import Flask
from flask_login import LoginManager, UserMixin, login_user, login_required   
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_pyfile('config.cfg')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'
login_manager = LoginManager(app)
db = SQLAlchemy(app)
app.app_context().push()

class Member(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True )
    #password = db.Column(db.String(30))
    #email = db.Column(db.String(50))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login')
def login():
    user = Member.query.filter_by(username = 'Merlin').first()
    login_user(user)
    return '<hi> Your are logged in! </h1>'

@app.route('/profile')
@login_required
def profile():
    return '<h1> Qour profile </h1>'



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
