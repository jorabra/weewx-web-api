from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#from models import Archive

Base = declarative_base()
engine = create_engine("postgresql://username:password@host/db_name")
Base.metadata.reflect(engine)


class Database(object):

    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    @contextmanager
    def scoped_db_session(self):
        session = self.Session()
        try:
            yield session
            #session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def get_latest_weather(self):
        with self.scoped_db_session() as session:
            archive_qr = session.query(Archive).all()[:3]
            print archive_qr[0]
            print dir(archive_qr[0])

class Archive(Base):
    __table__ = Base.metadata.tables['archive']
