from sqlalchemy import create_engine
from database_models import Base, Student, Group, Lecturer, Subject, Grades



db_url = 'postgresql://postgres:testtest@127.0.0.1:5432/univerdb'
#engine = create_engine(db_url)
engine = create_engine(db_url, echo=True)

Base.metadata.create_all(engine, checkfirst=False)
#Base.metadata.create_all(engine)

