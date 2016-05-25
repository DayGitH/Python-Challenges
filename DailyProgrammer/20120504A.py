"""
Take an array of integers and partition it so that all the even integers in the array precede all the odd integers in
the array. Your solution must take linear time in the size of the array and operate in-place with only a constant
amount of extra space.

Your task is to write the indicated function.
"""

import numpy.random as nprnd

int_list = list(nprnd.randint(100, size=10000))

print(int_list)

even = lambda x: x%2==0
odd = lambda x: x%2!=0
even_list = list(filter(even, int_list))
odd_list = list(filter(odd, int_list))

res_list = even_list+odd_list

print(res_list)