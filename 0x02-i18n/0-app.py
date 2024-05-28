#!/usr/bin/env python3
from flask import Flask, render_template

""" Basic flask setup """
app = Flask(__name__)

""" home route """


@app.route("/")
def hello_world():
    """return the home template"""
    return render_template("0-index.html")


if __name__ == "__main__":
    """ Main Function"""
    app.run(host="127.0.0.1", port=5000)
