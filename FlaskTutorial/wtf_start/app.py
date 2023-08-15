from flask import Flask, render_template, g, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, Form, FormField, FieldList    
from wtforms.validators import InputRequired, Length, AnyOf, Email  

class TelephoneField(Form):
    country_code = IntegerField('cuntry code') 
    area_code = IntegerField('area code') 
    number = StringField('number')

class YearForm(Form):
    year = IntegerField('year')
    total = IntegerField('total')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[
        InputRequired(),
        Length(min=5, max=15)
        ])
    password = PasswordField('password', validators=[
        InputRequired(),
        AnyOf(values=['secret', 'password'])
        ])
    email = StringField('email', validators=[Email()])
    age = IntegerField('age')
    yesno = BooleanField('Datenschutz')
    home_phone = FormField(TelephoneField)
    mobile_phone = FormField(TelephoneField)
    years = FieldList(FormField(YearForm), min_entries=3) 

class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route('/', methods = ['GET', 'POST'])
def index():
    user = User('Merlin', 'frech@freh.com', 15)
    form = LoginForm(obj=user)
    if form.validate_on_submit():
        return f'<h>Username: {form.username.data} , Password: {form.password.data} </h>'

    return render_template('index.html', form = form )


if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True, port = 5000)

