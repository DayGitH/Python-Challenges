"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

import math

PATH_SIZE = 20
SIZE = PATH_SIZE + 1

# My initial method
array = [[0 for x in range(SIZE)] for x in range(SIZE)]

array[0][0] = 1

for a in range(1,SIZE):
    x = 0
    y = a
    while y >= 0:
        if x == 0:
            array[y][x] = array[y-1][x]
        elif y == 0:
            array[y][x] = array[y][x-1]
        else:
            array[y][x] = array[y-1][x] + array[y][x-1]
        x += 1
        y -= 1

for b in range(1,SIZE):
    x = b
    y = SIZE - 1
    while x < SIZE:
        if y == 0:
            array[y][x] = array[y][x-1]
        else:
            array[y][x] = array[y-1][x] + array[y][x-1]
        x += 1
        y -= 1
print(array[-1][-1])

# Pure mathematical method
# This is 40 choose 20 from binomial algebra
print((math.factorial(2*PATH_SIZE))/(math.factorial(PATH_SIZE)**2))

