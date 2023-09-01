"""
This a module for Object Relational Mapping project
which start with task 0  that has select statment
"""
import sys
import MySQLdb

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name_searched = sys.argv[4]

connection = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=database)

cursor = connection.cursor()
"""
create variable to hold sql syntax because
cursor.execute does not work with format which checker mandate
instead it works with %s
"""
query = "SELECT * FROM states \
            WHERE name = {}",format([state_name_searched])

cursor.execute(query)

States = cursor.fetchall()

for state in States:
    print(state)
