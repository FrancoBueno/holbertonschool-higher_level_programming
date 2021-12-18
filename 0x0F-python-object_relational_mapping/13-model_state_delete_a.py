#!/usr/bin/python3
"""
13. Delete states
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
    detector = "a"
    sessions = Session()
    objectone = sessions.query(State).order_by(State.id).all()
    for idx in objectone:
        if detector in idx.name:
            sessions.delete(idx)
    sessions.commit()
    sessions.close()
