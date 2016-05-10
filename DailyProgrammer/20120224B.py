"""
A 30x30 grid of squares contains 900 fleas, initially one flea per square. When a bell is rung, each flea jumps to an
adjacent square at random (usually 4 possibilities, except for fleas on the edge of the grid or at the corners).

What is the expected number of unoccupied squares after 50 rings of the bell? Give your answer rounded to six decimal
places.

source: project euler
"""


import random
import cProfile
import re

LOC_SIZE = 30
RUNS = 100000


class Flea:
    # top left is origin.
    # x is horizontal to the left
    # y is vertical to below
    loc = []

    def __init__(self, x_loc, y_loc):
        self.loc = [x_loc, y_loc]

    def ring(self):
        choose = ['N', 'E', 'W', 'S']
        if self.loc[0] == 0:
            choose.remove('W')
        if self.loc[0] == LOC_SIZE - 1:
            choose.remove('E')
        if self.loc[1] == 0:
            choose.remove('N')
        if self.loc[1] == LOC_SIZE - 1:
            choose.remove('S')

        final_choice = random.choice(choose)
        if final_choice == 'N':
            self.loc[1] -= 1
        elif final_choice == 'S':
            self.loc[1] += 1
        elif final_choice == 'E':
            self.loc[0] += 1
        elif final_choice == 'W':
            self.loc[0] -= 1
        # while True:
        #     final_choice =
        # if not (0 <= self.loc[0] < LOC_SIZE) or not (0 <= self.loc[1] < LOC_SIZE):
        #     raise Exception('out of bounds')


def main():
    add = 0
    for r in range(RUNS):
        flea_list = {x: Flea(x // LOC_SIZE, x % LOC_SIZE) for x in range(LOC_SIZE ** 2)}

        # for i in range(50):
        #     for j in range(LOC_SIZE ** 2):
        #         flea_list[j].ring()

        [[flea_list[j].ring() for j in range(LOC_SIZE ** 2)] for i in range(50)]

        locs = [[0 for x in range(LOC_SIZE)] for y in range(LOC_SIZE)]
        for j in range(LOC_SIZE ** 2):
            l = flea_list[j].loc
            locs[l[0]][l[1]] += 1

        for i in locs:
            add += i.count(0)

        print(r)

    print('Average =', add / RUNS)

if __name__ == '__main__':
    cProfile.run('main()')
    # main()
