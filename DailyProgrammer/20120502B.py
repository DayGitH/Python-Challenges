"""
Given a string containing the English word for one of the single-digit numbers, return the number without using any of
the words in your code. Examples:
eng_to_dec('zero') # => 0
eng_to_dec('four') # => 4

Note: there is no right or wrong way to complete this challenge. Be creative with your solutions!

Thanks to HazierPhonics for posting this idea on /r/dailyprogrammer_ideas! If you have a problem that you think would
be good for us, head over there and contribute!
"""

import numpy as np


def eng_to_dec(string):
    """ method 1"""
    d = {3: {'e': 1, 'o': 2, 'x': 6},
         4: {'r': 0, 'u': 4, 'v': 5, 'n': 9},
         5: {'r': 3, 'v': 7, 'g': 8}}
    return d[len(string)][string[2]]

    """ method 2 """
    import unicodedata
    return unicodedata.lookup('digit {}'.format(string))


def main():
    L = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for l in L:
        print('{} :: {}'.format(eng_to_dec(l), l))


if __name__ == '__main__':
    main()
