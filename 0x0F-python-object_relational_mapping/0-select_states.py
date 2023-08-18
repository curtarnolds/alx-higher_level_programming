#!/usr/bin/python3
"""A MySQLdb script to list all `states` from the database `hbtn_0e_0_usa`"""
import MySQLdb


db = MySQLdb.connect(host='localhost', port=3306, user='', passwd='',
                     db='hbtn_0e_0_usa')
cur = db.cursor()
col_count = cur.execute("SELECT * FROM states ORDER BY id")
table_rows = cur.fetchall()
for row in table_rows:
    print(row)
