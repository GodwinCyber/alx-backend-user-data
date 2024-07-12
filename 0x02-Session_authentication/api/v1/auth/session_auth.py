#!/usr/bin/env python3
"""Module for session Auth"""

from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """Session Auth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id:
            Creates a Session ID for a user_id:
        Return:
            Return None if user_id is None
            Return None if user_id is not a string
        Otherwise:
            Generate a Session ID using uuid module and uuid4()
            like id in Base Use this Session ID as key of the
            dictionary user_id_by_session_id - the value for
            this key must be user_id Return the Session ID
            The same user_id can have multiple Session ID - indeed,
            the user_id is the value in the dictionary user_id_by_session_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns the user_id associated with a session_id:
        Returns a User ID based on a Session ID:
            Return None if session_id is None
            Return None if session_id is not a string
            Return the value (the User ID) for the key session_id in
            the dictionary user_id_by_session_id.
            You must use .get() built-in for accessing in a
            dictionary a value based on key
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Returns a User instance based on a cookie:
            (overload) that returns a User instance
            based on a cookie value: You must use
            self.session_cookie(...) and self.user_id_for_session_id(...)
        Return:
            return the User ID based on the cookie _my_session_id
        Note:
            By using this User ID, you will be able to retrieve a
            User instance from the database - you can use User.get(...)
            for retrieving a User from the database.
        """
        session_id = self.session_cookie(request)
        if session_id is None:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        return User.get(user_id)
