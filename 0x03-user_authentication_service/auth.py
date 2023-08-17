#!/usr/bin/env python3

"""This module contains code for
the user auth service in python
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes a password and returns
    the hashed password
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)
