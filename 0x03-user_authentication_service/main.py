#!/usr/bin/env python3

"""This module contains code for
the user auth service in python
"""

import requests

BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """Tests that the signup endpoint works as
    expected
    """
    res = requests.post("{}/users".format(BASE_URL), {
        "email": email,
        "password": password
    })

    user = res.json()

    assert user == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Tests that a 403 is thrown if login credentials
    are invalid
    """
    res = requests.post("{}/sessions".format(BASE_URL), {
        "email": email,
        "password": password
    })

    assert res.status_code == 401


def log_in(email: str, password: str) -> str:
    """Asserts that the login endpoint functions as expected
    """
    res = requests.post("{}/sessions".format(BASE_URL), {
        "email": email,
        "password": password
    })

    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "logged in"}
    assert res.cookies.get("session_id") is not None

    return res.cookies.get("session_id")


def profile_unlogged() -> None:
    """Tests the profile endpoint for non-logged in
    users"""
    res = requests.get("{}/profile".format(BASE_URL))

    assert res.status_code == 403


def profile_logged(session_id: str) -> None:
    """Tests the profile endpoint for
    logged in users
    """
    res = requests.get("{}/profile".format(BASE_URL),
                       cookies={"session_id": session_id})

    assert res.status_code == 200
    assert "email" in res.json()


def log_out(session_id: str) -> None:
    """Tests the logout endpoint"""
    res = requests.delete("{}/sessions".format(BASE_URL),
                          cookies={"session_id": session_id},
                          allow_redirects=False)

    assert res.status_code == 302
    assert res.headers["location"] == "/"


def reset_password_token(email: str) -> str:
    """Tests the reset passord endpoint
    """
    res = requests.post("{}/reset_password".format(BASE_URL),
                        data={"email": email})

    assert res.status_code == 200
    assert "reset_token" in res.json()

    return res.json()["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Tests reset password callback endpoint"""

    res = requests.put("{}/reset_password".format(BASE_URL),
                       data={"email": email, "reset_token": reset_token,
                             "new_password": new_password})

    assert res.status_code == 200
    assert {"email": email,  "message": "Password updated"} == res.json()


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
