#!/usr/bin/python3
"""A MySQLdb script to list all `states` from the database `hbtn_0e_0_usa`.
Usage:
    ./1-filter.py `user` `password` `database` `state name searched`
"""
import sys
import MySQLdb


if __name__ == "__main__":
    args = sys.argv
    db = MySQLdb.connect(user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()
    col_count = cur.execute("SELECT cities.id, cities.name, states.name FROM\
                            `cities` INNER JOIN states ON cities.state_id =\
                            states.id ORDER BY cities.id")
    table_rows = cur.fetchall()
    for row in table_rows:
        print(row)
    cur.close()
    db.close()
