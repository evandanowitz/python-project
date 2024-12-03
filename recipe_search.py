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

