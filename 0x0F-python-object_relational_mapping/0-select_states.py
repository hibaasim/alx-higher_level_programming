#!/usr/bin/python3
'''Lists all states from the database hbtn_0e_0_usa'''

import MySQLdb
import sys

if __name__=='__main__':

    try:
        conn = MySQLdb.connect(
                host="localhost",
                port=3360,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3],
                charset="utf8")
    except MySQLdb.Error as e:
        print ("Error connecting to database: {}".format(e))
        sys.exit(1)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
