import pprint
from pymongo import MongoClient
from flask import Flask, render_template, request, json, jsonify
from config import *
app = Flask(__name__, static_folder='static', template_folder='static')

client = MongoClient(db_conn)
db = client['blogger']
logins = db.datas
from views import *
if __name__ == "__main__":
    app.run(debug=True)
