#!/usr/bin/python3
"""Lists all cities by state from the database hbtn_0e_0_usa."""
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

    cursor.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))

    rows = cursor.fetchall()

    name_x = list(row[0] for row in rows)
    print(*name_x, sep=", ")

    cursor.close()
    database.close()
