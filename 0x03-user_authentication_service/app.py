#!/usr/bin/env python3
"""Flask Module"""

from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


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
        AUTH.register_user(email, password)
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

    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route("/profile", methods=['GET'])
def profile() -> str:
    """Get user profile: The end-point should expect a cookie:
        Implement a profile method to respond to the GET /profile route
    Args:
        The request is expected to contain a session_id cookie.
        Use it to find the user. If the user exist, respond with a
        200 HTTP status and the following JSON payload:
        {"email": "<user email>"}
    case:
        If the session ID is invalid or the user does not exist,
        respond with 403 HTTP status
    """
    session_id = request.cookies.get("session_id")
    if not session_id:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    return jsonify({"email": user.email})


@app.route("/reset_password", methods=['POST'])
def get_reset_password() -> str:
    """Get reset password: The end-point should expect a JSON payload:
        implement a get_reset_password method tpo respond to the
        POST /reset_password route
    Args:
        The request ie expected to contain form data with the "email" field
    Case:
        If the email is not registered, respond with a 403 status code. Else
        generate a token and respond with a 200 HTTP status and
        and following JSON payload
        {"email": "<user email>", "reset_token": "<reset token>"}
    """
    email = request.form.get("email")
    if not email:
        abort(400)
    try:
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token}), 200
    except ValueError:
        abort(403)

@app.route("/reset_password", methods=['PUT'])
def update_password() -> str:
    """Update password: The end-point should expect a JSON payload:
        Implement the update_password function in the app module to
        respond to the PUT /reset_password route.
    Args:
        The request is expected to contain form data with fields
        "email", "reset_token" and "new_password". Update the password.
        If the token is invalid, catch the exception and respond
        with a 403 HTTP code. If the token is valid, respond with a
        200 HTTP code and the following JSON payload:
        {"email": "<user email>", "message": "Password updated"}
    """
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    if not email or not reset_token or not new_password:
        abort(400)
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
