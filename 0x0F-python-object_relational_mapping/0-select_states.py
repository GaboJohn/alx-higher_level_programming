#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


def list_states():
    """List all states from the hbtn_0e_0_usa database."""

    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3], port=3306)
    
    cursor = database.cursor()
    
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    
    cursor.close()
    database.close()

if __name__ == "__main__":
    list_states()

