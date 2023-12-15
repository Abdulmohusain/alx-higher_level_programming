#!/usr/bin/env python3
import MySQLdb
import sys

if __name__ == '__main__':
    """Main"""
    print(sys.argv)
    if len(sys.argv) == 4:
        db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        all_states = cur.execute("SELECT * FROM states;")
        for state in all_states:
            print(state)
