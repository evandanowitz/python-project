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

# Ask the user for a filename
filename = input('Enter the name of the file you want to save your recipe to (<anything>.bin): ')

# Initialize 'recipes_list' and 'all_ingredients' as empty lists
recipes_list = []
all_ingredients = []

# try-except-else-finally block to handle file operations
try:
  # Attempt to open the file in binary read mode
  with open(filename, 'rb') as file:
    # Load the data from the file
    data = pickle.load(file)
    print('Data loaded successfully from the file.')

except FileNotFoundError:
  # Handle the case where the file does not exist
  data = {
    'recipes_list': [],
    'all_ingredients': []
  }
  print('File not found. Initializing new dictionary.')

except Exception as error:
  # Handle other exceptions (e.g., corrupted file, permission error, etc.)
  data = {
    'recipes_list': [],
    'all_ingredients': []
  }
  print(f'An error occurred: {error}. Initializing new dictionary.')

finally:
  # If no exceptions, extract values from the dictionary into two separate lists
  recipes_list = data['recipes_list']
  all_ingredients = data['all_ingredients']

# Ask the user how many recupes they'd like to enter and convert input to an integer
num_recipes = int(input('Enter the number of recipes you want to input: '))
# Loop for the number of recipes
# Here, I am looping num_recipes times to call the take_recipe() function and append its output to recipes_list.
# Don't need to reference the loop variable ('_') in this situation, which is why it can be an underscore or anything.
# Essentially saying: "I don't care about the index; I just want to execute this block num_recipes times."
for _ in range(num_recipes):
  # Call the take_recipe() function and append the result to recipes_list
  recipe = take_recipe()
  recipes_list.append(recipe)
  # Loop through the ingredients of the current recipe
  for ingredient in recipe['ingredients']:
    # Check if an ingredient in the current recipe is not already in the all_ingredients list
    if ingredient not in all_ingredients:
      # If an ingredient in current recipe is not already in all_ingredients list, add (append) it to it.
      all_ingredients.append(ingredient)

# Display the loaded or initialized lists
print(f'Recipes in the list: {len(recipes_list)}')
print(f'Ingredients available: {len(all_ingredients)}')

# This 'data' dictionary stores two key-value pairs.
# Pairing the keys 'recipes_list' and 'all_ingredients' with their respective list variables.
data = {
  'recipes_list': recipes_list,
  'all_ingredients': all_ingredients
} 

# Write and save data to the binary file.
# Open the file in binary write mode. 'filename' is the user-defined name of the file received earlier.
with open(filename, 'wb') as file:
  # Write the data dictionary to the binary file using pickle.
  # Converts the 'data' dictionary into a binary format and writes it to the file.
  # This saves the current state of the recipes_list and all_ingredients lists.
  pickle.dump(data, file)
  # Confirmation message for the user.
  print(f'Data successfully written to "{filename}".')
  # File is automatically closed when the block ends with 'with open(...)'