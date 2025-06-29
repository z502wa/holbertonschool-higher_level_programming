#!/usr/bin/python3
"""
5-filter_cities
that lists all cities from the
database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    name_search = sys.argv[4]
    cursor = db.cursor()
    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id" \
            "= states.id WHERE states.name = %s ORDER BY cities.id;"
    cursor.execute(query, (name_search,))
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))
    cursor.close()
    db.close()
