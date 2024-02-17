#!/usr/bin/python3
"""Lists all cities by state from the database hbtn_0e_0_usa."""
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Create a cursor to interact with the database
    cursor = database.cursor()

    # Execute the SQL query to join cities and states tables
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states ON states.id = cities.state_id
    """)

    # Fetch all rows and print the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    database.close()
