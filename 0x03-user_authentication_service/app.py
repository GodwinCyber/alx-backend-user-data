#!/usr/bin/env python3
"""Flask Module"""

from flask import Flask, jsonify, request
from auth import Auth

AUTH = Auth()

app = Flask(__name__)


@app.route("/")
def hello():
    """Hello World"""
    message = {"message": "Bienvenue"}
    return jsonify(message)


@app.route("/users", methods=['POST'])
def users():
    """Register a user: The end-point should expect two form data
        fields: "email" and "password". If the user does not exist,
        the end-point should register it and respond
        with the following JSON payload:
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        return jsonify({"message": "email and password required"}), 400
    try:
        user_id = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError as ve:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
