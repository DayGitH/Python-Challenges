"""
Write a function that takes two arguments a and b, and finds all primes that are between a and a + b (specifically,
find all primes p such that a ? p < a + b). So for instance, for a = 1234 and b = 100, it should return the following
15 primes:
1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327

The sum of those primes are 19339. The number of primes for a = 9! and b = 8! is 3124 and the sum of those primes is
1196464560.

How many primes are there for a = 16! and b = 10!, and what is their sum?

Note 1: In this problem, n! refers to the factorial [http://en.wikipedia.org/wiki/Factorial] of n, 1*2*3*...*(n-1)*n,
so 9! is equal to 362880.
Note 2: All numbers and solutions in this problem fit into 64-bit integers.
EDIT: changed some incorrect numbers, thanks ixid!
"""

import random


def is_prime(n):
    """https://stackoverflow.com/questions/15285534/isprime-function-for-python-language"""
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True


def eratosthene(n1, n2):
    """from another project"""
    L1 = [i for i in range(2, n2+1) if i%2!=0 or i%3!=0 or i%5!=0]
    i = 0
    while L1[i]**2 <= L1[-1]:
        L2 = [a for a in L1 if a%L1[i] != 0 or a <= L1[i]]
        L1 = L2  # avoid assignment issues between L1 and L2
        i += 1
    return [i for i in L1 if i > n1]


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    """is_prime solution too slow for inp1=16! inp2=10!
       eratosthene soluution runs out of memory
    """
    inp1 = factorial(16)
    inp2 = factorial(10)
    # inp1 = 1234
    # inp2 = 100

    p_list = eratosthene(inp1, inp1+inp2)

    print(p_list)
    # print(len(p_list), sum(p_list))
    # count = 0
    # summ = 0
    # for i in range(inp1+1, inp1+inp2, 2):
    #     if is_prime(i):
    #         count += 1
    #         summ += i
    # print(count, summ)
