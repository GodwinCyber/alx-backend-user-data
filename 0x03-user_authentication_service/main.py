#!/usr/bin/env python3
"""End-to-end integration test Module"""

import requests

url = "http://localhost:5000"
EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


def register_user(email: str, password: str) -> None:
    """Create function for this task to use the requests module to
       query your web server for the corresponding end-point.
       Use assert to validate the response’s expected
       status code and payload (if any) for each task.
    """
    payload = {"email": email, "password": password}
    response = requests.post(url + "/users", data=payload)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Create function for this task to use the requests module to log in
       with the wrong password.
    """
    payload = {"email": email, "password": password}
    response = requests.post(url + "/sessions", data=payload)
    assert response.status_code == 401
    assert response.json() == {"message": "Unauthorized"}


def log_in(email: str, password: str) -> str:
    """Create function for this task to use the requests module to
       log in correctly and return the session ID.
    """
    payload = {"email": email, "password": password}
    response = requests.post(url + "/sessions", data=payload)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "logged in"}
    return response.cookies.get("session_id")


def profile_unlogged() -> None:
    """Create function for this task to use the requests module to check
       the profile without being logged in.
    """
    response = requests.get(url + "/profile")
    assert response.status_code == 403
    assert response.json() == {"message": "Forbidden"}


def profile_logged(session_id: str) -> None:
    """Create function for this task to use the requests module to check
       the profile while being logged in.
    """
    cookies = {"session_id": session_id}
    response = requests.get(url + "/profile", cookies=cookies)
    assert response.status_code == 200
    assert "email" in response.json()


def log_out(session_id: str) -> None:
    """Create function for this task to use the requests module to log out."""
    cookies = {"session_id": session_id}
    response = requests.delete(url + "/sessions", cookies=cookies)
    assert response.status_code == 200
    assert response.json() == {"message": "Successfully logged out"}


def reset_password_token(email: str) -> str:
    """Create function for this task to use the requests module to request
       a password reset token.
    """
    payload = {"email": email}
    response = requests.post(url + "/reset_password", data=payload)
    assert response.status_code == 200
    assert "reset_token" in response.json()
    return response.json()["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Create function for this task to use the requests module to update
       the password.
    """
    payload = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password
    }
    response = requests.put(url + "/reset_password", data=payload)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "Password updated"}


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
