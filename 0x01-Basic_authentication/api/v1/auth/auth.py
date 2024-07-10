#!/usr/bin/env python3
"""Module Auth"""

from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method def require_auth(self, path: str, excluded_paths:
            List[str]) -> bool: that
            False - path and excluded_paths will be used later, now, you
            don’t need to take care of them
        Return:
            Returns True if path is None
            Returns True if excluded_paths is None or empty
            Returns False if path is in excluded_paths
        Cases:
            You can assume excluded_paths contains string path always
            ending by a / This method must be slash t lerant:
            path=/api/v1/status and path=/api/v1/status/ must be
            returned False if excluded_paths contains /api/v1/status/
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if not path.endswith('/'):
            path += '/'
        for excluded_path in excluded_paths:
            if excluded_path.endswith('/') and path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """public method def authorization_header(self, request=None) -> str:
            If request is None, returns None
            If request doesn’t contain the header key Authorization, returns
            None
            Otherwise, return the value of the header request Authorization
        Returns:
            tNone - request will be the Flask request object
        """
        if request is None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """public method def current_user(self, request=None) ->
            TypeVar('User'):
        Returns:
            None - request will be the Flask request object
        """
        return None
