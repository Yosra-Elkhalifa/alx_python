"""
This a module for Object Relational Mapping project 
which start with task 0  that has select statment
"""
import MySQLdb
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine import result


States = meta.tables["states"] 

query = sqlalchemy.select(States)

result = engine.execute(query).fetchall()

for record in result:
    print("/n", record)
