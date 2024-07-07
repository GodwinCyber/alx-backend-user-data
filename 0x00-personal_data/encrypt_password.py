#!/usr/bin/env python3
"""Module  Encrypting passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    """mplement a hash_password function that expects one string
        argument name password and returns a salted, hashed password,
        which is a byte string.
        Use the bcrypt package to perform the hashing (with hashpw).
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
