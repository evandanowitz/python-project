# Recipe App (Command Line Version)

## Objective
To build the command line version of a Recipe app, which acts as a precursor to its web app counterpart in Achievement 2.

## Context
This project primarily focuses on implementing Python fundamentals, data structures, and object-oriented programming. It also incorporates and interacts with databases using Python as well as promote standard programming practices that make the code simpler, more readable, and more robust during execution.

## User Goals
1. Users should be able to create and modify recipes with ingredients, cooking time, and a difficulty parameter that would be automatically calculated by the app.
2. Users should be able to search for recipes by their ingredients.

## Key Features
- Create and manage the user's recipes on a locally hosted MySQL database.
- Option to search for recipes that contain a set of ingredients specified by the user.
- Automatically rate each recipe by their difficulty level.
- Display more details on each recipe if the user prompts it, such as the ingredients, cooking time, and difficulty of the recipe.

## Technical Requirements
- The app should handle any common exceptions or errors that may pop up either during user input, database access, for example, and display user-friendly error messages.
- The app must connect to a MySQL database hosted locally on your system.
- The app must provide an easy-to-use interface, supported by simple forms of input and concise instructions that any user can follow (e.g., instead of having them manually type in the option, list the options with numbers, and have them enter the number corresponding to their choice).
- The app should work on Python 3.6+ installations.
- App code must be well-formatted according to standardized guidelines.
- App code should also be supported by concise, helpful comments that illustrate the flow of the program.
- The app hsould be able to handle any kind of input from the user–assume that your user would enter random, nonsensical inputs (this concept is known as "monkey testing").
- Make an instruction manual (a simple, one-page document would suffice) that describes the features of the app, as well as simple instructions that can take the user through the program. This can be hosted here in the README.

## Project Deliverables
### Exercise 1.1: Intro to Python Programming
- Install Python on macOS, Windows, or Linux
- Create and manage virtual environments
- Use pip to install and manage packages
#### What Did I Do?
- Install Python `3.8.7` on my system
- Created a new virtual environment called `cf-python-base`: `mkvirtualenv cf-python-base`
- Created a project directory folder called `python-project-1`
- Added a file called `add.py` and defined two variables as well as a function that stores the values of the two variables in a third variable. Then, I printed that variable (`c`) to the console
- Set up an IPython shell in the `cf-python-base` virtual environment (like the regular Python REPL): `pip3.8 install ipython`
- Verified the installation of IPython by launching an IPython shell: `ipython`
- Exported a `requirements.txt file`: `pip freeze > requirements.txt`
- Created a new virtual environment called `cf-python-copy` and installed packages from the `requirements.txt` file: `pip install -r requirements.txt`
- Created a GitHub repo for the project and made my commits and published the branch.
- Created and documented a README.md file
- Started a learning journal
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
### Exercise 1.3: Functions and Other Operations in Python
- Create your first script on a `.py` script file
- Build a script that uses `if-elif-else` statements, `for` loops, and functions to take recipes from the user, then display them
#### What Did I Do?
- Created a script called `Exercise_1.3.py` and initialized two empty lsits called `recipes_list` and `ingredients_list`
- Defined a function called `take_recipe()`, which takes inputs from users for the following variables: `name` (str), `cooking_time` (int), `ingredients` (list), and `recipe` (dictionary storing the above variables)
- Created variable `n` that stores the user response when asked how many recipes they want to enter
- Created a **for loop** to run `take_recipe()` function and store its ooutput in a variable called `recipe`
- Created another **for loop** to iterate over all ingredients, and if not present in ingredients_list already, will `append` the new ingredient to it. Once ingredients are added, it will be appended `recipe` to `recipes_list`
- Created a **for loop** to iterate through `recipes_list` pick out each `recipe`, and determine the **difficulty** for each one via the use of `if-elif-else` statements, **conditionals**, and **logic operators** such as `and`, `or`, and `not`.
- Displayed each `recipe` in an organized way as well as sorted and displayed all ingredients in alphabetical order.
### Exercise 1.4: File Handling in Python
- Create a Python script that takes recipes from the user and writes the data in a binary file
- Create another script that reads the binary file and lists out the available ingredients. The user chooses an ingredient and the script displays all recipes which contain it
- Use Python's exception handling features to handle common errors
#### What Did I Do?
### Exercise 1.5: Object-Oriented Programming in Python
- Build a custom class for your recipes, which contains its own data attributes for name, ingredients, cooking time, and difficulty, as well as other custom methods to interact with this data
#### What Did I Do?
### Exercise 1.6: Connecting to Databases in Python
- Set up a MySQL database and connect your scripts to it
- Build an application that creates, reads, updates, and deletes recipes, as well as searching for them by a single ingredient
#### What Did I Do?
### Exercise 1.7: Finalizing Your Python Program
- Use an Object Relational Mapper from SQLAlchemy to manage the contents of your database from your application
- Build a user-friendly menu for entering and searching recipes and ingredients
- Store recipe and ingredient data in a MySQL database
- Implement recipe search according to user-defined ingredients
- Implement a detailed display of the recipe selected by the user
#### What Did I Do?
