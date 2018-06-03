from flask import Flask
from flask import request
from flask import make_response

import perepelki_api.db.api as dbapi


APP = Flask("perepelki-live-api")


@APP.route("/proxy/comments", methods=["GET"])
def get_comments():
    comments = dbapi.get_comments_json()
    resp = make_response(comments, 200)
    resp.headers["Content-Type"] = "application/json"

    return resp


@APP.route("/proxy/comments", methods=["POST"])
def post_comment():
    name = request.form["name"]
    text = request.form["text"]

    dbapi.post_comment(name, text)

    return make_response("Saved", 202)
