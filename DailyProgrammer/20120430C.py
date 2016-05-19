"""
The prime HP reached starting from a number , concatenating its prime factors, and repeating until a prime is reached.
If you have doubts, refer the article here [http://mathworld.wolfram.com/HomePrime.html]

write a function to calculate the HP of a given number.

Also write a function to compute the Euclid-Mullin sequence [http://mathworld.wolfram.com/Euclid-MullinSequence.html].
"""

import numpy as np


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


def factorize(n):
    active_num = n

    factors = []
    n = 2
    while active_num != 1:
        if active_num % n == 0:
            active_num /= n
            factors.append(str(n))
        else:
            n += 1
    return factors


def home_prime(n):
    while not is_prime(n):
        n = int(''.join(factorize(n)))
    return n


def euclid_mullin(n):
    e_m = []
    for i in range(n):
        e_m.append(int(factorize(np.prod(e_m)+1)[0]))
        print(e_m)
    return e_m

if __name__ == '__main__':
    print(home_prime(5))
    euclid_mullin(9)