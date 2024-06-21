#!/usr/bin/python3
"""
script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument.
Your script should take 4 arguments: mysql username,
mysql password, database name and state name searched
(no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
You must use format to create the SQL query with the user input
Results must be sorted in ascending order by states.id
"""


import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cursor = db.cursor()

    sql = """ SELECT * FROM states
          WHERE name LIKE BINARY '{}'
          ORDER BY id ASC """.format(sys.argv[4])

    cursor.execute(sql)

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
