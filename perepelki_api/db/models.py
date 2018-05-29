import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text


BASE = declarative_base()

USERNAME = os.environ.get("username")
PASSWORD = os.environ.get("password")
HOST = os.environ.get("host")

engine = create_engine("mysql+pymysql://%s:%s@%s/perepelki" % (USERNAME, PASSWORD, HOST))


class Comment(BASE):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=100))
    content = Column(Text)


class Like(BASE):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True)
    count = Column(Integer)


BASE.metadata.create_all(engine)