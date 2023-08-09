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
    if not user:
        return redirect(url_for('login'))

    db = get_db()
    question_cur = db.execute('select questions.id as question_id, questions.question_text, u.name as u_name, e.name as e_name  \
            from questions join users as u on u.id = questions.asked_by_id join users as e on e.id = questions.expert_id \
            where questions.answer_text is not null' )
    questions = question_cur.fetchall()


    return render_template('home.html', user = user, questions = questions )

@app.route('/register', methods=['GET', 'POST'])
def register():
    db = get_db()
    user = get_current_user()
    if request.method == 'POST':
        name = request.form['name']
        existing_cur = db.execute('select id from users where name = ?', [name] )
        existing_user = existing_cur.fetchone()
        if existing_user:
            return render_template('register.html', user = user, error = 'This user exists!')
        # password insert and register
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
    error = None
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user_cur = db.execute('select id, name, password from users where name = ?', [name])
        user_result = user_cur.fetchone()
        if user_result: 
            if check_password_hash(user_result['password'], password ):
                session['user'] = user_result['name']
                return redirect(url_for('index'))
            else:
                error = 'There went something wrong'
        else:
            error = 'There went something wrong'

    return render_template('login.html', user = user, error = error)

@app.route('/question/<question_id>')
def question(question_id):
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    db = get_db()
    question_cur = db.execute('select questions.answer_text, questions.question_text, u.name as u_name, e.name as e_name  \
            from questions join users as u on u.id = questions.asked_by_id join users as e on e.id = questions.expert_id \
            where questions.id = ? ', [question_id] )
    question = question_cur.fetchone()
    return render_template('question.html', user = user, question = question)

@app.route('/answer/<question_id>', methods=['GET', 'POST' ])
def answer(question_id):
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    if user['expert'] == 0:
        return redirect(url_for('login'))

    db = get_db()
    if request.method == 'POST':
        answer = request.form['answer']
        db.execute('update questions set answer_text = ? where id = ?', [answer, question_id] )
        db.commit()
        #return '{} {}'.format(answer, question_id) 
        return redirect(url_for('unanswered'))

    question_cur = db.execute('select id ,question_text from questions where id = ?', [question_id])
    question = question_cur.fetchone()

    return render_template('answer.html', user = user, question = question)


@app.route('/ask', methods=['GET', 'POST'])
def ask():
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    db = get_db()
    if request.method == 'POST':
        db.execute('insert into questions (question_text, asked_by_id, expert_id) values (?, ?, ?)', \
                [request.form['question'], user['id'], request.form['expert'] ])
        db.commit()
        #return 'Q: {}, ID: {}, Exp: {}'.format(request.form['question'], user['id'], request.form['expert'] )
        return redirect(url_for('index'))
    # experten overview
    expert_cur = db.execute('select id, name from users where expert = 1')
    expert_results = expert_cur.fetchall() 
    return render_template('ask.html', user = user, expert_results = expert_results )

@app.route('/unanswered')
def unanswered():
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    if user['expert'] == 0:
        return redirect(url_for('login'))

    db = get_db()
    question_cur = db.execute('select questions.id, questions.question_text, questions.answer_text, users.name \
            from questions join users on users.id = questions.asked_by_id  \
            where questions.answer_text is null and questions.expert_id = ?', [user['id']])
    questions = question_cur.fetchall()

    return render_template('unanswered.html', user = user, questions = questions)

@app.route('/users')
def users():
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    if user['admin'] == 0:
        return redirect(url_for('login'))
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
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
    if user['admin'] == 0:
        return redirect(url_for('login'))

    db = get_db()
    db.execute('update users set expert = 1 where id = ?', [user])
    db.commit()
    return redirect(url_for('users'))


if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True, port = 5000)
