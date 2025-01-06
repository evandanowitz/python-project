from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base # changed to below
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker

# create engine object to connect to the task_database
# username: 'cf-python', password: 'password', hostname: 'localhost', database name: 'task_datbase'
engine = create_engine("mysql+pymysql://cf-python:password@localhost/task_database")

# store the declarative base class in 'Base'
Base = declarative_base()

# create session object that will be used to make changes to the database
Session = sessionmaker(bind=engine) # generate the Session class and bind it to the engine object
session = Session() # initialize the session object

# define Recipe model inheriting from Base
class Recipe(Base): # Recipe class inherits the Base class created previously
  __tablename__ = 'final_recipes' # define an attribute to set the table's name as 'final_recipes'
  # define the following attributes to create columns in your table
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50))
  ingredients = Column(String(255))
  cooking_time = Column(Integer)
  difficulty = Column(String(20))

  # quick representation of recipe. used for debugging and dev-friendly representation of object, typically when you print object directly
  def __repr__(self):
    return f'Recipe ID: {self.id} - {self.name}'

