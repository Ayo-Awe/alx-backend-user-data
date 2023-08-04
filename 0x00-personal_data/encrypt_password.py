#!/usr/bin/env python3

"""This module contains code for the
alx personal data task in the alx backend specialisation
"""

from typing import List
import bcrypt


def hash_password(password: str) -> bytes:
    """hashes the password"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """compares hashed password to password"""
    return bcrypt.checkpw(password.encode(), hashed_password)
