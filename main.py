"""Show request headers"""

import flask

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


app.run(host="127.0.0.1", port=8080)
