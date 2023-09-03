"""
A python file that uses module SQLAlchemy and contains the class definition of a State and an instance Base = declarative_base():

State class:
- inherits from Base 
- links to the MySQL table states
- class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
- class attribute name that represents a column of a string with maximum 128 characters and can’t be null
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

path = "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, database)
database = create_engine(path) 
connection = database.connect()

Base = declarative_base()

class State(Base):
   """
   State class:

   Attributes:

   - id: of type integar and constitute the primary key 
   - name: of type string and represents the name of state

   Args:

   - Base : instance of declarative_base
   """
   __tablename__ = "states"
   id = Column(Integer, primary_key=True, autoincrement=True,nullable=False)
   name = Column(String(128),nullable=False)
   
   def __init__(self, name):
        self.name = name

Base.metadata.create_all(bind-database)

