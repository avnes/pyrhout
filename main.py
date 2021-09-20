"""Show request headers"""

import flask
from waitress import serve

app = flask.Flask(__name__)


@app.route("/")
def index():
    """Show request headers on GET"""
    headers = flask.request.headers
    body = ""
    for key, value in headers.items():
        print(key, value)
        body += f"{key}: {value}<br>"
    return body


if __name__ == "__main__":
    # Allow to listen on all interfaces. hardcoded_bind_all_interfaces
    serve(app, host="0.0.0.0", port=8080)  # nosec
