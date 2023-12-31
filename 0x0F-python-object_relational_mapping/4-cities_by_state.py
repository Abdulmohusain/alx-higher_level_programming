#!/usr/bin/python3
"""Module contains """
import MySQLdb
import sys


def main():
    """Main"""
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
        )

    cur = db.cursor()
    cur.execute(
        "SELECT cities.id AS city_id, cities.name AS city, "
        "states.name AS state "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC;"
        )
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    """Main"""
    main()
