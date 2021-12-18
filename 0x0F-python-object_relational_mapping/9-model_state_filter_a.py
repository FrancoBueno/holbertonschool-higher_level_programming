#!/usr/bin/python3
"""
Contains `a`
"""
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base = declarative_base()

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sessions = Session()
    objectone = sessions.query(State).order_by(State.id).filter(
            State.name.like('%a%')
    )
    for idx in objectone:
        if idx is not None:
            print("{}: {}".format(idx.id, idx.name))
    sessions.close()
