# from sqlite3 import *

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def getdb(app):
    db.init_app(app)
    with app.app_context():
        db.drop_all()
        db.create_all()
        return db


class Department(db.Model):
    __tablename__ = "department"
    dep_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dep_name = db.Column(db.String(100))
    dep_location = db.Column(db.String(100))
    dep_employee = db.relationship(
        "Employee", back_populates="emp_department", lazy=True
    )


class Employee(db.Model):
    __tabelname__ = "employee"
    emp_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    emp_name = db.Column(db.String(100), nullable=False)
    emp_salary = db.Column(db.Integer)
    emp_dept_id = db.Column(db.Integer, db.ForeignKey("department.dep_id"))
    emp_department = db.relationship(
        "Department", back_populates="dep_employee", lazy=True
    )

    def __init__(self, name):
        self.emp_name = name
