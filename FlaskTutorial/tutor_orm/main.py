from flask import Flask
from model import Department, Employee, db, getdb

app = Flask(__name__)
# app.config.from_pyfile('config.cfg')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# db = getdb(app)

with app.app_context():
    db.drop_all()
    db.create_all()
    # Beispiele
    d1 = Department()
    d1.dep_name = "Entwicklung"
    d1.dep_location = "Wiesloch"
    db.session.add(d1)
    db.session.commit()
    # deparment testen
    d1 = Department.query.filter_by(dep_name="Entwicklung").first()
    d1.dep_location = "Frankfurt"
    db.session.commit()
    # Employee
    e1 = Employee("Elsa")
    e1.emp_salary = 5000
    e1.emp_department = d1
    e2 = Employee("Tim")
    e1.emp_salary = 10000
    e1.emp_department = d1
    db.session.add_all([e1, e2])
    db.session.commit()
