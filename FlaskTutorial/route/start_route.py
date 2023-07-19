from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>Hello</h2>'

@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return 'You are from {}. {} Welcome to this page'.format(location, name)

@app.route('/webform' )
def webform():
    return '''<form method="POST" action="/process">
                <input type="text"  name="name" title="name" >
                <input type="text"  name="location" title="Location" >
                <input type="submit"  name="submit" title="Please dend" value="submit">
              </form>
            '''

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    return 'Hi {}. You have submited for the {} comunity.'.format(name, location)

@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()
    name = data['name']
    location = data['location']
    randomlist = data['randomlist']
    return jsonify({'request' : 'Success', 'name' : name, 'location' : location , 'randomlist' : randomlist })

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)

