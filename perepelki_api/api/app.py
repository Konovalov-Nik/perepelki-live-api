from flask import Flask
from flask import make_response

import perepelki_api.db.api as dbapi


APP = Flask("perepelki-live-api")


@APP.route("/comments", methods=["GET"])
def get_comments():
    comments = dbapi.get_comments_json()
    resp = make_response(comments, 200)
    resp.headers["Content-Type"] = "application/json"

    return resp
