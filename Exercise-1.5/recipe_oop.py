# Define the Recpe class
class Recipe(object):
  def __init__(self, name, ingredients, cooking_time):
    self.name = name
    self.ingredients = ingredients
    self.cooking_time = cooking_time
    self.difficulty = None # 'difficulty' attribute is auto-generated and initially set to None

