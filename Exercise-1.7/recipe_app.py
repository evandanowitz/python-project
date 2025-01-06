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

# Function 1
def create_recipe():
  while True: # keeps looping until the break statement is executed
    name = input('Enter the name of the recipe (maximum of 50 characters): ')
    if len(name) > 50: # if name is too long...
      print('Name must be 50 characters or less. Please try again.') # print error message and let the loop run again
    else:
      break # exit the loop if the input is valid
  # print(f'Recipe name accepted: {name}')

  while True:
    try:
      cooking_time = int(input('Enter the cooking time (in minutes): '))
      if cooking_time > 0:
        # print(f'Recipe cooking time accepted: {cooking_time}')
        break # exit the loop if the input is valid
      else:
        print('Cooking time must be a positive number. Please try again.') # retry for negative or zero
    except Exception as e:
      print(f'An error occurred: {e}')
      return None
  
  while True:
    try:
      num_of_ingredients = int(input('Enter the number of ingredients to enter: '))
      if num_of_ingredients > 0:
        break # exit the loop if the input is valid
      else:
        print('Input must be a positive number. Please try again.') # retry for negative or zero
    except Exception as e:
      print(f'An error occurred: {e}')
      return None
  
  ingredients = [] # initialize empty list to store ingredients
  for i in range(num_of_ingredients):
    while True: # loop to retry entering the same ingredient until valid input is provided
      ing = input(f'Enter ingredient {i + 1}: ').strip()
      if not ing:
        print('Ingredient cannot be empty. Please try again.')
      elif ing in ingredients: # prevent duplicate ingredients
        print(f'Ingredient "{ing}" is already in the list. Please enter a different ingredient.')
      else:
        ingredients.append(ing) # add valid, unique ingredient
        break # ensures program exits inner loop and movies to next ingredient only when valid input is provided
  ingredients_str = ', '.join(ingredients) # Convert ingredients list to comma-separated string
  # print(f'Ingredients accepted: {ingredients_str}')

  recipe_entry = Recipe(
  name = name,
  cooking_time = cooking_time,
  ingredients = ingredients_str
  )

  # call the calculate_difficulty() method on the recipe_entry object
  recipe_entry.calculate_difficulty()

  # add and save the recipe to the database
  session.add(recipe_entry)
  session.commit()

  print(f'\nRecipe "{name}" has been successfully added to the database.')

# Function 2
def view_all_recipes():
  all_recipes = session.query(Recipe).all() # database query for all recipes
  if not all_recipes: # check to handle case when no recipes exist
    print('Recipes list is empty. Returning to Main Menu.')
    return None # exits the function
  else:
    print('\nEnjoy your ingredients list.')
    print('-' * 40)
    for index, recipe in enumerate(all_recipes, start=1): # use enumerate function to add numbers
      print(f'{index}.')
      print(recipe) # 'recipe' here in the print statement triggers the __str__ method of the Recipe class
      if index != len(all_recipes): # if the index of the recipe is not the last in the all_recipes list...
        print() # print a blank line for spacing
    print('-' * 40)

