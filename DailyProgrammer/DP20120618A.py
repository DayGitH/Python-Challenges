"""
Write a function that takes two arguments, x and y, which are two strings containing Roman Numerals without prefix
subtraction (so for instance, 14 is represented as XIIII, not XIV). The function must return true if and only if the
number represented by x is less than the number represented by y. Do it without actually converting the Roman numerals
into regular numbers.

Challenge: handle prefix subtraction as well.

    Thanks to cosmologicon for the challenge at /r/dailyprogrammer_ideas ! LINK .. If you think you got any challenge
    worthy for this sub submit it there!
"""

import itertools


def compare_roman(inp1, inp2):
    roman = "MDCLXVI"

    if inp1 == inp2:
        return False

    length = max([len(inp1), len(inp2)])
    inp1.ljust(length, '_')
    inp2.ljust(length, '_')

    while inp1[0] == inp2[0]:
        inp1, inp2 = inp1[1:], inp2[1:]

    return roman.index(inp1[0]) > roman.index((inp2[0]))


def main():
    inp1 = 'XCV'
    inp2 = 'CXVIII'
    print(inp1, inp2, compare_roman(inp1, inp2))


if __name__ == "__main__":
    main()
