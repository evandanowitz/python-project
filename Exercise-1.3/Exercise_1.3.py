recipes_list = []
ingredients_list = []

def take_recipe():
  name = str(input('Enter the name of the recipe: '))
  cooking_time = int(input('Enter the recipe time in minutes: '))
  ingredients = []
  while True:
    ingredient = input('Enter an ingredient (or type "done" to finish): ')
    if ingredient == 'done':
      break
    else:
      ingredients.append(ingredient)
  recipe = {
    'name': name,
    'cooking_time': cooking_time,
    'ingredients': ingredients
  }
  return recipe # This sends the recipe dictionary back to the caller (in this case, the for loop)

n = int(input('How many recipes would you like to enter? '))

for recipe in range(n): # Iterates n times for each recipe
  recipe = take_recipe() # This assigns the output of take_recipe() to the recipe variable during each iteration
  for ingredient in recipe['ingredients']: # Iterates over the ingredients in the current recipe
    if ingredient not in ingredients_list: # Checks if the ingredient is already in ingredients_list
      ingredients_list.append(ingredient) # If not already in ingredients_list, append the ingredient
  recipes_list.append(recipe) # Add the recipe to the list of recipes

# print("\nRecipes List:", recipes_list)
# print("\nIngredients List:", ingredients_list)

for recipe in recipes_list:
  if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
    recipe['difficulty'] = 'Easy' # Adds a 'difficulty' key to each recipe
  elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
    recipe['difficulty'] = 'Medium'
  elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
    recipe['difficulty'] = 'Intermediate'
  elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
    recipe['difficulty'] = 'Hard'

  print() # Adds a blank line before each recipe
  print('Recipe:', recipe['name'])
  print('Cooking Time (min): ' + str(recipe['cooking_time']) + ' minutes')
  # print('List of Ingredients:', recipe['ingredients'])
  print('Ingredients:')
  for ingredient in recipe['ingredients']:
    print('- ' + ingredient) # Prints each ingredient on its own line with a dash
  print('Difficulty:', recipe['difficulty'])

# Display all unique ingredients in alphabetical order
all_unique_ingredients = sorted(ingredients_list)
print('\nIngredients Available Across All Recipes')
print('-----------------------------------------')
for ingredient in all_unique_ingredients:
  print(ingredient)