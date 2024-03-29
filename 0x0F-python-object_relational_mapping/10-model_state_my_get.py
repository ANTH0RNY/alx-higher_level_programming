#!/usr/bin/python3
"""
prints State object
from database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connects to the db and get a state
    from the db.
    """

    db_uri = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()
    instance = session.query(State).filter(State.name == argv[4]).first()

    if instance is None:
        print('Not found')
    else:
        print(f'{instance.id}')
