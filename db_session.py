from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///test.sqlite", echo=False)
'''
engine = create_engine(
    "mysql://root:123456@192.168.56.200:23306/sqlalchemy_test?charset=utf8")
'''
Session = sessionmaker(bind=engine)
session = Session()
