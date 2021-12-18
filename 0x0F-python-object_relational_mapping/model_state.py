#!/usr/bin/python3
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer(), nullable=False, unique=True,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
