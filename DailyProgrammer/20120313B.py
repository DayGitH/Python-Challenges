"""
At McDonalds' Restaurants, the Chicken McNugget meals are available in sizes of 6 McNuggets, 9 McNuggets, or 20
McNuggets. A number is a McNugget number if it can be the sum of the number of McNuggets purchased in an order (before
eating any of them). Henri Picciotto devised [https://en.wikipedia.org/wiki/Coin_problem#McNugget_numbers] the math of
McNugget numbers in the 1980s while dining with his son at McDonald's, working the problem out on a napkin.
Your task is to determine all numbers that are not McNugget numbers.

source: programmingpraxis.com
"""

def mcnugget(n):
    check = lambda n: (n % 3 == 0 and n != 3)
    while n >= 0:
        if check(n):
            return True
        n -= 20
    return False

print([n for n in range(100) if not mcnugget(n)])
"""Heavily inspired by u/prophile's solution"""