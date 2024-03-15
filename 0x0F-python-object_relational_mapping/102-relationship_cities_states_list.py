#!/usr/bin/python3
"""Module contains main"""
from relationship_state import Base, State
from relationship_city import City
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
    # rows = session.query(City, State).filter(City.state_id == State.id).all()
    # for city, state in rows:
    #     print("{}: ({}) {}".format(state.name, city.id, city.name))

    cities = session.query(City).all()
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
    

if __name__ == '__main__':
    """Main"""
    main()