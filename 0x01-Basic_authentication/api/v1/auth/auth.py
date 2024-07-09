#!/usr/bin/env python3
"""Module Auth"""

from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method def require_auth(self, path: str, excluded_paths:
            List[str]) -> bool: that
        Returns:
            False - path and excluded_paths will be used later, now, you
            don’t need to take care of them
        """
        return False

    def authorization_header(self, request=None) -> str:
        """public method def authorization_header(self, request=None) -> str:
        Returns:
            tNone - request will be the Flask request object
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """public method def current_user(self, request=None) ->
            TypeVar('User'):
        Returns:
            None - request will be the Flask request object
        """
        return None
