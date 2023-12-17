#!/usr/bin/python3
"""Module contains main"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def main():
    """Main"""
    database_url = "mysql://{}:{}@localhost:3306/{}".format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
        )
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.query(State).order_by(State.id).first()
    # if row is not None:
    #     print("{}: {}".format(row.id, row.name))


if __name__ == '__main__':
    """Main"""
    main()
