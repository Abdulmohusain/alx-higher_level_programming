#!/usr/bin/python3
"""Module contains """
import MySQLdb
import sys


def main():
    """Main"""
    name = sys.argv[4]
    if name:
        if ';' in name:
            name = None

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
        )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = '{}' "
        "ORDER BY states.id ASC;".format(name)
        )
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    """Main"""
    main()
