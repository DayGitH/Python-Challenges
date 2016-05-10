"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from time import time

startTime = time()

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

index = 1000000
C = 10

fact = factorial(C)
print(index)
total_pos = [i for i in range(C)]
print(total_pos)

answer = ''
for n in range(C,1,-1):
    if fact != 2:
        fact = int(fact/n)
        div = int((index-1)/fact)
    else:
        div = int((index)/fact)
    answer += str(total_pos[div])
    total_pos.pop(div)
    index -= (div * fact)
answer += str(total_pos[0])
print(answer)

print(time() - startTime)