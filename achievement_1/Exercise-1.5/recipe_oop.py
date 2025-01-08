# Define the Recpe class
class Recipe(object):
  def __init__(self, name, ingredients, cooking_time):
    self.name = name
    self.ingredients = ingredients
    self.cooking_time = cooking_time
    self.difficulty = None # 'difficulty' attribute is auto-generated and initially set to None

  # Class variable. Can be used by any instance of the Recipe class.
  all_ingredients = []

  # Calculates difficulty level and updated self.difficulty attribute accordingly
  def calculate_difficulty(self):
    num_ingredients = len(self.ingredients)
    if self.cooking_time < 10 and num_ingredients < 4:
      self.difficulty = 'Easy'
    elif self.cooking_time < 10 and num_ingredients >= 4:
      self.difficulty = 'Medium'
    elif self.cooking_time >= 10 and num_ingredients < 4:
      self.difficulty = 'Intermediate'
    else:
      self.difficulty = 'Hard'

  def get_name(self):
    return self.name
  def set_name(self):
    self.name = input('Enter recipe name here: ')

  def get_cooking_time(self):
    return self.cooking_time
  def set_cooking_time(self):
    self.cooking_time = int(input('Enter cooking time (in minutes): '))

  def add_ingredients(self, *ingredients):
    for ingredient in ingredients:
      if ingredient not in self.ingredients:
        self.ingredients.append(ingredient)
    self.update_all_ingredients()

  def get_ingredients(self):
    return self.ingredients
  
  def get_difficulty(self):
    if not self.difficulty: # If difficulty has not been calculated...
      self.calculate_difficulty() # Call the calcualte_difficulty method
    return self.difficulty # Regardless of whether it was just calculated or already existsed, return the difficulty
  
  def search_ingredient(self, ingredient):
    if ingredient in self.ingredients: # Checks if the ingredient exists in the list
      return True # If it exists, True is returned immediately
    return False # If loop finishes without finding the ingredient, return False

  def update_all_ingredients(self):
    for ingredient in self.ingredients:
      if ingredient not in Recipe.all_ingredients:
        Recipe.all_ingredients.append(ingredient)
  
  def __str__(self):
    output = (
      f'\nRecipe Name: {self.name}'
      f'\nCooking Time: {self.cooking_time} minutes'
      f'\nIngredients: {", ".join(self.ingredients)}'
      f'\nDifficulty: {self.get_difficulty()}'
    )
    return output

def recipe_search(data, search_term):
  print(f'\nSearching for recipes containing "{search_term}"...')
  for recipe in data:
    if recipe.search_ingredient(search_term): # Check if the ingredient exists
      # Printing 'recipe' calls the __str()__ method, and the formatted string 'output' I defined is displayed
      print(recipe)

# Longer version going step-by-step
# tea = Recipe('Tea', [], 0)
# tea.add_ingredients('Tea Leaves', 'Sugar', 'Water')
# tea.set_cooking_time(5)
# print(tea)

# Concise way of just creating the object right away with all parameters
tea = Recipe('Tea', ['Tea Leaves', 'Sugar', 'Water'], 5)
print(tea) # When using print() on an object, Python internally searches for the __str__ method of that object's class
coffee = Recipe('Coffee', ['Coffee Powder', 'Sugar', 'Water'], 5)
print(coffee)
cake = Recipe('Cake', ['Sugar', 'Butter', 'Eggs', 'Vanilla Essence', 'Flour', 'Baking Powder', 'Milk'], 50)
print(cake)
banana_smoothie = Recipe('Banana Smoothie', ['Bananas', 'Milk', 'Peanut Butter', 'Sugar', 'Ice Cubes'], 5)
print(banana_smoothie)

recipes_list = [tea, coffee, cake, banana_smoothie]
# Later, if necessary, can dynamically add recipes to list as they're created (for loop)

search_terms = ['Water', 'Sugar', 'Bananas'] # List of ingredients to search for
for term in search_terms: # Use recipe_search method for each teerm
  recipe_search(recipes_list, term)