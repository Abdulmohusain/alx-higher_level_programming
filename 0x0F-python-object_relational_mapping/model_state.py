#!/usr/bin/python3
"""Module contains state class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class
    Attributes:
        __tablename__ (str): Name of table
        id (int): state_id which is the primary key
        name (str): Name of state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128))
