from flask import Flask
from flask_mail import Mail, Message 


app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = ''


mail = Mail(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    msg = Message('Halloa',
            recipients=['']
            ) 
    mail.send(msg)
    return '<h1>Send</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
