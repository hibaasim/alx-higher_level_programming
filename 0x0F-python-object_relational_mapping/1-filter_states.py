#!/usr/bin/python3
'''Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa'''

import MySQLdb as MYSQLdb
import sys


if __name__ == '__main__':

    try:
        conn = MYSQLdb.connect(
                host="localhost",
                port=3360,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3],
                charset="utf8")
    except MYSQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    conn.close()
