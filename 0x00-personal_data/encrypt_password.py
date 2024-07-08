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


def is_valid(hash_password: bytes, password: str) -> bool:
    """implement a is_valid function that expects two arguments:
    Args:
        hashed_password: bytes type
        password: string type
        bcrypt to validate that the provided password
        matches the hashed password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hash_password)
