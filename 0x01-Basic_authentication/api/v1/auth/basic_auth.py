#!/usr/bin/env python3

"""This module contains the declaration
of the basic auth class
"""

from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User


class BasicAuth(Auth):
    """Basic Auth Class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extracts the base64 part of the basic auth header"""
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        split_header = authorization_header.split(" ")

        if split_header[0] != "Basic":
            return None

        return split_header[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Decodes a base64 auth headers"""

        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            return b64decode(base64_authorization_header).decode("utf-8")
        except Exception as e:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                     str) -> (str, str):
        """extracts username and email from decoded auth header"""

        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        credentials = decoded_base64_authorization_header.split(":")

        if len(credentials) != 2:
            return None, None

        return tuple(credentials)

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """returns the associated user"""

        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None

        matching_users = User.search({"email": user_email})

        if matching_users is None or len(matching_users) == 0:
            return None

        if not matching_users[0].is_valid_password(user_pwd):
            return None

        return matching_users[0]
