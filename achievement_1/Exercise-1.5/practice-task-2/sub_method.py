class Height(object):
  def __init__(self, feet, inches):
    self.feet = feet
    self.inches = inches

  def __str__(self):
    output = str(self.feet) + ' feet, ' + str(self.inches) + ' inches'
    return output

  def __sub__(self, other):
    # Convert both heights to inches
    height_A_inches = self.feet * 12 + self.inches
    height_B_inches = other.feet * 12 + other.inches

    # Subtract the second height from the first
    total_height_inches = height_A_inches - height_B_inches

    # Convert total height back to feet and inches
    total_height_feet = total_height_inches // 12 # Calculates the feet
    remaining_inches = total_height_inches % 12 # Calculates the leftover inches

    # Return a new Height object with the resulting feet and inches
    return Height(total_height_feet, remaining_inches)

# Create two Height objects
height_A = Height(5, 10) # 5 feet 10 inches
height_B = Height(3, 9) # 3 feet 9 inches

# Perform subtraction
height_difference = height_A - height_B

# Print the result
print('Height Difference:', height_difference)