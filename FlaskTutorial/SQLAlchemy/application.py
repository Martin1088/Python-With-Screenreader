from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)
app.app_context().push()

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True )
    password = db.Column(db.String(30))
    email = db.Column(db.String(50))
    join_date = db.Column(db.DateTime)

    bookings = db.relationship('Booking', backref='member', lazy='dynamic')
    courses =  db.relationship('Course', secondary='user_courses' , backref='member', lazy='dynamic')


    def __repr__(self):
        return '<Member %r>' % self.username


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(50))
    price = db.Column(db.Integer)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))

    def __repr__(self):
        return '<Booking %r>' % self.product

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

db.Table('user_courses',
        db.Column('member_id', db.Integer, db.ForeignKey('member.id')),
        db.Column('sourse_id', db.Integer, db.ForeignKey('course.id'))
        )

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True, port = 5000)

