#!/usr/bin/python3
"""
Suhail Al-aboud <10675@holbertonstudents.com>
0-select_states.py
Lists every row in the `states` table of the given MySQL database. Rows are
printed in ascending order by `id`.

Usage:
    ./0-select_states.py <mysql_username> <mysql_password> <database_name>

The script:
    * Opens a connection to a local MySQL server on port 3306.
    * Executes a `SELECT id, name FROM states ORDER BY id ASC;` query.
    * Prints each row as a tuple (id, name).

This file is part of the Holberton School project: "Python ORM".
"""

import sys
import MySQLdb


def main():
    """Program entry point."""
    # Validate command‑line arguments
    if len(sys.argv) != 4:
        msg = (
            "Usage: ./0-select_states.py <mysql_username> <mysql_password> "
            "<database_name>"
        )
        print(msg, file=sys.stderr)
        sys.exit(1)

    user, passwd, db_name = sys.argv[1:4]

    # Establish connection to the MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name,
        charset="utf8mb4",
    )

    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC;")

    # Fetch and display all rows
    for row in cur.fetchall():
        print(row)

    # Clean up MySQL resources
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
