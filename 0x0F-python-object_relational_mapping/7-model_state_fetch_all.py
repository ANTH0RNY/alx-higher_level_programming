#!/usr/bin/python3
"""
list all state object
from db
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the db and get the states
    from the db.
    """

    db_uri = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    for instance in session.query(State).order_by(State.id):
        print(f'{instance.id}: {instance.name}')
