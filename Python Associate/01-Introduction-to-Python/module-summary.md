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

# Python Lists – Review Summary

### Lists

* A **list** stores multiple values in a single variable.
* Useful for collections such as:

  * Ingredients
  * User inputs
  * Database records
* Created using **square brackets `[]`**, with values separated by commas.

```python
ingredients = ["tomato", "garlic", "onion", "basil"]
```

* Lists can contain values of **any data type** and can also use variables.

### Checking List Type

* Use `type()` to check whether a variable is a list.

```python
print(type(ingredients))
```

* The result is `<class 'list'>`, regardless of the data types stored inside.

### List Indexing

* Lists are **ordered and indexed**.
* Python indexes start at **0**, not 1.

```text
Index:    0        1        2        3
Value:  tomato   garlic   onion    basil
```

* Access an element using square brackets:

```python
ingredients[0]  # first element
ingredients[3]  # fourth element
```

### Negative Indexing

* `-1` accesses the **last element**.
* Useful when the list length is unknown.

```python
ingredients[-1]
```

* `-2` = second-to-last, `-3` = third-to-last, etc.

### List Slicing

* Slicing extracts a **range of elements**.
* Syntax:

```python
list[start:end]
```

* The `start` index is included.
* The `end` index is **excluded**.

```python
ingredients[1:3]
```

* Returns indexes `1` and `2`.

### Slicing to the End

```python
ingredients[3:]
```

* Gets everything from index `3` to the end.

### Slicing from the Start

```python
ingredients[:3]
```

* Gets everything from the beginning up to, but **not including**, index `3`.

### Step Values

* Slicing can include a **step**:

```python
list[start:end:step]
```

* Every second element:

```python
ingredients[::2]
```

* Gets indexes `0, 2, 4, ...`

* Starting at index `1`, every third element:

```python
ingredients[1::3]
```

### Key Takeaways

* **List** = collection of multiple values
* `[]` = creates/accesses a list
* Indexing starts at **0**
* `list[0]` = first element
* `list[-1]` = last element
* `list[start:end]` = slice/range
* **End index is excluded**
* `list[start:]` = from start index to end
* `list[:end]` = from beginning to end index
* `list[::step]` = access elements at intervals

# Python Dictionaries – Review Summary

### Dictionaries

* A **dictionary (`dict`)** stores data as **key-value pairs**.
* Useful when you need to represent a relationship between pieces of data.
* Example: linking an ingredient to its quantity.

```python id="5rj7vq"
ingredients = {
    "pasta": 500,
    "tomato": 2,
    "garlic": 3
}
```

### Creating a Dictionary

* Use **curly brackets `{}`**.
* Each key-value pair follows:

```python id="x5m8zn"
"key": value
```

* Separate multiple pairs with commas.

### Dictionary vs. List

| Structure       | Purpose                | Access   |
| --------------- | ---------------------- | -------- |
| List `[]`       | Collection of values   | By index |
| Dictionary `{}` | Related key-value data | By key   |

### Accessing Values

* Use the **key inside square brackets** instead of an index.

```python id="t9p5xk"
ingredients["pasta"]
```

* Returns the value associated with `"pasta"`.

### Dictionary Methods

#### `.values()`

* Returns all **values**.

```python id="z7h2qm"
ingredients.values()
```

#### `.keys()`

* Returns all **keys**.

```python id="f1n6pa"
ingredients.keys()
```

#### `.items()`

* Returns all **key-value pairs**.
* Each pair is represented as a **tuple**.

```python id="k4v8dy"
ingredients.items()
```

### Adding a Key-Value Pair

* Assign a value to a **new key**:

```python id="n3x6wb"
ingredients["basil"] = 10
```

### Updating a Value

* Assign a new value to an **existing key**:

```python id="q6m2ks"
ingredients["pasta"] = 600
```

### Duplicate Keys

* Dictionaries **cannot have duplicate keys**.
* If the same key appears multiple times, the **most recent value overwrites the previous value**.

