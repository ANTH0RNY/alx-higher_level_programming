#!/usr/bin/python3
"""
lists the first state obj
from the db
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the db and get a state
    from the db.
    """

    db_uri = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()
    instance = session.query(State).order_by(State.id).first()

    if instance is None:
        print('Nothing')
    else:
        print('{0}: {1}'.format(instance.id, instance.name))
