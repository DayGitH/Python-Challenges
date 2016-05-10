"""
Your task today is show the implementation of two sorting algorithms Stooge sort
[http://en.wikipedia.org/wiki/Stooge_sort] and Bogosort [http://en.wikipedia.org/wiki/Bogosort] in anyway you like!
"""

import numpy as np


def create(n):
    return list(np.random.permutation([i for i in range(n)]))


def check(l):
    hold = -1
    for i in l:
        if i > hold:
            hold = i
        else:
            return False
    else:
        return True


def bogosort(l):
    n = 0
    while not check(l):
        print(l)
        l = list(np.random.permutation(l))
        n += 1
    return l, n


def stoogesort(l):
    if l[0] > l[-1]:
        l[0], l[-1] = l[-1], l[0]

    length = len(l)
    if length >= 3:
        l[:int(2*length/3)] = stoogesort(l[:int(2*length/3)])
        l[int(length/3):] = stoogesort(l[int(length/3):])
        l[:int(2*length/3)] = stoogesort(l[:int(2*length/3)])

    return l

if __name__ == '__main__':
    c = create(21)
    print(c)
    print(stoogesort(c))
