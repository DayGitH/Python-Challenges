"""
A polite number n is an integer that is the sum of two or more consecutive nonnegative integers in at least one way.
Here [http://en.wikipedia.org/wiki/Polite_number] is an article helping in understanding Polite numbers

Your challenge is to write a function to determine the ways if a number is polite or not.
"""

import math

def polite(n):
    print('Polite number sets for {}:'.format(n))
    a = 2
    while n / a > 1:
        div = n / a
        var = ((a - 1) / 2)

        if div-var <= 0:
            break

        if (div % 1 == 0.0 and var % 1 == 0.0) or (div % 1 == 0.5 and var % 1 == 0.5):
            print([i for i in range(int(div-var), int(div+var+1))])

        a += 1
    print('')


def main():
    polite(255)

if __name__ == "__main__":
    main()
