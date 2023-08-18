#!/usr/bin/env python3

"""This module contains code for
the user auth service in python
"""
from flask import Flask, jsonify, abort, request
# from flask_cors import (CORS, cross_origin)


app = Flask(__name__)
# CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """index route handler"""

    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
