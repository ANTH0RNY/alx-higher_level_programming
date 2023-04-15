#!/usr/bin/python3
"""
It adds state object
to the db
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    connect to the db and get a state
    from the db.
    """

    db_uri = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    lou_state = State(name='Louisiana')
    session.add(lou_state)
    session.commit()
    print(f'{lou_state.id}')
    session.close()
