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

