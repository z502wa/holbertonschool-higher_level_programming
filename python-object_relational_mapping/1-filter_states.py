#!/usr/bin/python3
"""
Afficher tous les états dont le nom commence par un "N" majuscule, triés par id
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    Print tous les états commençant par N et triés par id
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states "
        "WHERE BINARY name LIKE 'N%' "
        "ORDER BY id ASC"
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
