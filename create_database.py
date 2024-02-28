from connect_database import create_database_engine
from database_models import Base

engine = create_database_engine()


def create_tables(engine):
    Base.metadata.create_all(engine)