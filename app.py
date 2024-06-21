from flask import Flask, request, jsonify, abort
import json

app = Flask(__name__)

# Mock database
data = {
    1: {"user_id": 1, "name": "Alice", "balance": 1000},
    2: {"user_id": 2, "name": "Bob", "balance": 1500},
    3: {"user_id": 3, "name": "Charlie", "balance": 2000}
}

# Simple login to simulate user authentication
@app.route('/login', methods=['POST'])
def login():
    auth = request.json
    if auth.get('user_id') in data:
        return jsonify({"message": "Login successful", "user_id": auth.get('user_id')})
    return abort(401)

# Vulnerable endpoint
@app.route('/account/<int:user_id>', methods=['GET'])
def get_account(user_id):
    if user_id in data:
        return jsonify(data[user_id])
    return abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)