"""
Happy (Be-Lated) Pi Day! To celebrate, write a program that calculates a list of rational approximations of Pi. Output
should look like:

3/1, 22/7, 333/106, 355/113, 52163/16604, 103993/33102, ...

Thanks to Cosmologicon for this programming suggestion in /r/dailyprogrammer_ideas!
"""

import math
import fractions

# Brute force method
for a in range(52000, 53000):
    diff = a
    b = 0
    while diff > 0:
        b_old = b if b > 0 else 1
        b += 1

        diff = (a / b) - math.pi

    # new = (math.pi - (a / b))
    # old = (math.pi - (a / b_old))
    # print(new, b, old, b_old)
    if abs(math.pi - (a / b)) < abs(math.pi - (a / b_old)):
        print("{} / {} : {}".format(a, b, a / b))
    else:
        print("{} / {} : {}".format(a, b_old, a / b_old))

# Newton's approximation
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

workingset = fractions.Fraction()
for k in range(100):
    num = 2 * (2 ** k) * (factorial(k) ** 2)
    denom = factorial((2 * k) + 1)
    workingset += fractions.Fraction(num, denom)
    print(workingset.numerator / workingset.denominator)