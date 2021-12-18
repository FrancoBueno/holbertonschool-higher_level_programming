#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    engin = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                      argv[2],
                                                                      argv[3]))
    Base = declarative_base()

    Base.metadata.create_all(engin)
    Session = sessionmaker(bind=engin)
    sessions = Session()
    for objects in sessions.query(State).order_by(State.id)
        print("{}: {}".format(objects.id, objects.name))
    sessions.close()
