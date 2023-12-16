#!/usr/bin/python3
"""Module contains """
import MySQLdb
import sys

if __name__ == '__main__':
    """Main"""
    if len(sys.argv) == 4:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            password='qwerty',
            database=sys.argv[3]
            )

        cur = db.cursor()
        try:
            cur.execute("USE hbtn_0e_0_usa;")
            cur.execute("SELECT * FROM states;")
            rows = cur.fetchall()
        except MySQLdb.Error as e:
                print("MySQL Error {}: ".format(e))
                
        for row in rows:
            print(row)
