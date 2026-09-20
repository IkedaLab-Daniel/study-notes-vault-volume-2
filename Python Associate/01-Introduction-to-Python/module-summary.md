# Python Fundamentals – Review Summary

### What is Python?

* **Python** is a popular, general-purpose programming language.
* Used to build **applications, automations, websites, and other software**.
* Popular applications such as **Facebook, Netflix, and Spotify** use Python.
* Known for:

  * **Clear and readable syntax**
  * Large developer community
  * **Free and open-source**

### Course Project: Recipe Scaler

* Build a **recipe scaler** that converts a recipe into a shopping list for a party.
* A **Python script** is a file containing Python code that tells the computer what to do when executed.
* Development approach:

  * Start small
  * Iterate/improve
  * Test code
  * Document code

### Core Python Concepts

By the end of the course, you will understand:

* **Variables**
* **Data types**
* **Control flow**
* Structuring working Python code

### `print()` Function

* `print()` is a **built-in Python function** used to display information/results.
* Useful for:

  * Checking what code is doing
  * Testing code
  * Debugging mistakes
* Basic syntax:

```python
print("Hello World")
```

* Strings can use either **single (`'`) or double (`"`) quotation marks**.

### Comments

* Comments document code and help developers understand what the code does.
* Begin with `#`.
* Python ignores comments when executing the program.

```python
# This is a comment
print("Hello")
```

### Key Takeaways

* Python = **general-purpose, readable, open-source programming language**
* Python code is commonly written in **scripts**
* `print()` = **display output**
* `#` = **comment**
* Good development practice = **start small → iterate → test → document**

Python Variables, Strings, and Integers – Review Summary
Variables
Variables store values so they can be reused throughout code.
They work like labeled containers for data.
Using variables makes code easier to read, update, and maintain.
Basic syntax:
ingredient_name = "Tomato"
Data Types
A data type describes what kind of information a value represents.
Common examples:
String → text
Integer → whole number
Boolean → True or False
Python automatically determines the data type based on the stored value.
Strings
A string is text data.
Strings can contain letters, numbers, spaces, and punctuation.
Created using single (') or double (") quotes.
message = "Hello, world!"
recipe = "20-minute pasta recipe"
Use double quotes when the text contains an apostrophe:
ingredient = "Chef's secret seasoning"
Variable Naming
Python convention: use lowercase letters with underscores between words.
Example:
ingredient_name = "Tomato"
ingredient_quantity = 2
This naming style improves readability.
Integers
An integer (int) is a whole number without decimals or fractions.
Do not use quotation marks for integers.
ingredient_quantity = 2
"2" → String
2 → Integer
Printing Variables
print() can display the value stored in a variable.
print(ingredient_name)
print(ingredient_quantity)
Python looks inside the variable and outputs its stored value.
Changing Variables
Variables can be updated/reassigned after creation.
ingredient_quantity = 2
ingredient_quantity = 1
print(ingredient_quantity)

Output:

1
Key Takeaways
Variable = named storage for a value
String = text, written inside quotes
Integer = whole number, no quotes
= = assigns a value to a variable
print(variable) = displays the variable's current value
Variables can be changed/reassigned
Use lowercase_with_underscores for readable Python variable names