from os import name
from flask import Flask
app = Flask(__name__)
@app.route('/') 
def index():
    return ('<h1>Hallo Flask! </h1>')
@app.route('/hello/<name>') 
def hello(name):
    return ('<h1>Hallo ' + name + '</h1>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
