from flask import Flask, render_template, url_for, request, redirect
from flask_socketio import SocketIO 


app = Flask(__name__)
#app.config.from_pyfile('config.cfg')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db-login.sqlite3' 
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)



if __name__ == '__main__':
    socketio.run(app)
    
