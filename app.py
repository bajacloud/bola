from flask import Flask, request, jsonify, abort, render_template, redirect, url_for

app = Flask(__name__)

# Mock database
data = {
    1: {"user_id": 1, "name": "Alice", "balance": 1000},
    2: {"user_id": 2, "name": "Bob", "balance": 1500},
    3: {"user_id": 3, "name": "Charlie", "balance": 2000}
}

@app.route('/')
def index():
    return redirect(url_for('login_page'))

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        user_id = int(request.form.get('user_id'))
        if user_id in data:
            return redirect(url_for('account_page', user_id=user_id))
        return abort(401)
    return render_template('login.html')

@app.route('/account/<int:user_id>', methods=['GET'])
def account_page(user_id):
    if user_id in data:
        user_data = data[user_id]
        return render_template('account.html', name=user_data['name'], balance=user_data['balance'])
    return abort(404)

# Vulnerable endpoint for demonstration
@app.route('/api/account/<int:user_id>', methods=['GET'])
def get_account(user_id):
    if user_id in data:
        return jsonify(data[user_id])
    return abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
