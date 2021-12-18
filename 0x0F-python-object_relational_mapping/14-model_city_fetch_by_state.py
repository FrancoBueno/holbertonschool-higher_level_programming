#!/usr/bin/python3
"""
14. Cities in state
"""
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base = declarative_base()

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sessions = Session()
    objects = sessions.query(City, State).order_by(City.id).filter(
            City.state_id == State.id
    )
    for idxcity, idxstate in objects:
        print("{}: ({}) {}".format(idxstate.name, idxcity.id, idxcity.name))
    sessions.commit()
    sessions.close()
