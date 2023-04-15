#!/usr/bin/python3
"""
lists all values in the states where name
matches argv[4] from the db
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connect to the db and get the states
    from the db.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute(f"SELECT * FROM states \
                 WHERE name LIKE BINARY '{argv[4]}' \
                 ORDER BY states.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)
