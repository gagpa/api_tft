import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from config.db_config import URL

engine = create_engine(URL)


def create_db():
    db = sqlalchemy
    Base = declarative_base()
    session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    Base.query = session.query_property()
    Base.metadata.create_all(bind=engine)
    return db, Base, session


db, Base, session = create_db()
