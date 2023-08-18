#!/usr/bin/env python3

"""This module contains code for
the user auth service in python
"""
from flask import Flask, jsonify, abort, request, make_response, redirect
import flask
from auth import Auth
# from flask_cors import (CORS, cross_origin)


app = Flask(__name__)
AUTH = Auth()
# CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """index route handler"""

    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user() -> str:
    """Registers a new user"""

    body = request.form

    try:
        user = AUTH.register_user(body["email"], body["password"])
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """Login an existing user"""

    body = request.form

    if body["email"] is None or body["password"] is None:
        flask.abort(401)

    is_credentials_valid = AUTH.valid_login(body["email"], body["password"])

    if not is_credentials_valid:
        flask.abort(401)

    session_id = AUTH.create_session(body["email"])
    response = jsonify({"email": body["email"], "message": "logged in"})
    response.set_cookie("session_id", session_id)

    return response, 200


@app.route("/sessions", methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """Sign out from current session"""

    session_id = request.cookies.get("session_id")

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)

    res = redirect("/")
    res.set_cookie("session_id", "", expires=0)

    return res


@app.route("/profile", methods=['GET'], strict_slashes=False)
def profile() -> str:
    """Returns the profile of the logged in
    user
    """

    session_id = request.cookies.get("session_id")

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    return jsonify({"email": user.email}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
