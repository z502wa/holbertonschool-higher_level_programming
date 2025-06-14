#!/usr/bin/python3
# 10675@holbertonstudents.com
# Suhail Alaboud
"""
Module: task_05_basic_security
Basic and JWT authentication for Flask API.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory user store with hashed passwords and roles
users = {
    'user1': {
        'username': 'user1',
        'password': generate_password_hash('password'),
        'role': 'user'
    },
    'admin1': {
        'username': 'admin1',
        'password': generate_password_hash('password'),
        'role': 'admin'
    }
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return False
    return True

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return 'Basic Auth: Access Granted'

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'error': 'Invalid credentials'}), 401
    token = create_access_token(
        identity={'username': username, 'role': user['role']}
    )
    return jsonify(access_token=token)

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return 'JWT Auth: Access Granted'

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    identity = get_jwt_identity()
    if identity.get('role') != 'admin':
        return jsonify({'error': 'Admin access required'}), 403
    return 'Admin Access: Granted'

# JWT error handlers
@jwt.unauthorized_loader
def missing_token(err):
    return jsonify({'error': 'Missing or invalid token'}), 401

@jwt.invalid_token_loader
def invalid_token(err):
    return jsonify({'error': 'Invalid token'}), 401

@jwt.expired_token_loader
def expired_token(err):
    return jsonify({'error': 'Token has expired'}), 401

@jwt.needs_fresh_token_loader
def fresh_token(err):
    return jsonify({'error': 'Fresh token required'}), 401

if __name__ == '__main__':
    app.run()
