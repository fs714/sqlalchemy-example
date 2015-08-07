"""

   +--------+-------+         +-----------------------+        +----------+
   |                |1       M|                       |M      1|          |
   |     Story      +---------+         Task          +--------+   User   |
   |                |         |                       |        |          |
   +----------------+         +-----------------------+        +----------+

"""

from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship


Base = declarative_base()


class Story(Base):
    __tablename__ = 'story'
    id = Column(Integer, primary_key=True)
    story_title = Column(String(32))
    story_task_relation = relationship('Task', backref='task_story_relation')
    task_titles = association_proxy('story_task_relation', 'task_title')


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(32))
    user_task_relation = relationship('Task', backref='task_user_relation')
    task_titles = association_proxy('user_task_relation', 'task_title')


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task_title = Column(String(32))

    story_id = Column(Integer, ForeignKey('story.id', ondelete='cascade'))
    user_id = Column(Integer, ForeignKey('user.id'))
