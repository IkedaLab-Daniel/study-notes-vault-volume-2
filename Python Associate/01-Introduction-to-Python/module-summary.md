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
