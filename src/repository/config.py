from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.strategic_ploy import Base

user = 'compose-postgres'
password = 'compose-postgres'
host = 'localhost'
port = 5432
database = 'Killteam'

def get_connection():
    return create_engine(
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )

def connect_db():
    # Setup DB connection
    engine = get_connection()
    Session = sessionmaker(bind=engine)
    session = Session()

    # Ensure tables exist
    Base.metadata.create_all(engine)

    return session
