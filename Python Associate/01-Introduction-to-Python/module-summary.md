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

# Common Python Data Types & Operators – Review Summary

### Float

* A **float** represents a number with a decimal.
* Example:

```python
new_ingredient_quantity = 1.5
```

* Like integers, floats **do not use quotation marks**.

### Boolean

* A **boolean (`bool`)** stores only two possible values:

  * `True`
  * `False`
* Used for **yes/no**, **on/off**, and decision-making.
* `True` and `False` must:

  * Start with a **capital letter**
  * Have **no quotation marks**

```python
is_in_stock = True
```

* `"True"` is a **string**, not a boolean.

### Four Common Data Types

| Data Type | Purpose         | Example    |
| --------- | --------------- | ---------- |
| `str`     | Text            | `"Tomato"` |
| `int`     | Whole numbers   | `2`        |
| `float`   | Decimal numbers | `1.5`      |
| `bool`    | True/False      | `True`     |

### `type()` Function

* `type()` identifies the **data type of a value or variable**.
* Useful for **debugging** and checking data received from external sources.

```python
quantity = 1.5
print(type(quantity))
```

* Helps verify that you're working with the expected data type.

### Operators

Operators are symbols used to perform computations.

#### Arithmetic Operators

| Operator | Operation      | Example |
| -------- | -------------- | ------- |
| `+`      | Addition       | `2 + 3` |
| `-`      | Subtraction    | `5 - 2` |
| `*`      | Multiplication | `2 * 3` |
| `/`      | Division       | `6 / 2` |

* Python handles operations between integers and floats automatically.

### Operators with Strings

Only `+` and `*` work with strings:

* `+` → **concatenates/joins** strings

```python
"Hello " + "World"
# "Hello World"
```

* `*` → **repeats** a string

```python
"Hi " * 3
# "Hi Hi Hi "
```

* `-` and `/` **cannot be used with strings** and will cause an error.

### Key Takeaways

* `int` = whole numbers
* `float` = decimal numbers
* `bool` = `True` or `False`
* `str` = text
* `type()` = checks a value's data type
* `+`, `-`, `*`, `/` = arithmetic operators
* For strings:

  * `+` = join
  * `*` = repeat
  * `-` and `/` = error

# Python Strings – Review Summary

### Strings

* **Strings (`str`)** are one of the most commonly used Python data types.
* Used for:

  * Displaying messages
  * Processing user input
  * File names
  * Formatting output
  * Handling text data

### Single vs. Double Quotes

* Strings can use either **single (`'`) or double (`"`) quotes**.
* Use double quotes when the string contains an apostrophe.

```python id="j8rj3x"
message = "Chef's recipe"
```

* Using single quotes around the same text can cause a **syntax error** because Python may interpret the apostrophe as the end of the string.

### Multi-line Strings

* Use **triple double quotes (`"""`)** for multi-line strings.
* Useful for:

  * Long text
  * Recipe instructions
  * Documentation
  * Error messages
  * Help text

```python id="g7w6nb"
recipe_instruction = """Step 1: Prepare the ingredients.
Step 2: Cook the pasta.
Step 3: Serve."""
```

### Methods

* A **method** is a function associated with a particular data type.
* String methods are used to **modify, transform, or standardize text**.
* General syntax:

```python id="8b4q8s"
variable.method()
```

### `.replace()`

* Replaces one part of a string with another.
* Syntax:

```python id="p5z9k1"
variable.replace("old_text", "new_text")
```

Example:

```python id="m0j6xk"
welcome_message = welcome_message.replace("George", "John")
```

* First argument = text to replace
* Second argument = replacement text

### `.lower()`

* Converts a string to **lowercase**.
* Useful for standardizing input, such as email addresses.

```python id="w7c4pn"
ingredient_name.lower()
```

### `.upper()`

* Converts a string to **uppercase**.

```python id="w2q5sd"
ingredient_name.upper()
```

* `.lower()` and `.upper()` do not require arguments.

### Key Takeaways

* `str` = text data
* `'text'` and `"text"` both create strings
* `"""text"""` = multi-line string
* **Method** = function associated with a specific data type
* `.replace(old, new)` = replaces text
* `.lower()` = converts to lowercase
* `.upper()` = converts to uppercase
* Methods are called using **dot notation**: `variable.method()`
