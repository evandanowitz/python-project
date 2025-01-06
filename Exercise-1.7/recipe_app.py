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

# Function 3
def search_by_ingredient():
  if session.query(Recipe).count() == 0: # check if there are any recipes
    print('No recipes found. Returning to Main Menu.')
    return None # exits the function
  
  results = session.query(Recipe.ingredients).all() # retrieve only the values from the ingredients column

  # compile all unique ingredients
  all_ingredients = set() # set() automatically ensures no duplicates and eliminates need for a manual check
  for ing_row in results:
    ingredients = ing_row[0].split(', ') # extract and split ingredients string into a list
    all_ingredients.update(ingredients) # add ingredients to the set
  
  # display list of unique ingredients
  print('Available Ingredients:')
  for index, ingredient in enumerate(sorted(all_ingredients), start=1): # sort for readability
    print(f'{index}. {ingredient}')
  
  while True:
    try:
      user_input = input('\nEnter the number(s) of the ingredient(s) you want to search for, separated by spaces: ') # prompt user for input
      num_choices = []
      for num in user_input.split():
        num_choices.append(int(num))

      valid = True
      for num in num_choices:
        if not (1 <= num <= len(all_ingredients)):
          valid = False
          break
      
      if valid: # map the numbers to ingredients
        sorted_ingredients = sorted(all_ingredients) # sort for consistent order
        search_ingredients = [] # list of ingredients to be searched for (contains these ingredients as strings)
        for num in num_choices:
          search_ingredients.append(sorted_ingredients[num - 1])
        
        print(f'You selected: {", ".join(search_ingredients)}')
        
        conditions = [] # initialize empty list that will contain like() (search) conditions for search ingredient
        
        for ingredient in search_ingredients:
          like_term = f'%{ingredient}%' # surround ingredient with wildcards (%)
          conditions.append(Recipe.ingredients.like(like_term)) # add the condition to the list
        break # exits the loop after successful input
      else:
        print(f'Error: Please enter numbers between 1 and {len(all_ingredients)}.')
    except Exception as e:
      print(f'An error occurred: {e}')
      return None

  # query database with all conditions from the 'conditions' list
  recipes_matching_conditions = session.query(Recipe).filter(* conditions).all()
  if not recipes_matching_conditions: # check if any recipes match the conditions
    print('No recipes found matching the selected ingredients. Please try again.')
    return None # ensures the function exits immediately
  else:
    print('\nRecipes matching your search:')
    for recipe in recipes_matching_conditions:
      print(recipe) # calls the __str__ method of the Recipe class for a clean formatted display of the recipe(s)

# Function 4
def edit_recipe():
  recipes = session.query(Recipe).all()
  if not recipes:
    print('No recipes found. Returning to Main Menu.')
    return None
  else:
    results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
    print('\nAvailable Recipes:')
    for id, name in results: # unpack the tuple since each item in results is a tuple with multiple items (id and name)
      print(f'  {id}. {name}')

    # extract valid IDs from 'results'
    valid_ids = []
    for id, name in results:
      valid_ids.append(id) # add each recipe ID to the valid IDs list

    try:
      user_input = input('\nEnter the ID number of the Recipe you want to edit: ') # prompt user for input
      recipe_id = int(user_input) # convert user input to an integer

      if recipe_id not in valid_ids: # check if the ID is valid
        print('Please enter a valid ID number from the list.')
        return None
      else:
        recipe_to_edit = session.query(Recipe).filter_by(id=recipe_id).first() # fetch the recipe from the database by its ID
        print(f'\nYou have chosen to edit the recipe: {recipe_to_edit.name}')
        print(f'  1. Name: {recipe_to_edit.name}')
        print(f'  2. Cooking Time: {recipe_to_edit.cooking_time} minutes')
        print(f'  3. Ingredients: {recipe_to_edit.ingredients}')
        while True:
          update_choice_input = input('\nEnter the number of category you want to update: ')
          try:
            category_to_update = int(update_choice_input) # convert input to an integer in the try block
            if category_to_update == 1:
              print('\nYou selected the "Name" category.')
              break # exit the loop if input is valid
            elif category_to_update == 2:
              print('\nYou selected the "Cooking Time" category.')
              break
            elif category_to_update == 3:
              print('\nYou selected the "Ingredients" category.')
              break
            else: # handle out-of-range input
              print('\nPlease enter a number between 1 and 3.')
          except Exception as e:
            print(f'\nAn error occurred: {e}')
            return None

        # after the use selects an attribute (category) and breaks the loop
        if category_to_update == 1:
          new_name = input('\nEnter the new name: ')
          recipe_to_edit.name = new_name
        elif category_to_update == 2:
          try:
            new_cooking_time = int(input('\nEnter the new cooking time (in minutes): '))
            recipe_to_edit.cooking_time = new_cooking_time
          except Exception as e:
            print(f'\nAn error occurred: {e}')
            return None
        elif category_to_update == 3:
          new_ingredients = input('\nEnter the new ingredient(s), separated by commas: ')
          recipe_to_edit.ingredients = new_ingredients
        else:
          print('\nThere was an error. Please try again.')

        # recalculate recipe difficulty after making the update
        recipe_to_edit.calculate_difficulty()

        # commit the updates to the database
        try:
          session.commit()
          print('\nRecipe updated successfully!')
        except Exception as e:
          print(f'\nAn error occurred: {e}')

    except Exception as e: # handle invalid input (e.g., non-integer values)
      print(f'\nAn error occurred: {e}')
      return None

