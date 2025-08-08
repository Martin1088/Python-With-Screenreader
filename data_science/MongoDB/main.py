from flask import Flask, Response
from pymongo import MongoClient
from bson.json_util import dumps


app = Flask('__name__')

#connection to mongoDB
client= MongoClient('')

db = client.schuleDB #Name der Datenbank
serien = db.serien #Name der Collection


@app.route("/")
def index():
    return ('<h1> Eine REST - Schnitstelle für Mongo-DB </h1>')

@app.route("/all")
def readall():
    cursor = serien.find()
    json_data = dumps(list(cursor))
    return Response(json_data, mimetype='text/json')

@app.route("/one/<title>")
def readone():
    cursor = serien.find({"title": title})
    json_data = dumps(list(cursor))
    return Response(json_data, mimetype='text/json')
app.run(host='0.0.0.0', port=9020, debug=True)
