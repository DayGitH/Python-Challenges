"""
As is well known, the decimal expansion of sqrt(N) when N is not a perfect square, goes on forever and does not repeat.
For instance, sqrt(8) starts out 2.82842712... and never starts repeating itself. This is because when N is not a
perfect square, sqrt(N) is irrational
[http://en.wikipedia.org/wiki/Infinite_descent#Irrationality_of_.E2.88.9Ak_if_it_is_not_an_integer] and all numbers with
repeating decimals are rational
[http://en.wikipedia.org/wiki/Repeating_decimal#Every_repeating_or_terminating_decimal_is_a_rational_number].

However, if instead of using a decimal representation, you use a continued fraction representation
[http://en.wikipedia.org/wiki/Continued_fraction] of sqrt(N) when N is not a perfect square, then it will always have a
repeating period. For instance, this is the beginning of the continued fraction of sqrt(8)
[http://i.imgur.com/WWlFJ.gif]. The pattern of 1,4,1,4,1,4,... will repeat forever (the first integer, the 2, is not
included in the period). A continued fraction with a period like this can be written as [a; [b,c,d,...]], where a is the
first number outside of the fraction, and b, c, d, etc. are the period repeating inside the fraction. For example,
sqrt(8) has a continued fraction representation of [2; [1,4]].

Here are some other continued fraction representations of square roots:

sqrt(2) = [1; [2]]
sqrt(13) = [3; [1, 1, 1, 1, 6]]
sqrt(19) = [4; [2, 1, 3, 1, 2, 8]]
sqrt(26) = [5; [10]]

Let Q(N) be the sum of the numbers in the period for the continued fraction representation of sqrt(N). So Q(19) = 2 + 1
+ 3 + 1 + 2 + 8 = 17 and Q(26) = 10. When N is a perfect square, Q(N) is defined to be 0.

The sum of Q(N) for 1 ≤ N ≤ 100 is 1780.

What is the sum of Q(N) for 1 ≤ N ≤ 50000?

Bonus: If your code for solving this problem includes use of the sqrt() function, solve today's intermediate problem and
use your own implementation of sqrt().
"""

from math import sqrt
from decimal import getcontext, Decimal


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

    # baby = babylonian_sqrt(rough, n)

    bakh = bakhshali_sqrt(rough, n)

    return bakh


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
        rough = Decimal(0.5) * (Decimal(rough) + (Decimal(n) / Decimal(rough)))
    return rough


def bakhshali_sqrt(rough, n):
    """https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Bakhshali_method"""
    iterations = 10
    for _ in range(iterations):
        a = (n - (Decimal(rough) ** 2)) / (2 * Decimal(rough))
        b = Decimal(rough) + Decimal(a)
        rough = Decimal(b) - ((Decimal(a) ** 2) / (2 * Decimal(b)))
    return rough


def continued_frac(n):
    if n % 1 == 0.0:
        return [0]

    rep = [int(n)]
    for _ in range(16):
        n = 1 / (n - rep[-1])
        rep.append(int(n))
    rep.pop(0)

    n = 1
    original = rep[:]
    answer = rep[:n]
    while len(rep) > n:
        if answer == rep[n:n+n]:
            rep = rep[n:]
        elif answer[:len(rep[n:n+n])] == rep[n:n+n]:
            break
        else:
            rep = original[:]
            n += 1
            answer = rep[:n]

    return answer


def continued_frac2(n):
    sq = my_sqrt(n)
    if sq % 1 == 0.0:
        return 0
    m, d, a0 = 0, 1, int(sq)
    a = a0

    res = 0
    while a != 2 * a0:
        m = (d * a) - m
        d = (n - (m ** 2)) / d
        a = int((a0 + m) / d)
        res += a
    return res  # returns sum of results


def main():
    total = 50000
    getcontext().prec = 1000

    """
    *** failed first attempt ***
    
    number_list = []
    for i in range(1, total+1):
        frac = sum(continued_frac(my_sqrt(i)))
        number_list.append(frac)
        # print(i, frac)

    print(sum(number_list))
    # print('The sum of Q(N) for 1 ≤ N ≤ {} is {}.'.format(total, final))
    """

    """
    https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm
    """
    final = sum(continued_frac2(n) for n in range(1, total+1))
    print('The sum of Q(N) for 1 ≤ N ≤ {} is {}.'.format(total, final))


if __name__ == "__main__":
    main()
