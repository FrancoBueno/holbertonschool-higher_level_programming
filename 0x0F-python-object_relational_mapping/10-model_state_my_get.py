#!/usr/bin/python3
"""
10. Get a state
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
    argumento = argv[4]
    objectone = sessions.query(State).filter_by(name=argumento).first()
    if objectone is not None:
        print(str(objectone.id))
    else:
        print('Not Found')
    sessions.close()
