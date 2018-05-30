import json

from sqlalchemy.orm import sessionmaker

from perepelki_api.db.models import Comment
from perepelki_api.db.models import engine

Session = sessionmaker(bind=engine)


def get_comments():
    session = Session()
    comments = session.query(Comment).order_by(Comment.id).limit(100).all()
    session.close()

    return comments


def get_comments_json():
    return json.dumps([dict(c) for c in get_comments()])


def post_comment(name, text):
    session = Session()
    c = Comment(name=name, content=text)
    session.add(c)
    session.commit()
