#!/usr/bin/python3
"""Module contains """
from model_state import Base, State
from sqlalchemy import create_engine, text
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
    with engine.begin() as connection:
        result = connection.execute(
            text(
                "SELECT * FROM states ORDER BY states.id ASC;"
                )
            )
        for row in result:
            print("{}: {}".format(row[0], row[1]))


if __name__ == '__main__':
    """Main"""
    main()
