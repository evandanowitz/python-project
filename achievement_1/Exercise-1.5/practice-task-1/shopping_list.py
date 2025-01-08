# Define a class that will keep track of items to be purchased
class ShoppingList(object):
  def __init__(self, list_name):
    self.list_name = list_name # Name of list (passed as a param when creating object)
    self.shopping_list = [] # An empty list that will hold the items to be purchased
  
  def add_item(self, item):
    if item not in self.shopping_list:
      self.shopping_list.append(item)
    else:
      print(f'\n"The item "{item}" you are trying to add already exists')

  def remove_item(self, item):
    if item in self.shopping_list: # Checks whether item exists in list. If it does...
      self.shopping_list.remove(item) # Removes first occurrence of the item from list.
      print(f'- "{item}" successfully removed.') # Notify user of successful removal of item.
    else: # If item is not in the list...
      print(f'- "{item}" you wish to remove not found.') # Notify user of failure.

  def view_list(self):
    if not self.shopping_list:
      print('\nThe shopping list is empty.')
    else:
      print('\nShopping List:')
      for item in self.shopping_list:
        print(f'- {item}')

pet_store_list = ShoppingList('Pet Store Shopping List')

pet_store_items = ['dog food', 'frisbee', 'bowl', 'collars', 'flea collars']
for item in pet_store_items:
  pet_store_list.add_item(item)

print('\nItems have been added to Shopping List...')
pet_store_list.view_list()

print('\nAttempting to remove "flea collars"...')
pet_store_list.remove_item('flea collars')

# print('\nUpdated Shopping List:')
pet_store_list.view_list()

print('\nAttempting to add "frisbee"...')
pet_store_list.add_item('frisbee')
print() # Add a blank line for spacing at the end




class Height(object):
  def __init__(self, feet, inches):
    self.feet = feet
    self.inches = inches

Adam = Height(5, 10)