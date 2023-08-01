from flask import Flask, render_template, g, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

def connect_db():
    sql = sqlite3.connect('food_log.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/', methods=['POST', 'GET'])
def index():
    db = get_db()
    if request.method == 'POST':
        date = request.form['date'] # always in YYY-MM-DD
        dt = datetime.strptime(date, '%Y-%m-%d')
        db_date = datetime.strftime(dt, '%Y%m%d')
        db.execute('insert into log_date (entry_date) values(?)', [db_date])
        db.commit()
        # show entreis
    cur = db.execute('select entry_date from log_date order by entry_date desc')
    results = cur.fetchall()
    # pretty the format
    results_d = []
    for i in results:
        s_date = {}
        s_date['n_date'] = i['entry_date']
        d = datetime.strptime( str(i['entry_date']), '%Y%m%d')
        s_date['s_date'] = datetime.strftime(d, '%B %d, %Y')
        results_d.append(s_date)
    return render_template('home.html', results_d = results_d)

@app.route('/view/<date>', methods=['GET', 'POST'] ) # get date 20230220
def view(date):
    db = get_db()
    log_cur = db.execute('select id, entry_date from log_date Where entry_date =?', [date])
    date_result = log_cur.fetchone()
    # insert the food with the date
    if request.method == 'POST':
        db.execute('insert into food_date(food_id, log_date_id) values(?,?)', [request.form['food-select'], date_result['id']])
        db.commit()
    d = datetime.strptime( str(date_result['entry_date']), '%Y%m%d')
    s_date = datetime.strftime(d, '%B %d, %Y')
    # option list data = list of foods avalible 
    food_cur = db.execute('select id, name from food')
    food_results = food_cur.fetchall()
    # join on food_date get fod and log_date together
    join_cur = db.execute('select food.name, food.protein, food.carbohydrates, food.fat, food.calories \
            from log_date join food_date on food_date.log_date_id = log_date.id join food on food.id = food_date.food_id \
            where log_date.entry_date = ?', [date])
    join_results = join_cur.fetchall()
    # make the total of the entry
    total = {}
    total['protein'] = 0
    total['carbohydrates'] = 0
    total['fat'] = 0
    total['calories'] = 0
    for i in join_results:
        total['protein'] += i['protein']
        total['carbohydrates'] += i['carbohydrates']
        total['fat'] += i['fat']
        total['calories'] += i['calories']

    return render_template('day.html', entry_date = date_result['entry_date'], s_date = s_date, food_results = food_results, join_resuls = join_results, total = total)

@app.route('/food', methods=['GET', 'POST'] )
def food(): 
    db = get_db()
    if request.method == 'POST':
        name = request.form['food-name']
        protein = int(request.form['protein'])
        carbohydrates = int(request.form['carbohydrates'])
        fat = int(request.form['fat'])
        calories = protein * 4 + fat * 9
        # database init
        db.execute('insert into food(name, protein, carbohydrates, fat, calories) values (?, ?, ?, ?, ?)',\
                [name, protein, carbohydrates, fat, calories])
        db.commit()

    # view entries
    cur = db.execute('select name, protein, carbohydrates, fat, calories from food')
    results = cur.fetchall()
    return render_template('add_food.html', results = results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
