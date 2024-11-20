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

