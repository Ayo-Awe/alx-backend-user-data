#!/usr/bin/env python3

"""This module contains code for
the user auth service in python
"""
from flask import Flask, jsonify, abort, request, make_response, redirect
import flask
from auth import Auth
# from flask_cors import (CORS, cross_origin)


app = Flask(__name__)
auth = Auth()
# CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """index route handler"""

    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user():
    """Registers a new user"""

    body = request.form

    try:
        user = auth.register_user(body["email"], body["password"])
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """Login an existing user"""

    body = request.form

    if body["email"] is None or body["password"] is None:
        flask.abort(401)

    is_credentials_valid = auth.valid_login(body["email"], body["password"])

    if not is_credentials_valid:
        flask.abort(401)

    session_id = auth.create_session(body["email"])
    response = jsonify({"email": body["email"], "message": "logged in"})
    response.set_cookie("session_id", session_id)

    return response


@app.route("/sessions", methods=['DELETE'], strict_slashes=False)
def logout():
    """Sign out from current session"""

    session_id = request.cookies.get("session_id")

    if session_id is None:
        abort(403)

    user = auth.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    auth.destroy_session(user.id)

    res = redirect("/")
    res.set_cookie("session_id", "", expires=0)

    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
