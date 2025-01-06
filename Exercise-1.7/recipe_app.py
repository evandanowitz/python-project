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

  # responsible for the formatted output you see when running view_all_recipes()
  def __str__(self):
    ingredients_list = self.return_ingredients_as_list() # convert to list
    return (
      f'Recipe Name:\t{self.name or "N/A"}\n'
      f'Cooking Time:\t{self.cooking_time} minutes\n'
      f'Ingredients:\t{", ".join(ingredients_list) if ingredients_list else "N/A"}\n'
      f'Difficulty:\t{self.difficulty}'
    )
  
  # difficulty level is assigned to instance variable self.difficulty
  def calculate_difficulty(self):
    num_ingredients = len(self.return_ingredients_as_list())
    if self.cooking_time < 10 and num_ingredients < 4:
      self.difficulty = 'Easy'
    elif self.cooking_time < 10 and num_ingredients >= 4:
      self.difficulty = 'Medium'
    elif self.cooking_time >= 10 and num_ingredients < 4:
      self.difficulty = 'Intermediate'
    else:
      self.difficulty = 'Hard'

  def return_ingredients_as_list(self):
    if self.ingredients == '': # if ingredients string is empty...
      print('Ingredients list is empty. Here is an empty list.')
      return [] # return an empty list
    else:
      return self.ingredients.split(', ') # split string into list with ', '

