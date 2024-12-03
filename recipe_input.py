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
  
  # Calculate the difficulty of the recipe using the 'calc_difficulty' function
  difficulty = calc_difficulty(cooking_time, ingredients)
  
  # Create a dictionary to store all recipe details
  recipe = {
    'recipe_name': recipe_name, # Name of the recipe
    'cooking_time': cooking_time, # Cooking time in minutes
    'ingredients': ingredients, # List of ingredients
    'difficulty': difficulty # Difficulty level
  }
  # Return the completed recipe dictionary
  return recipe

def calc_difficulty(cooking_time, ingredients):
  num_ingredients = len(ingredients) # Get the number of ingredients
  if cooking_time < 10 and num_ingredients < 4:
    return 'Easy'
  elif cooking_time < 10 and num_ingredients >= 4:
    return 'Medium'
  elif cooking_time >= 10 and num_ingredients < 4:
    return 'Intermediate'
  else:
    return 'Hard'

