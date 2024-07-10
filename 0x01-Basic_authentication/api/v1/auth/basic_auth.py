#!/usr/bin/env python3
"""Module BasicAuth"""

import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class that inherits from Auth"""
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """Extracts base64 authorization header:
            class BasicAuth that returns the Base64 part of the Authorization
            header for a Basic Authentication:
        Return:
            Return None if authorization_header is None
            Return None if authorization_header is not a string
            Return None if authorization_header doesn’t start by Basic
            (with a space at the end)
            Otherwise, return the value after Basic (after the space)
            You can assume authorization_header contains only one Basic
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Decodes base64 authorization header:
            class BasicAuth that returns the decoded value of a Base64
            string base64_authorization_header:
        Return:
            Return None if base64_authorization_header is None
            Return None if base64_authorization_header is not a string
            Return None if base64_authorization_header is not a valid
            Base64 - you can use try/except Otherwise, return the decoded
            value as UTF8 string - you can use decode('utf-8')
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decode_bytes = base64.b64decode(base64_authorization_header)
            return decode_bytes.decode('utf-8')
        except Exception:
            return None