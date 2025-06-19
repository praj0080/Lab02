from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == 'secure123':
        app.logger.info(f"Successful login for user: {username}")
        return jsonify({"message": "Login successful"}), 200
    else:
        app.logger.warning(f"Failed login for user: {username}")
        return jsonify({"message": "Login failed"}), 401

@app.route('/')
def home():
    return "Web App Running", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
