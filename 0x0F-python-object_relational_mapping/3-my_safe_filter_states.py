#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306
    )
    cursor = database.cursor()

    match_state = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (match_state, ))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    database.close()
