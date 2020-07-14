# Intro To Python III

## The Four Pillars of OOP

Encapsulation
Abstraction
Inheritence
Polymorphism

## Defining Our First Class

It is easy to see why Python is known as a “clean” language. When we want to do something in Python, well, we just do it!

The simplest class in Python 3 looks like this:

```python
class MyFirstClass:
    pass
```

We are now writing object-oriented code in Python. We define the class by starting with the reserved class keyword. Then, we write the name of the class and terminate the line with a colon.

Note: PEP 8 recommends that classes be named using CamelCase notation (start with a capital letter and any subsequent words also start with a capital letter).

After the class definition, we have the contents of the class indented below. In Python, indentation is used, rather than braces or brackets to delimit the class definition. In our example, we simply added the pass keyword to indicate that no further action be taken. This is acting essentially as a placeholder.

## Instantiating a Class

So we’ve defined a class, but we haven’t actually done anything with it. It would be like creating a blueprint for a house but never building the house. In order to “create the house”, we have to instantiate the class.

```python
>>> class MyFirstClass:
...     pass
...
>>> a = MyFirstClass()
>>> b = MyFirstClass()
>>> print(a)
<__main__.MyFirstClass object at 0x107dcf340>
>>> print(b)
<__main__.MyFirstClass object at 0x107d3f670>
>>>
```

First, we defined `MyFirstClass` in the interpreter. Then, we store instances of the class in variables `a` and `b`. Finally, we printed out a and b. Notice that when we print out `a` and `b`, we can see that those objects are of type `MyFirstClass` and are stored at two unique memory addresses.

As you can see, creating an instance of a class is as simple as typing the class name followed by a pair of parentheses. Even though it looks just like we are calling some function `MyFirstClass()`, we are actually calling the `__init__()` function that creates all of our class’s attributes and assigns them their initial values. If we don’t define our own, we inherit `__init__()` from the base Object class.

By printing the objects, Python tells us which class the objects are and what memory address they live at. We don’t actually use the memory addressed but this shows that we did in fact create two distinct objects in memory.

## Learn to demonstrate usage of **init**, **str**, and **repr** when defining a class in Python

### init

Most object-oriented languages have the concept of a constructor. A constructor is a special method that initializes an object when it is created.

Note: Python is unique in that it has a constructor method and an initialization method. However, the constructor method is only used if you are doing something rare and exotic. We will focus on the initialization method here.

The `__init__` method is just like any other method except for its special name. The leading and trailing double underscores denote that this is a special method that the Python interpreter will treat as a special case.

Let’s create a Student class and define an `__init__` method on it.

```python
>>> class Student:
...     def __init__(self, first_name, last_name):
...          self.first_name = first_name
...          self.last_name = last_name
...
>>>
```

Notice the first argument self that is passed into the `__init__` method. This is the primary difference between methods defined on an object and a normal function. All methods have one required argument. Conventionally, we name this argument self (although, in reality, we could name it anything we wanted). The self argument is simply a reference to the object that the method is being invoked on.

The next two arguments that we pass into the `__init__` method, we are calling first_name and last_name. Notice in the body of the method, we are storing the values of those arguments in attributes on the object itself.

Now, we have a blueprint for a Student object, but we haven’t actually created any instances of a Student yet. Let’s do that now:

```python
>>> student = Student("John", "Lennon")
>>> print(student.first_name, student.last_name)
John Lennon
>>> print(student)
<__main__.Student object at 0x105608340>
>>>
```

What do you think would happen if we try to instantiate a Student class without passing in the first_name and last_name arguments? Let’s try it out:

```python
>>> student = Student()
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: __init__() missing 2 required positional arguments: 'first_name' and 'last_name'
>>>
```

Notice that the error message tells us that we are missing two positional arguments that are required to instantiate the Student object.

Whenever you define a class, the `__init__` method is where you define the initialization behavior required to create a new instance of that class.

### str

The `__str__` method is special just like `__init__`. The `__str__` method is supposed to return a string representation of an object (which is useful for debugging).

For an example, let’s look at the `__str__` method that is defined for Time objects:

```python
### inside class Time:

def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
```

When you print an object, Python calls the `__str__` method to determine what to print out. Compare the `__str__` method definition above to the output below.

```python
>>> time = Time(3, 17)
>>> print(time)
03:17:00
```

Whenever you are defining a new class, you should start by defining the `__init__` method so you can instantiate objects. The next thing you should do is define the `__str__` method so you have useful information for debugging.

### repr

`__repr__` is similar to `__str__` in that it will return a printable representation of the object. However, with `__repr__` it will return one of the ways possible to create the object.

For example, let’s say we have a Point class like this:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

Below, you can see how the interpreter represents an instance of Point:

```python
>>> point = Point(1, 2)
>>> point
<__main__.Point object at 0x10d814340>
>>>
```

As you can see, this isn’t that helpful as a developer. What we might really want to know is how we could recreate that object. By defining a `__repr__` method on the Point class, we can do that:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Point(x=%s, y=%s)' % (self.x, self.y)
```

Now, look at how the interpreter returns a representation of the object when we access it:

```python
>>> point = Point(1, 2)
>>> point
Point(x=1, y=2)
>>>
```
