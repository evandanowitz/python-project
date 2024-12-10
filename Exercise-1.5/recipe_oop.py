# Define the Recpe class
class Recipe(object):
  def __init__(self, name, ingredients, cooking_time):
    self.name = name
    self.ingredients = ingredients
    self.cooking_time = cooking_time
    self.difficulty = None # 'difficulty' attribute is auto-generated and initially set to None

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

