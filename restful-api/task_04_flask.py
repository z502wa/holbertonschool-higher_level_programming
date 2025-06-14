#!/usr/bin/python3
# 10675@holbertonstudents.com
# Suhail Alaboud
"""
Module: task_04_flask
Simple REST API implemented with Flask.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users: username -> user data
users = {}


@app.route("/", methods=["GET"])
def home():
    """
    Root endpoint returns a welcome message.
    """
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_usernames():
    """
    Return a JSON list of all usernames.
    """
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """
    Return API status.
    """
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    Return user data for a given username or error if not found.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user from JSON payload.
    Payload must include 'username'.
    """
    data = request.get_json() or {}
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    user = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }
    users[username] = user
    return jsonify({"message": "User added", "user": user}), 201


if __name__ == "__main__":
    app.run()
