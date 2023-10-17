from flask import Flask
from comment_handler import comments_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'
# @app.route('/') 
# def index():
    # return ('hallo')
app.register_blueprint(comments_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

