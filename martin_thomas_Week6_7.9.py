import numpy as np

array = np.arange(1, 16).reshape(3, 5)

print(array)

# Part A

row2 = array[1, :]

print('Exercise 7.9 Part A:', row2)

# Part B

column5 = array[:, 4]

print('Exercise 7.9 Part B:', column5)

# Part C

rows01 = array[0:2, :]

print('Exercise 7.9 Part C:', rows01)

# Part D

columns234 = array[:, 2:5]

print('Exercise 7.9 Part D:', columns234)

# Part E

elements14 = array[1, 4]

print('Exercise 7.9 Part E:', elements14)

# Part F

rows12cols024 = array[1:3, [0, 2, 4]]

print('Exercise 7.9 Part F:', rows12cols024)
