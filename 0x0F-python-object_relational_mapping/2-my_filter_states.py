#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""
import MySQLdb
import sys

def list_states(username, password, database, search_name):
    """Lists states from the hbtn_0e_0_usa database filtered by name."""
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)
        cursor = db.cursor()

        # Execute the SQL query to retrieve states with the specified name
        query = f"SELECT * FROM states WHERE name LIKE BINARY '{search_name}'"
        cursor.execute(query)

        # Fetch all rows and print the states
        [print(row) for row in cursor.fetchall()]

    except MySQLdb.Error as e:
        print(f"Error executing query: {e}")

    finally:
        cursor.close()
        db.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        # Get MySQL credentials and search name from command-line arguments
        username, password, database, search_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
        
        # Call the function to list states
        list_states(username, password, database, search_name)

    else:
        print("Usage: {} <username> <password> <database> <search_name>".format(sys.argv[0]))
        sys.exit(1)

