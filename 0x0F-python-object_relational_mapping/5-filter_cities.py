#!/usr/bin/python3
"""
lists all the cities of a state
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connect to the db and get the cities
    from the db.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
        })

        rows = cur.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))
