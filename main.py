"""Show request headers"""

import json

import flask
from waitress import serve

app = flask.Flask(__name__)


def get_json(headers) -> str:
    """Construct a str formatted like JSON"""
    body: dict = {}
    for key, value in headers.items():
        body[key] = value
    return json.dumps(body, indent=2)


@app.route("/<path:text>", methods=["GET"])
def all_routes(text):
    """Show request headers on GET for all paths"""
    print(text)
    return get_json(flask.request.headers), {
        "Content-Type": "application/json; charset=utf-8"
    }


@app.route("/", methods=["GET"])
def index():
    """Show request headers on GET for /"""
    return get_json(flask.request.headers), {
        "Content-Type": "application/json; charset=utf-8"
    }


if __name__ == "__main__":
    # Allow to listen on all interfaces. hardcoded_bind_all_interfaces
    serve(app, host="0.0.0.0", port=8080)  # nosec