# Function 5
def delete_recipe():
  recipes = session.query(Recipe).all()

  if not recipes:
    print('\nNo recipes found. Returning to Main Menu.')
    return None

  results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
  print('\nAvailable Recipes:')
  for id, name in results: # unpack the tuple since each item in results is a tuple with multiple items (id and name)
    print(f'  {id}. {name}')
    
  valid_ids = [id for id, name in results]
  
  try:
    user_input = input('\nEnter the ID number of the recipe you want to delete: ')
    recipe_id = int(user_input)

    if recipe_id not in valid_ids:
      print('\nPlease enter a valid ID number from the list.')
      return None

    recipe_to_delete = session.query(Recipe).filter_by(id=recipe_id).first()
    print(f'\nYou have chosen to delete the recipe "{recipe_to_delete.name}"')

    while True:
      user_confirmation = input(f'\nAre you sure you want to delete "{recipe_to_delete.name}"? Type "Yes" or "No": ').lower()
      if user_confirmation == 'yes':
        try:
          session.delete(recipe_to_delete)
          session.commit()
          print('\nRecipe deleted successfully!')
          break # exit the loop after successful deletion
        except Exception as e:
          print(f'\nAn error occurred: {e}')
          return None
      elif user_confirmation == 'no':
        print('\nDeletion cancelled. Returning to Main Menu.')
        return None
      else:
        print('\nInvalid input. Please type "Yes" or "No".')

  except Exception as e:
    print(f'\nAn error occurred: {e}')
    return None

def main_menu():
  user_choice = ''
  while user_choice != 'quit':
    print('--------------- Main Menu ---------------\n')
    print('Choose from the following options:')
    print('  1. Create a new recipe')
    print('  2. View all recipes')
    print('  3. Search for recipes by ingredients')
    print('  4. Edit an existing recipe')
    print('  5. Delete an existing recipe\n')
    print('Type "quit" to exit the application.\n')

    user_choice = input('Enter the number of your choice (e.g., 1): ').strip()

    if user_choice == '1':
      create_recipe()
    elif user_choice == '2':
      view_all_recipes()
    elif user_choice == '3':
      search_by_ingredient()
    elif user_choice == '4':
      edit_recipe()
    elif user_choice == '5':
      delete_recipe()
    elif user_choice.lower() == 'quit':
      print('Saving changes and closing connection...') # close connection before exiting
      session.close() # close the database connection. commits are handled in the functions
      print('Goodbye!')
      break
    else:
      print('\nInvalid choice. Please type "1", "2", "3", "4", "5" or "quit" to proceed.')

    print('\n') # additional new line to separate menu iterations

# create the table on the database
Base.metadata.create_all(engine)
