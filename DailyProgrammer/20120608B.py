"""
Find all the subsets of a set of non-negative integers where the largest number is the sum of the remaining numbers, and
return a count of the number of them. For instance, for the set { 1, 2, 3, 4, 6 } the subsets are 1+2=3, 1+3=4, 2+4=6,
and 1+2+3=6, so the result is 4 subsets. Apply your program to the set { 3, 4, 9, 14, 15, 19, 28, 37, 47, 50, 54, 56,
59, 61, 70, 73, 78, 81, 92, 95, 97, 99 }.

Your task is to write a program to solve the challenge.

Bonus: you might like to apply your solution to the set of prime numbers less than 2 ** 10

taken from http://challenge.greplin.com/
"""

from itertools import combinations
from collections import defaultdict


def eval_and_check_sum(comb, test):
    return int(sum(comb) in test)


def main():
    test = [3, 4, 9, 14, 15, 19, 28, 37, 47, 50, 54, 56, 59, 61, 70, 73, 78, 81, 92, 95, 97, 99]
    count = 0

    single_line_count = sum([eval_and_check_sum(comb, test)
                             for n in range(2, len(test))
                             for comb in combinations(test[:-1], n)])
    print(single_line_count)

    for a in range(2, len(test)):
        for b in combinations(test[:-1], a):
            if sum(b) in test:
                count += 1
    print(count)


if __name__ == "__main__":
    main()
