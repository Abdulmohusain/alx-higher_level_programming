#!/usr/bin/python3
"""Module contains main"""
from model_state import Base, State
from model_city import City
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
    rows = session.query(City).join(State).all()
    for cities, states in rows:
        print("{}: {} {}".format(states.name, cities.id, cities.name))

    session.close()


if __name__ == '__main__':
    """Main"""
    main()
