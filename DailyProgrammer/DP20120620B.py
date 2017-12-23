"""
You are given a list of 999,998 integers, which include all the integers between 1 and 1,000,000 (inclusive on both
ends) in some unknown order, with the exception of two numbers which have been removed. By making only one pass through
the data and using only a constant amount of memory (i.e. O(1) memory usage), can you figure out what two numbers have
been excluded?

Note that since you are only allowed one pass through the data, you are not allowed to sort the list!

EDIT: clarified problem

    Thanks to Cosmologicon for suggesting this problem at /r/dailyprogrammer_ideas? Do you have a problem you think
    would be good for us? Why not head over there and suggest it?
"""

from random import shuffle
from math import sqrt


def main():
    """ inspired by a genius solution from the reddit post """
    sums = sum([n for n in range(1, 1000000+1)])
    sq_sums = sum([n*n for n in range(1, 1000000+1)])

    test = list(range(1, 1000000+1))
    shuffle(test)
    test = test[2:]

    for t in test:
        sums -= t
        sq_sums -= t*t

    a = 1
    b = -sums
    c = ((sums ** 2) - sq_sums) / 2

    print(int((-b + sqrt((b ** 2) - (4 * c))) / 2), int((-b - sqrt((b ** 2) - (4 * c))) / 2))


if __name__ == "__main__":
    main()
