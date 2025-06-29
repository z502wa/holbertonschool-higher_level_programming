#!/usr/bin/python3
"""
Suhail Al-aboud <10675@holbertonstudents.com>
0-select_states.py
يسرد جميع الولايات من قاعدة hbtn_0e_0_usa بترتيب تصاعدي.
الاستخدام: ./0-select_states.py <user> <password> <database>
"""

import sys
import MySQLdb


def main():
    """نقطة الدخول للبرنامج."""
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <user> <password> <db>", file=sys.stderr)
        sys.exit(1)

    user, passwd, db_name = sys.argv[1:4]
    # الاتصال
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name,
        charset="utf8mb4"
    )

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC;")
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
