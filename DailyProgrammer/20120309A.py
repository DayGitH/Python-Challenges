'''
Input: a number

Output : the next higher number that uses the same set of digits.
'''

import itertools

inp = input('Input number: ')
perm = itertools.permutations(inp)

for i in perm:
    n = int(''.join(i))
    if n > int(inp):
        print(n)
        break

