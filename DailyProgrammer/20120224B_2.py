"""
A 30x30 grid of squares contains 900 fleas, initially one flea per square. When a bell is rung, each flea jumps to an
adjacent square at random (usually 4 possibilities, except for fleas on the edge of the grid or at the corners).

What is the expected number of unoccupied squares after 50 rings of the bell? Give your answer rounded to six decimal
places.

source: project euler
"""

import numpy
import cProfile

LOC_SIZE = 30
RUNS = 100000


def ring(locs):
    # working set
    ret_locs = [[0 for x in range(LOC_SIZE)] for y in range(LOC_SIZE)]
    # looping over x and y coords
    for y in range(LOC_SIZE):
        for x in range(LOC_SIZE):
            # ringing at a corner
            if x == 0 and y == 0:
                ret_locs[x + 1][y] += locs[x][y] * (1 / 2)
                ret_locs[x][y + 1] += locs[x][y] * (1 / 2)
            elif x == 0 and y == LOC_SIZE - 1:
                ret_locs[x + 1][y] += locs[x][y] * (1 / 2)
                ret_locs[x][y - 1] += locs[x][y] * (1 / 2)
            elif x == LOC_SIZE - 1 and y == 0:
                ret_locs[x - 1][y] += locs[x][y] * (1 / 2)
                ret_locs[x][y + 1] += locs[x][y] * (1 / 2)
            elif x == LOC_SIZE - 1 and y == LOC_SIZE - 1:
                ret_locs[x - 1][y] += locs[x][y] * (1 / 2)
                ret_locs[x][y - 1] += locs[x][y] * (1 / 2)
            # ringing at a non-corner edge
            elif x == 0:
                ret_locs[x + 1][y] += locs[x][y] * (1 / 3)
                ret_locs[x][y + 1] += locs[x][y] * (1 / 3)
                ret_locs[x][y - 1] += locs[x][y] * (1 / 3)
            elif x == LOC_SIZE - 1:
                ret_locs[x - 1][y] += locs[x][y] * (1 / 3)
                ret_locs[x][y + 1] += locs[x][y] * (1 / 3)
                ret_locs[x][y - 1] += locs[x][y] * (1 / 3)
            elif y == 0:
                ret_locs[x + 1][y] += locs[x][y] * (1 / 3)
                ret_locs[x - 1][y] += locs[x][y] * (1 / 3)
                ret_locs[x][y + 1] += locs[x][y] * (1 / 3)
            elif y == LOC_SIZE - 1:
                ret_locs[x + 1][y] += locs[x][y] * (1 / 3)
                ret_locs[x - 1][y] += locs[x][y] * (1 / 3)
                ret_locs[x][y - 1] += locs[x][y] * (1 / 3)
            # ringing at a non-edge location
            else:
                ret_locs[x + 1][y] += locs[x][y] * (1 / 4)
                ret_locs[x - 1][y] += locs[x][y] * (1 / 4)
                ret_locs[x][y + 1] += locs[x][y] * (1 / 4)
                ret_locs[x][y - 1] += locs[x][y] * (1 / 4)

    return ret_locs


def operate_on_narray(x, y, function):
    """from stackoverflow - used to do element-wise operations on 2d arrays.
       TODO: learn how this works
    """
    try:
        return [operate_on_narray(a, b, function) for a, b in zip(x, y)]
    # except TypeError as e:
    except TypeError:
        # Not iterable
        return function(x, y)


def init_block():
    """Creates the set of probabilities for the first quadrant. The other three quadrants are copies of this."""
    final_locs = [[1 for x in range(LOC_SIZE)] for y in range(LOC_SIZE)]
    for a in range(int(LOC_SIZE / 2)):
        for b in range(a, int(LOC_SIZE / 2)):
            # creating and ringing each of the fleas individually
            print(a, b)
            locs = [[1 if x == a and y == b else 0 for x in range(LOC_SIZE)] for y in range(LOC_SIZE)]
            for i in range(50):
                locs = ring(locs)
            # finding complement of all probabilities to find probabilities of not having a flea there
            for r in range(LOC_SIZE):
                for s in range(LOC_SIZE):
                    locs[r][s] = 1 - locs[r][s]
            # transposes and adds the set of probabilities to not have to recalculate for mirrored values
            if a != b:
                locs = operate_on_narray(locs, zip(*locs), lambda o, p: o*p)
            # multiplying the probabilities together
            final_locs = operate_on_narray(final_locs, locs, lambda o, p: o*p)
    return final_locs


def rem_blocks(starting_quad):
    """ mirroring the first calculated quadrant to the other three """
    remaining_quads = 3
    complete = starting_quad
    working_set = starting_quad

    for i in range(remaining_quads):
        # zip(*original)[::=1] rotates 2d array anticlockwise 90 degrees
        working_set = list(zip(*working_set))[::-1]
        complete = operate_on_narray(complete, working_set, lambda a, b: a*b)
    return complete


def main():
    first_quad = init_block()
    completed = rem_blocks(first_quad)

    # for i in completed:
    #     print(i)

    print(numpy.sum(completed))

if __name__ == '__main__':
    cProfile.run('main()')
    # main()
