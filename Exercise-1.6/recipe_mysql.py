# Import the mysql.connector module
import mysql.connector

# Initialize a connection object called conn, which connects with following parameters:
# Based on user that was set up earlier
conn = mysql.connector.connect(
  host = 'localhost',
  user = 'cf-python',
  passwd = 'password'
)

# Initialize a cursor object from conn
cursor = conn.cursor()

# Create database. IF NOT EXISTS ensures it is only database with its name on the server
cursor.execute('CREATE DATABASE IF NOT EXISTS task_database')

# Script to access database with the USE statement
cursor.execute('USE task_database')

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  ingredients VARCHAR(255),
  cooking_time INT,
  difficulty VARCHAR(20)
)''')

def calculate_difficulty(cooking_time, ingredients):
  num_ingredients = len(ingredients)
  if cooking_time < 10 and num_ingredients < 4:
    difficulty = 'Easy'
  elif cooking_time < 10 and num_ingredients >= 4:
    difficulty = 'Medium'
  elif cooking_time >= 10 and num_ingredients < 4:
    difficulty = 'Intermediate'
  else:
    difficulty = 'Hard'
  return difficulty

def format_recipe(recipe):
  return (
    f'\nID: {recipe[0]}\n'
    f'Name: {recipe[1]}\n'
    f'Ingredients: {recipe[2]}\n'
    f'Cooking Time: {recipe[3]} minutes\n'
    f'Difficulty: {recipe[4]}\n'
    '----------------------------'
  )

def create_recipe(conn, cursor):
  name = input('Enter the name of the recipe: ')
  cooking_time = int(input('Enter the cooking time (in minutes): '))
  ingredients = []
  while True:
    ingredient = input('Enter one ingredient at a time (type "done" when finished): ').strip()
    if ingredient.lower() == 'done':
      break
    ingredients.append(ingredient)
  difficulty = calculate_difficulty(cooking_time, ingredients)

  ingredients_str = ', '.join(ingredients) # Convert ingredients list to comma-separated string

  # Executes the query (sends the SQL command to the MySQL database to perform the operation)
  cursor.execute(
    'INSERT INTO Recipes (name, cooking_time, ingredients, difficulty) VALUES (%s, %s, %s, %s)',
    (name, cooking_time, ingredients_str, difficulty)
  )
  conn.commit() # Commit the changes to the database
  print(f'\nRecipe "{name}" has been successfully added to the database.')

  # ingredients_input = input('Enter the recipe\'s ingredients (separate each with a comma):')
  # ingredients = ingredients_input.split(', ')

def search_recipe(conn, cursor):
  cursor.execute('SELECT ingredients FROM Recipes') # fetches ingredients column from Recipes table in database
  results = cursor.fetchall() # retrieves all the rows into results as a list of tuples
  all_ingredients = [] # ensures you start with an empty list to store unique ingredients
  
  for row in results: # iterates through each row
    ingredients_list = row[0].split(', ') # splits the ingredient strings into individual items
    for ingredient in ingredients_list: # iterate over each item in ingredients_list
      ingredient = ingredient.lower() # convert all ingredients to lowercase before adding them
      if ingredient not in all_ingredients: # ensures there are no duplicate ingredients
        all_ingredients.append(ingredient) # if no duplicate, append the unique ingredient to all_ingredients list

  sorted_all_ingredients = sorted(all_ingredients)

  print('\nAvailable Ingredients:')  
  
  if not sorted_all_ingredients: # check if the list is empty
    print('The list of ingredients is currently empty.')
    return # exit the function

  for index, ingredient in enumerate(sorted_all_ingredients): # enumerate() returns both an index and value of each item
    print(f'{index + 1}. {ingredient}') # Example would look like: "3. Pizza"

  while True: # use a while loop to retry the check until valid input is entered
    try:
      choice = int(input('\nEnter the number corresponding to the ingredient you want to search for: '))
      if 1 <= choice <= len(sorted_all_ingredients): # reads like "if 1 is <= choice and choice is <= the length of the list"
        search_ingredient = sorted_all_ingredients[choice - 1] # value entered by user is 1-based. List indices in Python are 0-based
        print(f'You selected: "{search_ingredient}"')
        break # break exits the loop as opposed to a return statement that exits the function
      else:
        print('The number you entered is not in the list. Please try again.')
    except ValueError: # if there is a ValueError, the loop catches it, prints the error, and re-prompts the user
      print('Input value must be a number. Please try again.')

  # to search for substring in a column using SQL, use LIKE operator with wildcards(%). Matches any seq of characters
    # LIKE is an SQL operator used for pattern matching. % is a wildcard for zero or more characters
    # Example: WHERE name LIKE '%cake%' matches any name containing "cake"
  # query format: SELECT <columns to be displayed> FROM <table> WHERE <search column> LIKE <search pattern>
  # second arg must be a tuple. Adding a comma makes it a single-element tuple. Without the comma, Python will treat it as a string, causing an error.
  search_query = 'SELECT * FROM Recipes WHERE ingredients LIKE %s' # search_query contains the SQL query as a string
  cursor.execute(search_query, (f'%{search_ingredient}%',)) # passing search_query to cursor.execute() for execution. the second argument in this line provides the value for %s placeholder
  recipe_search_results = cursor.fetchall()

  if recipe_search_results:
    print(f'\nRecipes containing "{search_ingredient}":')
    # recipe_search_results is a list of tuples, where each tuple represents a row returned by the query.
    # Each tuple contains values for the columns of the Recipes table.
    # recipe is the placeholder variable representing each individual tuple (or row) as you iterate through recipe_search_results
    for recipe in recipe_search_results:
      print(format_recipe(recipe))

