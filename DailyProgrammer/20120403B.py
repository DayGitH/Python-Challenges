"""
Imagine you are given a function flip() that returns a random bit (0 or 1 with equal probability). Write a program that
uses flip to generate a random number in the range 0...N-1 such that each of the N numbers is generated with equal
probability. For instance, if your program is run with N = 6, then it will generate the number 0, 1, 2, 3, 4, or 5 with
equal probability.

N can be any integer >= 2.
Pseudocode is okay.
You're not allowed to use rand or anything that maintains state other than flip.
Thanks to Cosmologicon for posting this challenge to /r/dailyprogrammer_ideas!
"""

import random
import matplotlib.pyplot as plt
from bitarray import bitarray


def flip():
    return random.getrandbits(1)


def binary_to_int(n):
    out = 0
    for bit in n:
        out = (out << 1) | bit

    return out


def randomize(a):
    for n, i in enumerate(a):
        a[n] = flip()
    return a

number = 200
binary = bin(number)[2:]
a = len(binary) * bitarray('0')

while True:
    a = randomize(a)
    if binary_to_int(a) <= number:
        break

print(binary_to_int(a))


