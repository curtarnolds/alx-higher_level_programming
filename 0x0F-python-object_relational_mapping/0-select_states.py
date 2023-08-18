#!/usr/bin/python3
"""A MySQLdb script to list all `states` from the database `hbtn_0e_0_usa`"""
import MySQLdb
import sys


args = sys.argv
db = MySQLdb.connect(host='localhost', port=3306, user=args[1], passwd=args[2],
                     db=args[3])
cur = db.cursor()
col_count = cur.execute("SELECT * FROM states ORDER BY id")
table_rows = cur.fetchall()
for row in table_rows:
    print(row)
