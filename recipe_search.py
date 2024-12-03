# File handling (e.g., reading the binary file) will be handled in the main code or another function.

import pickle # Allows reading from and writing to binary files

# This function should format and print the details of the recipe passed to it as an argument.
# Displays a single recipe's details.
def display_recipe(recipe):
  print(f'Recipe Name: {recipe["recipe_name"]}')
  print(f'Cooking Time: {recipe["cooking_time"]} minutes')
  print('Ingredients:')
  for ingredient in recipe['ingredients']:
    print(f'{ingredient}')
  print(f'Difficulty: {recipe["difficulty"]}')

def search_ingredient(data):
  # Display all ingredients with their index
  print('\nAvailable Ingredients: ')
  for index, ingredient in enumerate(data['all_ingredients']):
    print(f'{index}. {ingredient}')

  try:
    # Prompt user to enter a number that will be used as an index to iterate through all_ingredients list.
    user_choice = int(input('\nEnter the number of the ingredient you want: '))
    # This line assumes user_choice is the index provided by the user and retrieves the corresponding ingredient.
    # Accesses data dictionary's all_ingredients key and retrieves ingredient at the index specified by user_choice.
    # If list exists and the index is valid, it will assign the ingredient to ingredient_searched.
    ingredient_searched = data['all_ingredients'][user_choice]
    print(f'You selected: {ingredient_searched}')
  except ValueError:
    print('The input you entered must be a number.')
  except IndexError:
    print('The number you entered is out of range.')
  else:
    print(f'\nRecipes containing "{ingredient_searched}":\n')
    # Use a flag to track whether any recipes are found. found variable is initialized as False.
    found = False
    # Loops through each recipe is recipes_list. Each recipe is a dictionary that contains an ingredients list.
    for recipe in data['recipes_list']:
      # Checks if the selected ingredient (ingredient_searcehd) exists in current recipe's ingredients list.
      if ingredient_searched in recipe['ingredients']:
        # If yes to the above, calls display_recipe() function to print the recipe details.
        display_recipe(recipe)
        # Add a blank line to separate recipes
        print('-' * 40)
        # Set the flag to True if a recipe is found containing the searched_ingredient.
        found = True
    # If no recipes were found containing searched_ingredient, display a message for the user.
    if not found:
      print('No recipes with that ingredient found.')

# Prompts user to provide name of binary file where recipes are saved. Stores the name in filename variable.
filename = input('Enter the name of the file containing your recipe data: ')
try:
  # Opens the file in binary read mode. File will close after the block, even if an error occurs.
  with open(filename, 'rb') as file:
    # Reads the binary data from the file and deserializes it into a Python object, which is stored in 'data' variable.
    data = pickle.load(file)
except FileNotFoundError:
  # Inform user that file does not exist.
  print('File not found. Initializing new data structure.')
  # Set data to an empty dictionary so the program still has a valid data object to work with if file isn't found.
  data = {
    'recipes_list': [],
    'all_ingredients': []
  }
  if not data['all_ingredients']:
    print('No ingredients available. Please add recipes to the file first.')
else: # else block ensures that search_ingredient() is only called if no exceptions occurred in the try block
  # Inform user that file load was successful.
  print('File loaded successfully.')
  print('\nNow you can search for a recipe by selecting an ingredient from the list below.')
  # Pass the 'data' dictionary to the search_ingredient() function.
  search_ingredient(data)