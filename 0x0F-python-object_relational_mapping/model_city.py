#!/usr/bin/python3
"""Module contains state class"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """State class
    Attributes:
        __tablename__ (str): Name of table
        id (int): state_id which is the primary key
        name (str): Name of state
        state_id (int): state_id foreign key
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
