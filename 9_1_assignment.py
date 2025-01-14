# -*- coding: utf-8 -*-
"""9_1_assignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jVJrNkzgfKrKqhVKE6f8lwm-_WcrGyRM

# Assignment 9.1

> Replace all TODOs with your code. Do not change any other code.
"""

# Do not edit this cell

import numpy as np
import pandas as pd

"""## Numpy

### Task 1

Create a 1D numpy array with elements [1, 2, 3, 4, 5]. Do it in two different ways.
"""

res = np.arange(1, 6)

print(res)

res2 = np.array([1,2,3,4,5])

print(res2)

"""### Task 2

Create a 2D numpy array with shape (3, 5) filled with random integers between 1 and 100.
"""

res3 = np.random.randint(1, 101, size=(3, 5))

print(res3)

"""### Task 3

Print the first row of array `res3`.
"""

print(res3[0])

"""### Task 4

Access the last column of array `res3`. Assume that the array may be of any 2D shape.
"""

print(res3[:, -1])

"""### Task 5

Find the min, max, and sum of elements of the second column of array `res3`.
"""

# Min
res_min = np.min(res3[:, 1])

print('min =', res_min)

# Max
res_max = np.max(res3[:, 1])

print('max =', res_max)

# Sum
res_sum = np.sum(res3[:, 1])

print('sum =', res_sum)

"""### Task 6

Tabulate the function

$$f(x) = e^{2x}$$

on interval `[0, 1]` with step 0.1.

By "tabulate" we mean that we want to have a table (1D array), where on the first position we will have the function value for 0, on the second position 0.1, and so on.
"""

x = np.arange(0, 1.1, 0.1)
f_x = np.exp(2 * x)

print(f_x)

"""## Pandas

We will be working on the classic dataset for beginner data scientists: Titanic passengers.

### Task 7

Load the dataset from the following URL: https://web.stanford.edu/class/cs102/datasets/Titanic.csv
"""

import os


file_name = "Titanic.csv"
file_url = "https://web.stanford.edu/class/cs102/datasets/Titanic.csv"

if not os.path.exists(file_name):
    print("File does not exist!")

    df = pd.read_csv(file_url)

    df.to_csv(file_name, index=False)
    print("file downloaded")

else:
    print("File Already Exists!")

    df = pd.read_csv(file_name)

"""### Task 8

Let's see the series/columns present in the data frame.

Also, let's inspect the first ten rows of data.
"""

print(df.columns)

print(df.head(10))

"""### Task 9

Add a new column - full name - it should be a concat of the first and last name.
"""

df["full name"] = df["first"] + df["last"]
print(df.columns)

"""### Task 10

Remove the two original columns - last, first.
"""

df.drop([df.columns[0], df.columns[-1]], axis=1, inplace=True)
print(df.columns)

"""### Task 11

Calculate the total number of survivors in the dataset.
"""

survived_mask = df['survived'] == 'yes'
survived_count = survived_mask.sum()
print(f"Total number of survivors: {survived_count}")

