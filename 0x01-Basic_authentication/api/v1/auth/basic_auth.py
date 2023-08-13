#!/usr/bin/env python3

"""This module contains the declaration
of the basic auth class
"""

from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


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
