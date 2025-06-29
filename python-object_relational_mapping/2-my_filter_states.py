#!/usr/bin/python3
"""
Display the row(s) in the `states` table whose name matches the value
supplied as the fourth command‑line argument.

Usage:
    ./<script_name> <mysql_username> <mysql_password> <database_name> <state_name>

The script connects to a local MySQL server (port 3306), performs a
case‑sensitive comparison using the `BINARY` keyword, orders the results by
`id` in ascending order, and prints each matching row.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """Run the query only when the module is executed directly."""

    # Establish the database connection
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8mb4",
    )

    cur = db.cursor()
    query = (
        "SELECT * FROM states "
        "WHERE BINARY name = '{}' "
        "ORDER BY id ASC"
    ).format(sys.argv[4])

    cur.execute(query)

    # Fetch and display all matching rows
    for row in cur.fetchall():
        print(row)

    # Clean up MySQL resources
    cur.close()
    db.close()
