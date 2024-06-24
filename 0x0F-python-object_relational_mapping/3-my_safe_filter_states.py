#!/usr/bin/python3
'''Displays all values in the states table of hbtn_0e_0_usa where
name matches the argument, safe from MySQL injection'''

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
    cur.execute("SELECT * FROM states WHERE name LIKE %s\
            ORDER BY id ASC",(sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    conn.close()
