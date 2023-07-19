
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>This is my Python start!</h1>'

@app.route('/home' , methods=['POST', 'GET'], defaults={'name' : 'Default'} )
@app.route('/home/<string:name>', methods=['POST' , 'GET'] )
def home(name):
    return 'Hello, Iam {} . You are in my space!'.format(name)

@app.route('/json')
def json():
    return jsonify({'Einkaufsliste' : ["Bananen", "Butter", "Brot"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
