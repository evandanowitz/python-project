# This script takes recipes from the user, compiles them and their ingredients 
# into a list, and stores all this in a binary file for later use. 
# The script can be run again later to add more recipees

import pickle # Allows you to work with binary files later in the script

# Function to take user input and return a recipe dictionary
def take_recipe():

  # Prompt user to enter the recipe's name
  recipe_name = input('Enter the name of the recipe: ')

  # Prompt user to enter the cooking time and convert it to an integer
  cooking_time = int(input('Enter the cooking time (minutes): '))

  # Initialize an empty list to store ingredients
  ingredients = []

  # While loop to gather ingredients until user types 'done'
  while True:
    # Prompt user to enter an ingredient
    ingredient = input('Enter an ingredient (type "done" when finished): ')
    
    # Check if user wants to stop entering ingredients
    if ingredient == 'done':
      # Exit loop if 'done' is typed by user
      break
    else:
      # Add the ingredient to the list
      ingredients.append(ingredient)
  
