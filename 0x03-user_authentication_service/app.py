#!/usr/bin/env python3
"""Flask Module"""

from flask import Flask, jsonify, request, abort, make_response
from auth import Auth

AUTH = Auth()

app = Flask(__name__)


@app.route("/")
def hello():
    """Hello World"""
    message = {"message": "Bienvenue"}
    return jsonify(message)


@app.route("/users", methods=['POST'])
def register_users():
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


@app.route("/sessions", methods=['POST'])
def login() -> str:
    """Login a user: The end-point should expect two form data:
    Args:
        The request is expected to contain form data with email
        and a password fields
    Cases:
        If the login information is incorrect, use flask.abort
        to respond with a 401 HTTP status
        else, create a new session for the user, store the
        session ID as a cookie with key "session_id" on the
        response and return a JSON payload of the form
        {"email": "email", "message": "logged in"}
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        return jsonify({"message": "email and password required"}), 400
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


@app.route("/sessions", methods=['DELETE'])
def logout() -> str:
    """Logout a user: The end-point should expect a cookie:
        Implement logout function to respond to the DElETE /sessions route
    Args:
        The request is expected to contain sesssion
        ID as cookie with key "session_id"
    Cases:
        find the user with requested session ID. If th user exist, destroy
        the session and redirect the user to GET /. If user does not
        exist, respond with a 403 HTTP status
    """
    session_id = request.cookies.get("session_id")
    if not session_id:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    AUTH.destroy_session(user_id)
    return redirect("/")
