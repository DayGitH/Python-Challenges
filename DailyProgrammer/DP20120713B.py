"""
Write a function graph(f, low, high, tests) that outputs a probability graph of the function f from range low to high
(inclusive) over tests tests (i.e., counting the frequencies of f() outputs). f takes no arguments and returns an
integer, low, high and tests are all integer values. For example, a function f that simulates two-dice rolls:

def two_dice():
    return random.randint(1, 6) + random.randint(1, 6)

Then graph(f, 2, 12, 10000) should output something roughly like:

  2: ##
  3: #####
  4: #######
  5: ###########
  6: #############
  7: #################
  8: #############
  9: ###########
 10: ########
 11: #####
 12: ##

For bonus points, output the graph with the numbers on the bottom and the bars drawn vertically.
"""

import random


def two_dice():
    return random.randint(1, 6) + random.randint(1, 6)


def three_dice():
    return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)


def graph(f, low, high, tests):
    res = {i: 0 for i in range(low, high+1)}
    for _ in range(tests):
        try:
            res[f()] += 1
        except KeyError:
            pass
    print(res)

    horizontal_print(res)
    vertical_print(res)


def horizontal_print(res):
    rounder = min([res[k] for k in res]) // 2
    max_size = len(str(max(res)))

    for k in res:
        res[k] = int(round(res[k] / rounder))
        print('{:>{max_size}}: {}'.format(k, '#' * res[k], max_size=max_size))


def vertical_print(res):
    rounder = min([res[k] for k in res]) // 2
    max_size = len(str(max(res)))

    max_height = max([res[k] for k in res])
    for k in res:
        res[k] = int(round(res[k] / rounder))
        res[k] = '{:>{max_height}}'.format('#' * res[k], max_height=max_height)

    for i in range(max_height):
        for k in res:
            print('{:>{max_size}}'.format(res[k][i], max_size=max_size+1), end='')
        print('')

    print('=' * (max_size+1) * len(res))
    for k in res:
        print('{:>{max_size}}'.format(k, max_size=max_size+1), end='')


def main():
    graph(two_dice, 2, 12, 100000)
    graph(three_dice, 3, 18, 100000)


if __name__ == "__main__":
    main()
