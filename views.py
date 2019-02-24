from app import app, Flask, json, jsonify, request
from app import logins


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
    gmail_id = data['gmail_id']
    username = data['username']
    password = data['password']
    dataie = {"gmail_id": gmail_id, "username": username, "password": password}
    logins.insert_one(dataie)
    return jsonify({"message": "user registered successfully"})
