#!/usr/bin/python3
'''Lists all cities from the database hbtn_0e_4_usa'''

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
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
            JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
