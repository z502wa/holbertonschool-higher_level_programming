#!/usr/bin/python3
"""
Script that lists all states with a name starting with N from the database
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

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name REGEXP '^N' ORDER BY id ASC")
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
