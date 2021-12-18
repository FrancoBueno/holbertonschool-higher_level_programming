#!/usr/bin/python3
"""
First state model
"""
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class Create State"""
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
