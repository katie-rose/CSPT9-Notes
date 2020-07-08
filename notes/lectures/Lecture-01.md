```python
print('Hello World')
```

..and here, we, go.

_Preclass videos:_

• Python Basics - https://youtu.be/KtYGuqq_irU
• Python Collections - https://youtu.be/fxDQzub2AtI
• (optional) Example Python Project - https://youtu.be/f3YAP5NsRYI

_Links for today_
• Main site - https://www.python.org/
• Official docs - https://docs.python.org/3/
• Python-to-JS cheatsheet - https://github.com/LambdaSchool/CS-Wiki/wiki/Javascript-Python-cheatsheet
• Tutorials with interactive examples - https://www.learnpython.org/en/
• Install guide on CS Wiki - https://github.com/LambdaSchool/CS-Wiki/wiki/Installing-Python-3-and-pipenv
• Independent project - https://github.com/LambdaSchool/Intro-Python-I

---

Quotes

- Don't mix and match "" and ''
  - Single quotes only gang

```python
name = 'Katie'
hi = 'Hello ' + name
print(hi)
```

This creates `Hello Katie`. A little different than JS which requires explicit typecasting in certain circumstances.

**Lists**
_Ordered Values_

```python
lst = [1, 4, 10, "dog", 23]
print(list)

lst.append(3.5)
print(list)
```

Creates `[1, 4, 10, 'dog', 23, 3.5]`. Appends adds an item to the end of a list, in this case 3.5.

```python
lst = [1, 4, 10, "dog", 23]
print(list)

lst.append(3.5)
lst.append([100,200,300])
print(list)
```

Creates `[1, 4, 10, 'dog', 23, 3.5, [100, 200, 300]]`. Adds another set of items to the end of the original set of items.

`lst.insert` = Inserts an item.

`lst.remove` = Wait for it.. removes an item.

```python
for elm in lst:
    print(elm)
```

Prints every element in the list.

```python
1
4
hello
10
dog
23
3.5
[100, 200, 300]
```

**Dictionary**
_Key, value pairs_

`dict = {'key0':value0, 'key1':value1}` = Dictionary format.

```python
book={"peanut butter":12, "and chocco": 34}
print(book)
```

This prints `{'peanut butter': 12, 'and chocco': 34}`.

```python
val = book["peanut butter"]
print(val)
```

This is how we access a value from a dictionary. Prints `12`.

- F Strings
  - Short name for "formatted string literals".

```python
name = "Katie"
print(f"My name is: {name}")
```
