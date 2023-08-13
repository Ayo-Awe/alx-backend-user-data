#!/usr/bin/env python3

"""This module contains the declaration
of the auth class
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """to be updated"""
        return False

    def authorization_header(self, request=None) -> str:
        """to be update"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """to be update"""
        return None
