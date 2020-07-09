# Intro To Python

![picture 3](../images/363f4406f5a4187b84a398798d30fad7325dc9bb3e3e1f3bcb99786a981d0f45.png)

## Arithmetic Operators

Operators are special symbols that represent computations like addition and multiplication.

- `**`: exponentiation
- `^`: exclusive-or (bitwise)
- `%`: modulus
- `//`: divide with integral result (discard remainder)

```python
>>> 30 + 6
36
>>> 40 - 4
36
>>> 6 * 6
36
>>> 72 / 2
36.0
>>> 6**2
36
>>> 36 % 35
1
>>>
```

## Exponentiation(\*\*)

Raises the first number to the power of the second.

The ** operator does exponentiation. a ** b is a raised to the b power. The same \*\* symbol is also used in function argument and calling notations, with a different meaning (passing and receiving arbitrary keyword arguments).

```python
f4(city="Berkeley", population=121240, founded="March 23, 1868")

d = {
    "monster": "goblin",
    "hp": 3
}

# How do you have to modify the f4 call below to make this work?
f4(**d)
```

### **Python Arbitrary Arguments**

Python allows us to have the arbitrary number of arguments. This is especially useful when we are **not sure in the advance** that how many arguments, the function would require.

We define the arbitrary arguments while defining a function using the **asterisk (\*)** sign.

```python
a = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?
print(f2(*a))    # Should print 22
```

## Strings, Integers, and Floats

- Ints (Integers): (6) - a whole number/ positive or negative. No decimals.
- Floating or Floating Point: 5.2, 1.333, 0.0 - this takes up a lot more space than a whole number. If we include decimals, there are an infinite number of numbers between two whole numbers.
- String: `'Hello, World!'`

Python can tell you:

```python
>>> type(6)
<class 'int'>
>>> type(36.0)
<class 'float'>
>>> type('Hello, World!')
<class 'str'>
>>>
```

## Variables

Containers that store data to be used later. Hold numbers, booleans, strings, etc. It is a named symbol that holds a value. Kind of like a safe.

```python
X = 500
tomHardy = 1
Print (tomHardy+ x) = 501
```

## Whitespace

![picture 1](../images/f05a0d45f8d2480d8ea83d8a2ce5681461500fde84a10c5d799fe33c96abc5a2.png)

No brackets. You can use tabs, but you can't mix tabs and spaces.

### Python Collections

**Lists**

- Group of items we reference by index
- Mutable, we can change the content
- Can have duplicate Items
- Can iterate through it
- Passed by reference

```python
############################################
#CREATE LIST
############################################

my_colors = ["red", "orange", "yellow"]

############################################
#ADD ITEMS
############################################
my_colors = ["red", "orange", "yellow"]

#add to end
my_colors.append("green")
#["red", "orange", "yellow", "green"]

#insert at i (or index 2)
my_colors.insert(2, "blue")
#["red". "orange", "blue", "yellow"]

############################################
#REMOVE ITEMS
############################################
my_colors = ["red", "orange", "yellow"]

#removes item
my_colors.remove("orange")
#["red", "yellow"]

#removes last item
my_colors.pop()
#["red", "orange"]

#removes item at i (or index 2)
del my_colors[2]
#["red", "orange"]

#traverse
for i in range( 0 , len(my_colors) ):
	#access an item
	print( my_colors[i] )

############################################
#LIST SLICES
############################################
my_colors = ["red", "yellow", "orange"]

#keep items at indexes 0 through not including 2
primary_colors = my_colors[0:2]
#["red", "yellow"]

#keep items at indexes 1 through the end
primary_colors = my_colors[1:]
#["orange", "yellow"]

#keep items from the beginning up to index 2
primary_colors = my_colors[:2]
#["red", "orange"]

#creates a copy of a list
primary_colors = my_colors[:]
#["red", "yellow", "orange"]

############################################
#FILTER LIST
############################################
my_colors = ["red", "orange", "yellow"]

#filter out all colors with names less than 5 chars
new_colors = [c for c in my_colors if len(c) < 5]
#["red"]
```

**List Comprehensions**

List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated.

```python
x = [i+1 for i in range(5)]
#[1,2,3,4,5]

#if statement
x = [1,2,3,4,5,6,7,8,9,10]
y = [int(i) for i in x if int(i) % 2 == 0]
#[2,4,6,8,10]

#if else statement
x = [1,2,3,4,5,6,7,8,9,10]
y = [int(i) if int(i)%2 == 0 else 'nope' for i in x]
#['nope', 2, 'nope', 4, 'nope', 6, 'nope', 8, 'nope', 10]
```

**Tuples**

- Group of items we reference by index
- Not Mutable
- Can have duplicate Items
- Can iterate through it
- Passed by reference

```python
############################################
#CREATE TUPLE
############################################

my_animals = ("dog", "cat", "fish")

#create tuple with 1 element
my_taco = ("cat",)

############################################
#GET TUPLE LENGTH
############################################
my_animals = ("dog", "cat", "fish")

len( my_animals )
#3

############################################
#TRAVERSE THE TUPLE
############################################

for animal in my_animals:
	print( animal )

############################################
#NOT ALLOWED
############################################

#add items
#change items
#remove items
```

**Sets**

- Unordered group of items
- Semi-mutable (can add, can't change)
- No duplicate items
- Can iterate through it
- Passed by reference

```python
############################################
#CREATE IT
############################################

my_cities = {"Dallas", "Houston", "Austin"}

############################################
#ADD ITEMS
############################################
my_cities = {"Dallas", "Houston", "Austin"}

#add a single item
my_cities.add("San Antonio")
#{"Dallas", "Houston", "Austin", "San Antonio"}

#add multiple items
my_cities.update(["Boerne", "Galveston"])
#{"Dallas", "Houston", "Austin", "Boerne", "Galveston"}

############################################
#REMOVE ITEMS
############################################
my_cities = {"Dallas", "Houston", "Austin"}

#remove by value
my_cities.remove("Houston")
#{"Dallas", "Austin"}

#remove last item that was added to the set
my_cities.pop()
#{"Dallas", "Houston"}

############################################
#GET SET LENGTH
############################################
my_cities = {"Dallas", "Houston", "Austin"}

len(my_cities)
#3

############################################
#NOT ALLOWED
############################################

#change items
```

**Dictionaires**

Group of values we reference through their keys.

- Group of values we reference through their keys
- Mutable
- Can have duplicate items
- Not iterable
- Passed by reference

```python
############################################
#CREATE DICTIONARY
############################################

my_grades = {
	#"key": "value"
	"Math": 42,
	"Science": 42,
	"English": 42,
	"History": 42
}

############################################
#ADD ITEMS
############################################
my_grades = {"Math": 42, "Science": 42, "English": 42, "History": 42}

#add new item assuming "Art" doesn't already exist
my_grades["Art"] = 0

############################################
#CHANGE ITEMS
############################################
my_grades = {"Math": 42, "Science": 42, "English": 42, "History": 42}

#update value of existing item
my_grades["Math"] = 17

############################################
#REMOVE ITEMS
############################################
my_grades = {"Math": 42, "Science": 42, "English": 42, "History": 42}

#remove a specific item
my_grades.pop("Science")
#{"Math": 42, "English": 42, "History": 42}

#remove last item
my_grade.popitem()
#{"Math": 42, "Science": 42, "English": 42}

############################################
#ACCESS VALUES
############################################
my_grades = {"Math": 42, "Science": 42, "English": 42, "History": 42}

my_grades.get("History")
#42

```
