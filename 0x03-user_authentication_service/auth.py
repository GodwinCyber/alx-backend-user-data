#!/usr/bin/env python3
"""Auth Module"""

import bcrypt
from user import User, Base
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> bytes:
    """Hashes a password: efine a _hash_password method that'
        takes in a password string arguments and returns bytes.
    Return:
        The bytes salted input password hashd with bcrypt.hashpw
    """
    if password is None or password == "":
        raise ValueError("Password cannot be empty")
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a user: define a register_user method that takes in
            Auth.register_user should take mandatory email and password
            string arguments and return a User object.
            If a user already exist with the passed email, raise a ValueError
            with the message User <user's email> already exists.
            If not, hash the password with _hash_password, save the user to
            the database using self._db and return the User object.
        Note:
            Auth._db is a private property and should
            NEVER be used from outside the class.
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed = _hash_password(password)
            user = self._db.add_user(email, password)
            return user