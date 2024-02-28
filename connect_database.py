from sqlalchemy import create_engine


def create_database_engine():
    db_url = 'postgresql://postgres:testtest@127.0.0.1:5432/univerdb'
    engine = create_engine(db_url)
    return engine