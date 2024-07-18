#!/usr/bin/env python3
"""Auth Module"""

import bcrypt
from user import User, Base
from db import DB
from uuid import uuid4
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


def _generate_uuid() -> str:
    """Generate a UUID4: implement a _generate_uuid function in the auth
        module. The function should return a string representation of a
        new UUID. Use the uuid module.
    """
    UUID = uuid4()
    return str(UUID)


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
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password.decode('utf-8'))
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validates a login attempt: In this task, you will implement the
            Auth.valid_login method. It should expect email and password
            required arguments and return a boolean.
            Try locating the user by email. If it exists, check the password
            with bcrypt.checkpw. If it matches return True.
            In any other case, return False
        """
        if email is None or password is None:
            return False
        try:
            user = self._db.find_user_by(email=email)
            valid = bcrypt.checkpw(
                password.encode('utf-8'), user.hashed_password.encode('utf-8')
            )
            return valid
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Creates a session: In this task, you will implement the
            Auth.create_session method:
        Args:
            It will take email string argumnent and return
            session ID as string.
        Note:
            The method should find the user corresponding to the mail,
            generate a new UUID and store it in the database as user's
            session_id, and return the session ID.
        Remember:
            Only public method of self._db can be used.
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User or None:
        """Gets user from session ID: In this task, you will implement the:
            the Auth.get_user_from_session_id method. It take a single
            session_id string argument and return the corresponding
            User or None.
        Cases:
            if the session ID is None or no user is found, return None, else
            return the corresponding user
        Note:
            Only use public methods of self._db
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroys a session: In this task, you will implement the:
            The method updates the corresponding user's session ID to None
        Note:
            Only use public methods of self._db
        """
        self._db.update_user(user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """Gets reset password token: In this task, you will implement the:
            get_reset_password_token that take an email string argument
            and return string
        Case:
            Find the user corresponding to the email. if the user
            does not exist raise ValueError exception. If it exist, generate
            UUID and update the user's reset_token database field. Return token
        """
        try:
            user = self._db.find_user_by(email=email)
            token = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return token
        except NoResultFound:
            raise ValueError("User not found")

    def update_password(self, reset_token: str, password: str) -> None:
        """Updates password: In this task, you will implement the:
            Implement Auth.update_password method. It takes reset_token
            string argumnent and a password string argument and return None
        Args:
            The reset_token to find the corresponding user. If it does not
            exist, raise a ValueError exception. Else hash the password and
            update the user's hashed_password field with the new hashed
            password and the reset_token field to None.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(
                user.id, hashed_password=hashed_password.decode(
                    'utf-8'
                ), reset_token=None
            )
        except NoResultFound:
            raise ValueError
        return None
