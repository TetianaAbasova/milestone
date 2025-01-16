# -*- coding: utf-8 -*-
"""9_2_assignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1t8haxL15EOZqVJbHZXhqpdF7vjKVNItj

# Assignment 9.2

> Replace all TODOs with your code. Do not change any other code.
"""

# Do not edit this cell

from typing import List
import math

"""## Descriptive statistics

In this assignment, we will write the functions to calculate the basic statistics from scratch, not using numpy.

### Task 1

Let's start simple: write a function `mean` that calculates the average of the list.

$$\mu = \frac{{\sum_{i=1}^n x_i}}{{n}}$$
"""

def mean(li: List[float]) -> float:
    if not li:
      return 0
    mean_value = sum(li)/len(li)
    return mean_value

assert mean([1., 2., 3.]) == 2.
assert mean([1., 1., 2., 0.]) == 1.

"""### Task 2

Now let's calculate variance (dispersion). You may use the `mean` function implemented before.

$$V = \frac{{\sum_{i=1}^n (x_i - \mu)^2}}{{n}}$$
"""

def variance(li: List[float]) -> float:
    if not li:
      return 0
    mean_value = sum(li)/len(li)
    variance_value = sum((x - mean_value)**2 for x in li) / len(li)
    return variance_value


assert variance([1., 1., 1.]) == 0.
assert variance([1., 2., 3., 4.]) == 1.25

"""### Task 3

The standard deviation is easy once you get the variance:

$$\sigma = \sqrt{V}$$
"""

def std(li: List[float]) -> float:
    if not li:
      return 0
    mean_value = sum(li)/len(li)
    variance_value = sum((x - mean_value)**2 for x in li) / len(li)
    return math.sqrt(variance_value)


assert std([1., 1., 1.]) == 0.
assert std([1., 2., 3., 4.]) == 1.25**0.5

"""### Task 4

**Median**

The median is the middle value in a sorted dataset. If the dataset has an odd number of values, the median is the value at the center. If the dataset has an even number of values, the median is the average of the two middle values.
"""

def median(li: List[float]) -> float:
    if not li:
        return 0
    n = len(sorted(li))

    if n % 2 == 1:
        return sorted(li)[n//2]
    else:
        return (sorted(li)[n//2-1]+sorted(li)[n//2]) / 2


assert median([1., 1., 1.]) == 1.
assert median([1., 4., 3., 2.]) == 2.5

"""## Measure performance

Sometimes, apart from theoretical, algorithmic complexity, it's a good idea to compare the runtime of two algorithms empirically, i.e., run the code many times and time it.

In Python's standard library, we have [timeit](https://docs.python.org/3/library/timeit.html) module that does exactly that.

Let's compare the runtime of your implementations and numpy. Use the provided setup code:
"""

# generate data for tests

setup = '''
import random
import numpy as np

arr = np.random.rand(10_000) * 100
li = [random.random() * 100 for _ in range(10_000)]
'''

# pass your function to timeit module
funcs = {
    'mean': mean,
    'variance': variance,
    'std': std,
    'median': median,
}

"""### Task 5

Complete Python statements to compare your functions to numpy. Use `li` for your function and `arr` for numpy functions.
"""

stmt_mean_custom = 'mean(li)'
stmt_mean_np = 'np.mean(arr)'

stmt_var_custom = 'variance(li)'
stmt_var_np = 'np.var(arr)'

stmt_std_custom = 'std(li)'
stmt_std_np = 'np.std(arr)'

stmt_median_custom = 'median(li)'
stmt_median_np = 'np.median(arr)'

"""### Task 6

Measure average exec time of your statements with `timeit` module. As your submission, fill out the table with results (rounded to 2 decimal places)
"""

import timeit
mean_custom = timeit.timeit(stmt=stmt_mean_custom, setup=setup, globals=funcs, number=10_000)
mean_np = timeit.timeit(stmt=stmt_mean_np, setup=setup, globals=globals(), number=10_000)

var_custom = timeit.timeit(stmt=stmt_var_custom, setup=setup, globals=funcs, number=10_000)
var_np = timeit.timeit(stmt=stmt_var_np, setup=setup, globals=globals(), number=10_000)

std_custom = timeit.timeit(stmt=stmt_std_custom, setup=setup, globals=funcs, number=10_000)
std_np = timeit.timeit(stmt=stmt_std_np, setup=setup, globals=globals(), number=10_000)

median_custom = timeit.timeit(stmt=stmt_median_custom, setup=setup, globals=funcs, number=10_000)
median_np = timeit.timeit(stmt=stmt_median_np, setup=setup, globals=globals(), number=10_000)

print(f"Time per 10000 executions, secs")
print(f'Func\t\tCustom\t\tNumpy')
print(f'mean\t\t{mean_custom:.2f}\t{mean_np:.2f}')
print(f'var\t\t{var_custom:.2f}\t{var_np:.2f}')
print(f'std\t\t{std_custom:.2f}\t{std_np:.2f}')
print(f'median\t\t{median_custom:.2f}\t{median_np:.2f}')

"""Time per 10000 executions, secs

| Func       | Custom | Numpy |
| ---------- | ------ | ----- |
| mean       | 0.54   | 0.10  |
| var        | 13.39  | 0.32  |
| std        | 13.17  | 0.32  |
| median     | 55.07  | 1.90  |
"""