"""Show request headers"""

import json

import flask
from waitress import serve

app = flask.Flask(__name__)


@app.route("/")
def index():
    """Show request headers on GET"""
    headers = flask.request.headers
    print(type(headers))
    body: dict = {}
    for key, value in headers.items():
        body[key] = value
    return json.dumps(body, indent=2), {
        "Content-Type": "application/json; charset=utf-8"
    }


if __name__ == "__main__":
    # Allow to listen on all interfaces. hardcoded_bind_all_interfaces
    serve(app, host="0.0.0.0", port=8080)  # nosec
