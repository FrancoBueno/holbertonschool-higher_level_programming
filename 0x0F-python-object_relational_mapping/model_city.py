#!/usr/bin/python3
"""
Cities in state
"""
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
Base = declarative_base()


class City(Base):
    """ City tabla nueva"""
    __tablename__ = 'cities'
    id = Column(Integer(), nullable=False, unique=True,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
