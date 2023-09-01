"""
This a module for Object Relational Mapping project 
which start with task 0  that has select statment
"""
import sys
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]


path = "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, database)
database = create_engine(path)
connection = database.connect()


session = sessionmaker(bind= database)
session = session()

States = session.query(states).order_by(states.id).all()

for state in states:
    print(states.id, states.name)

session.close()
