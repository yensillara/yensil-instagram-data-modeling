import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column (String(20), nullable=False)
    user_name = Column (String(), nullable=False)
    firts_name = Column (String(), nullable=False)
    last_name = Column (String(), nullable=False)

    post= relationship ('Post', backref='user')
    comments = relationship ('Comment', backref='user')
    comment_likes = relationship ('CommentLike', backref='user')
    post_likes = relationship ('PostLike', backref='user')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    image_url = Column (String(), nullable=False)
    date_published = Column (DateTime(), nullable=False)
    latitude = Column (String(8))
    longitude = Column (String(8))
    content = Column (String (300))
    
    likes = relationship ('PostLike', backref='post')
    comments = relationship ('Comment', backref='post')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    post_id = Column (Integer, ForeignKey ('post.id'))
    user_id = Column (Integer, ForeignKey ('user.id'))
    content = Column (String (300), nullable=False)
    date_publisher = Column (DateTime(), nullable=False)

    likes = relationship ('CommentLike', backref='comment')

class PostLike(Base):
    __tablename__ = 'post_like'
    id = Column(Integer, primary_key=True)
    post_id = Column (Integer, ForeignKey ('post.id'))
    user_id = Column (Integer, ForeignKey ('user.id'))

class CommentLike(Base):
    __tablename__ = 'comment_like'
    id = Column(Integer, primary_key=True)
    post_id = Column (Integer, ForeignKey ('post.id'))
    user_id = Column (Integer, ForeignKey ('user.id'))
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')