```python id="c8y4zn"
ingredients = {
    "garlic": 3,
    "garlic": 5
}
```

Result:

```python id="w9k3pt"
{"garlic": 5}
```

* Duplicate keys **do not cause an error**; they silently overwrite earlier values.

### Key Takeaways

* **Dictionary** = collection of key-value pairs
* `{}` = creates a dictionary
* `key: value` = key-value pair
* `dict["key"]` = access a value
* `.keys()` = all keys
* `.values()` = all values
* `.items()` = all key-value pairs
* `dict["new_key"] = value` = add a pair
* `dict["existing_key"] = new_value` = update a value
* **Duplicate keys overwrite previous values**
* Dictionary keys are used for lookup instead of numeric indexes

# Python Sets and Tuples – Review Summary

### Sets

* A **set (`set`)** stores **unique values**.
* Duplicate values are automatically removed.
* Useful for:

  * Removing duplicates
  * Tracking unique items
  * Fast membership/search operations
* Sets are **mutable**: values can be added or removed, but individual elements cannot be changed.
* Sets are **unordered** and do not have indexes.

```python id="7p3h1q"
ingredients = {"pasta", "tomato", "garlic", "pasta"}
# {"pasta", "tomato", "garlic"}
```

### Creating a Set

* Sets use **curly brackets `{}`** without key-value pairs.

```python id="4m8x2c"
ingredients_set = {"pasta", "tomato", "garlic"}
```

* Dictionaries also use `{}`, but dictionaries contain **colons `:`** between keys and values.

```python id="6z9w1k"
# Set
{"pasta", "tomato"}

# Dictionary
{"pasta": 500}
```

### Converting to a Set

* Use `set()` to convert another data structure into a set.
* This process is called **casting**.

```python id="2v5k7m"
ingredients_set = set(ingredients_list)
```

* Converting a list to a set automatically removes duplicates.

### Set Limitations

* Sets have **no indexes**.
* Cannot access elements by position:

```python id="9c4w6y"
ingredients_set[0]  # Error
```

### Sorting a Set

* `sorted()` can sort set values.
* It returns a **list**, not a set.

```python id="5q8n3x"
sorted(ingredients_set)
```

* Result is a list of unique values in sorted order.

---

# Tuples

### Tuples

* A **tuple (`tuple`)** is an **ordered, immutable** collection.
* **Immutable** means its values cannot be:

  * Changed
  * Added
  * Removed
* Useful when data should remain unchanged, such as:

  * Coordinates/location information
  * Identifiers
  * Fixed configuration data

### Creating a Tuple

* Use **parentheses `()`** with comma-separated values.

```python id="1n6k4p"
serving_sizes = (2, 4, 6, 8)
```

* Can also convert another data structure using `tuple()`.

```python id="8x2m5q"
tuple(my_list)
```

### Accessing Tuples

* Tuples are ordered, so elements can be accessed using indexes like lists.
* Indexing starts at **0**.

```python id="3j7v9d"
serving_sizes[1]
```

### Set vs. Tuple

| Feature    | Set           | Tuple       |
| ---------- | ------------- | ----------- |
| Syntax     | `{}`          | `()`        |
| Ordered    | ❌ No          | ✅ Yes       |
| Indexed    | ❌ No          | ✅ Yes       |
| Duplicates | ❌ No          | ✅ Yes       |
| Mutable    | ✅ Add/remove  | ❌ Immutable |
| Main use   | Unique values | Fixed data  |

### Key Takeaways

* **Set** = unique, unordered collection
* `set()` = converts data to a set
* Sets automatically remove duplicates
* Sets have **no indexes**
* `sorted(set)` = returns a sorted **list**
* **Tuple** = ordered, immutable collection
* `()` = creates a tuple
* Tuples support indexing
* `tuple()` = converts data to a tuple
* Use tuples when data should **not be modified**
