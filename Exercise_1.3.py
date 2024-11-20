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
