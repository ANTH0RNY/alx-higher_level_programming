#!/usr/bin/python3
"""
Deletes states with name
containing the letter a
from db
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Deletes State objects on the database.
    """

    db_uri = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    for instance in session.query(State).filter(State.name.contains('a')):
        session.delete(instance)

    session.commit()
    session.close()
