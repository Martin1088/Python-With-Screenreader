from flask import Flask, render_template, g, request, session, redirect, url_for 
from database import *
from werkzeug.security import generate_password_hash, check_password_hash
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

# function for the user
def get_current_user():
    user_result = None 
    db = get_db()
    if 'user' in session:
        user = session['user']
        user_cur = db.execute('select id, name, password, expert, admin from users where name = ?', [user])
        user_result = user_cur.fetchone()
    return user_result 


@app.route('/')
def index():
    user = get_current_user()
    return render_template('home.html', user = user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    db = get_db()
    user = get_current_user()
    if request.method == 'POST':
        hash_password = generate_password_hash(request.form['password'], method='sha256')
        db.execute('insert into users(name, password) values (?, ?)', [request.form['name'], hash_password])
        db.commit()
        session['user'] = request.form['name']
        return redirect(url_for('index'))
    return render_template('register.html', user = user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    db = get_db()
    user = get_current_user()
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user_cur = db.execute('select id, name, password from users where name = ?', [name])
        user_result = user_cur.fetchone()
        if check_password_hash(user_result['password'], password ):
            session['user'] = user_result['name']
            return redirect(url_for('index'))
        else:
            return 'False'
    return render_template('login.html', user = user)

@app.route('/question')
def question():

    user = get_current_user()
    return render_template('question.html', user = user)

@app.route('/answer')
def answer():
    user = get_current_user()
    return render_template('answer.html', user = user)


@app.route('/ask', methods=['GET', 'POST'])
def ask():
    user = get_current_user()
    db = get_db()
    if request.method == 'POST':
        db.execute('insert into questions (question_text, asked_by_id, expwer_id) values (`, ?, ?)', \
                [request.form['question'], user['id'], request.form['expert'] ])

    # experten overview
    expert_cur = db.execute('select id, name from users where expert = 1')
    expert_results = expert_cur.fetchall() 
    return render_template('ask.html', user = user, expert_results = expert_results )

@app.route('/unanswered')
def unanswered():
    user = get_current_user()
    return render_template('unanswered.html', user = user)

@app.route('/users')
def users():
    user = get_current_user()
    db = get_db()
    user_cur = db.execute('select id, name, expert, admin from users ')
    users_result = user_cur.fetchall()

    return render_template('users.html', user = user, users_result = users_result)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/promote/<user>')
def promote(user):
    db = get_db()
    db.execute('update users set expert = 1 where id = ?', [user])
    db.commit()
    return redirect(url_for('users'))


if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True, port = 5000)
