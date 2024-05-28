#!/usr/bin/env python3
"""
Basic flask setup
    - app: instance of the Flask class
    - __name__: name of the current function
"""
from flask import Flask, render_template

app = Flask(__name__)

"""
home route
    - return the home template
"""


@app.route("/")
def hello_world():
    """
    return the home template
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    """
    Main Function
    """
    app.run(host="127.0.0.1", port=5000)
