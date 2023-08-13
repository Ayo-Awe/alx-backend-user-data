#!/usr/bin/env python3

"""This module contains the declaration
of the auth class
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns true if a path requires authentication"""
        if path is None or excluded_paths is None:
            return True

        tolerant_path = path if path[-1] == "/" else path+"/"

        return tolerant_path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """to be update"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """to be update"""
        return None
