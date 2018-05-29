import json

from sqlalchemy.orm import sessionmaker

from perepelki_api.db.models import Comment
from perepelki_api.db.models import engine

Session = sessionmaker(bind=engine)


def get_comments():
    session = Session()
    comments = session.query(Comment).order_by(Comment.id).limit(100).all()

    return comments


def get_comments_json():
    return json.dumps(get_comments())