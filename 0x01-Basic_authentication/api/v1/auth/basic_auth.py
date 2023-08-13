#!/usr/bin/env python3

"""This module contains the declaration
of the basic auth class
"""

from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Auth Class"""
