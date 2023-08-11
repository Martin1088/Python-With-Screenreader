from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True, port = 5000)

