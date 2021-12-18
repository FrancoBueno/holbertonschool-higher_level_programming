#!/usr/bin/python3
"""

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

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sessions = Session()
    statenew = State(name='Louisiana')
    sessions.add(statenew)
    row = sessions.query(State).filter_by(name='Louisiana').first()
    if row is not None:
        print(str(row.id))
    else:
        print('Not Found')
    sessions.commit()
    sessions.close()
