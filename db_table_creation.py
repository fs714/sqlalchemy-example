from db_objects import Base
from db_session import engine


Base.metadata.create_all(engine)
