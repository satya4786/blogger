from app import app, Flask, json, jsonify, request
from app import logins
import re

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if logins.find_one({"username": username, "password": password}):

        return jsonify({"message": "login successfully", "username": username})
    else:
        return jsonify({"message": "username or password is not valid"})


@app.route('/signup', methods=['POST'])
def reg():
    data = request.get_json()
    email_id = data['email_id']
    username = data['username']
    password = data['password']
    if len(email_id) > 7:
        if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email_id) != None:
            dataie = {"email_id": email_id, "username": username, "password": password}
            logins.insert_one(dataie)
        else:
            return jsonify({"message": " invalid email id"})
    return jsonify({"message": "user registered successfully"})
