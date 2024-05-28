#!/usr/bin/env python3
"""Task 1: Basic Flask app
"""

from flask import Flask, render_template
from flask_babel import Babel
from requests import request


class Config:
    """Config class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


def get_locale():
    """get locale"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """default route"""
    return render_template(
        "1-index.html",
    )


if __name__ == "__main__":
    app.run(debug=True)