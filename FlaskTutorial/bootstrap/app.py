from flask import Flask, render_template, g, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)

