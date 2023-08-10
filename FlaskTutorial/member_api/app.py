from flask import Flask, render_template, g, request, session, redirect, url_for, jsonify
from database import *
from functools import wraps


# Auth test
api_user = 'admin'
api_password = 'secret'

def protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == api_user and auth.password == api_password:
            return f(*args, **kwargs)

        return jsonify({ 'message' : 'Error'}), 403
    return decorated

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/member', methods=['GET'])
@protected
def get_members():
    db = get_db()
    member_cur = db.execute('select * from members')
    results = member_cur.fetchall()
    m_values = []
    for result in results:
        dict = {}
        dict['id'] = result['id'] 
        dict['name'] = result['name'] 
        dict['email'] = result['email'] 
        dict['level'] = result['level'] 
        m_values.append(dict)
    
    return jsonify({ 'members' : m_values })

@app.route('/member/<int:member_id>', methods=['GET'])
@protected
def get_member(member_id):
    db = get_db()
    member_cur = db.execute('select * from members where id = ?', [member_id])
    result = member_cur.fetchone()
    return jsonify({ 'member' : \
            {'id' : result['id'], 'name' : result['name'], 'email' : result['email']} \
            })

@app.route('/member', methods=['POST'])
@protected
def add_member():
    member_data = request.get_json()
    name = member_data['name']
    email = member_data['email']
    level = member_data['level']
    db = get_db()
    db.execute('insert into members (name, email, level) values (?, ?, ?)', [name, email, level])
    db.commit()
    # output as success
    member_cur = db.execute('select * from members where name = ?', [name])
    result = member_cur.fetchone()
    return jsonify({ 'member' : \
            {'id' : result['id'], 'name' : result['name'], 'email' : result['email']} \
            })
    #return "Add member {}, {}, {}".format(name, email, level)

@app.route('/member/<int:member_id>', methods=['PUT', 'PATCH'])
@protected
def edit_member(member_id):
    db = get_db()
    member_data = request.get_json()
    name = member_data['name']
    email = member_data['email']
    level = member_data['level']
    db.execute('update members set name = ?, email = ?, level = ? where id = ? ', \
            [name, email, level, member_id] )
    db.commit()
    # show new data 
    member_cur = db.execute('select * from members where id = ?', [member_id])
    result = member_cur.fetchone()
    return jsonify({ 'member' : \
            {'id' : result['id'], 'name' : result['name'], 'email' : result['email']} \
            })

@app.route('/member/<int:member_id>', methods=['DELETE'])
@protected
def delete_member(member_id):
    db = get_db()
    db.execute('delete from members where id = ?', [member_id])
    db.commit()
    return jsonify({ 'message' : 'has been deleted' })


if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True, port = 5000)

