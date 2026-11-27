#!/usr/bin/python3
"""List all cities belonging to a given state"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    cursor.execute(query, (argv[4],))

    rows = cursor.fetchall()

    cities = []

    for row in rows:
        cities.append(row[0])

    print(", ".join(cities))

    cursor.close()
    db.close()
