# Recipe App (Command Line Version)

## Project Deliverables
### Exercise 1.2: Data Types in Python
- Use data types and methods to execute Python commands that store recipes containing their own internal data
- Enter a number of these recipes into another linear data structure
#### What Did I Do?
- Used a **dictionary** data structure to create `recipe_1` with `name`, `cooking_time`, and `ingredients` keys.
  - I’ve chosen dictionaries as the data structure for creating individual recipes.
  - Dictionaries are great for storing labeled data like the keys I’ll use in the recipes.
  - Values can be of **any data type** (useful when values are _strings_/_integers_/_lists_/etc.)
  - There is **no restrictions for immutable data types** for values.
  - Key-value pairs **can be added or deleted**.
  
- Created an outer structure called `all_recipes` with a **list** data structure and added `recipe_1` to it.
  - For `all_recipes`, I’ve chosen to use a list for the data structure because of their **mutability and flexibility** as opposed to a _tuple_.
  - Any of the internal elements in that list **can be modified or deleted** with ease.
  - Elements **can be rearranged** and **new elements can be added**.
  - All of these modifications can take place **without affecting the rest of the sequence**.

- Generated four additional recipes and used the **`append()`** function to add them to `all_recipes`.

- Printed the `ingredients` key for each recipe as five different lists inside the **IPython** shell.

- Added to learning journal
