#!/usr/bin/env python3

"""This module contains the declaration
of the auth class
"""

from flask import request
from typing import List, TypeVar
import re


class Auth:
    """Auth Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns true if a path requires authentication"""
        if path is None or excluded_paths is None:
            return True

        tolerant_path = path if path[-1] == "/" else path+"/"

        for ep in excluded_paths:
            pre_star = ep[:-1] if ep.endswith("*") else None

            if pre_star is not None and tolerant_path.startswith(pre_star):
                return False

            if ep == tolerant_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Returns the value of the Authorization header"""
        if request is None:
            return None

        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """to be update"""
        return None
