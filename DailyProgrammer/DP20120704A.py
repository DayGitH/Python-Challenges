"""
The one-dimensional simple cellular automata Rule 110 [http://en.wikipedia.org/wiki/Rule_110] is the only such cellular
automata currently known to be turing-complete, and many people say it is the simplest known turing-complete system.

Implement a program capable of outputting an ascii-art representation of applying Rule 110 to some initial state. How
many iterations and what your initial state is is up to you!

You may chose to implement rule 124 instead if you like (which is the same thing, albeit backwards).

Bonus points if your program can take an arbitrary rule integer from 0-255 as input and run that rule instead!
"""

import random
from PIL import Image, ImageFont, ImageDraw


def create_pattern_dict(rule):
    patterns = ['111', '110', '101', '100',
                '011', '010', '001', '000']
    rule = bin(rule)[2:].zfill(8)
    return {a: b for a, b in zip(patterns, rule)}


def writer(res):
    return ''.join(res).replace('0', ' ').replace('1', 'O')


def run_rule(init, rule):
    patterns = create_pattern_dict(rule)
    print(patterns)

    size = len(init)
    res = init[:]
    im = Image.new('RGB', (size, size+1), (255, 255, 255))
    for n, i in enumerate(init):
        if i == '1':
            im.putpixel((n, 0), (0, 0, 0))
    for _ in range(size):
        res[0] = patterns[''.join([init[-1]] + init[:2])]
        for r in range(1, size-1):
            res[r] = patterns[''.join(init[r-1:r+2])]
        res[-1] = patterns[''.join(init[-2:] + [init[0]])]
        init = res[:]
        for n, i in enumerate(res):
            if i == '1':
                im.putpixel((n, _), (0, 0, 0))
    im.show()


def main():
    s = 512
    init = list(bin(random.randint(0, 2**s-1))[2:].zfill(s))

    # run_rule(init, 110)
    run_rule(init, 105)


if __name__ == "__main__":
    main()
