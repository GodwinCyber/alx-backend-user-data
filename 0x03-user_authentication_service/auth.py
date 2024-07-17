#!/usr/bin/env python3
"""Auth Module"""

import bcrypt
from user import User, Base
from db import DB


def _hash_password(password: str) -> bytes:
    """Hashes a password: efine a _hash_password method that'
        takes in a password string arguments and returns bytes.
    Return:
        The bytes salted input password hashd with bcrypt.hashpw
    """
    if password is None or password == "":
        raise ValueError("Password cannot be empty")
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
