"""
Today you should implement a function that all of us programmers depend heavily on, but most never give a second thought
as to how it's actually coded: the square root function.

Write a function that given a number as input, will return the square root of that number, in floating point.

Obviously, you are not allowed to use the library version of sqrt() in the implementation of your function. Also, stay
away from log() and exp(). In fact, don't use any mathematical functions that aren't the basic arithmetic ones
(addition, subtraction, multiplication, division) or bit operations (though you can of course still use operators that
compares numbers with each other, like "less than", "equal to", "more than", etc.)
"""
from math import sqrt


class EvenNotation:
    def __init__(self, n):
        self.n = n

    def __format__(self, format_spec):
        number = ('{:' + format_spec + '}').format(self.n)
        coeff, exp = number.split('e')
        if int(exp) % 2 == 0:
            return number
        else:
            coeff = coeff.replace('.', '')
            coeff = coeff[:2] + '.' + coeff[2:]
            exp = str(int(exp) - 1)
            return coeff + 'e' + exp


def my_sqrt(n):
    rough = rough_sqrt(n)

    baby = babylonian_sqrt(rough, n)
    print('babylonian = {}'.format(baby))

    bakh = bakhshali_sqrt(rough, n)
    print('bakhshali  = {}'.format(bakh))


def rough_sqrt(n):
    """https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Rough_estimation"""
    sci = '{:e}'.format(EvenNotation(n))
    coeff, exp = sci.split('e')
    coeff, exp = int(coeff.split('.')[0]), int(exp)
    exp /= 2
    if coeff ** 2 > 10:
        return 6 * (10 ** exp)
    else:
        return 2 * (10 ** exp)


def babylonian_sqrt(rough, n):
    """https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method"""
    iterations = 10
    for _ in range(iterations):
        rough = 0.5 * (rough + (n / rough))
    return rough


def bakhshali_sqrt(rough, n):
    """https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Bakhshali_method"""
    iterations = 10
    for _ in range(iterations):
        a = (n - (rough ** 2)) / (2 * rough)
        b = rough + a
        rough = b - ((a ** 2) / (2 * b))
    return rough


def main():
    number = 125348
    print('Standard   = {}'.format(sqrt(number)))
    my_sqrt(number)


if __name__ == "__main__":
    main()
