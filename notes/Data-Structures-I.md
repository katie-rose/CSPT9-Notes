# Data Structures I

## Big O

Big O notation is a way of describing the rate of change in the execution speed of an algorithm when the data size increases. It is the agreed-upon terminology we use to describe how long an algorithm takes to run. It is a way of comparing different algorithm’s efficiencies.

The specific terms of Big O notation describe how fast the runtime grows (relative to the size of the input) with a focus on when the input gets extremely large.

![picture 1](../images/7511c7c252d823b1ceb7682d29b28f48e7abba1dcbd9e0a13d8345cf43b12d8b.png)

Besides the table, it’s also essential to look at the curves of these different run times.

![picture 2](../images/2e001347c2b0c82a9e68c0808ffdf8280b86af9e4aa0ff590e8e2f325aca8ccd.png)

Again, `n` represents the size of the data, and on the chart above, `N` represents the number of operations. This visualization should help illustrate why `O(1)` or `O(log n)` is the most desirable.

## Examples

**Constant Time** `O(1)`

```python
def print_one_item(items):
    print(items[0])
```

No matter how large or small the input is (1,000,000 or 10), the number of computations within the function is the same.

**Linear Time** `O(n)`

```python
def print_every_item(items):
    for item in items:
        print(item)
```

The speed of the algorithms increases at the same rate as the input size. If items has ten items, then the function will print ten times. If it has 10,000 items, then the function will print 10,000 times.

**Quadratic Time** `O(n^2)`

```python
def print_pairs(items):
    for item_one in items:
        for item_two in items:
            print(item_one, item_two)
```

The clue is the nested for loops. These nested for loops mean that for each item in items (the outer loop), we iterate through every item in items (the inner loop). For an input size of n, we have to print n \* n times or n^2 times.
