"""
Given a binary matrix like this:
0 1 1 1 1 0
1 0 0 1 1 1
1 0 1 1 1 1
1 1 1 1 1 1
0 1 1 1 1 0

Output the clues for a nonogram puzzle [http://en.wikipedia.org/wiki/Nonogram] in the format of "top clues, empty line,
bottom clues", with clues separated by spaces:
3
1 2
1 3
5
5
3

4
1 3
1 4
6
4

That is, count the contiguous groups of "1" bits and their sizes, first in columns, then in rows.

Thanks to nooodl for suggesting this problem at /r/dailyprogrammer_ideas! If you have a problem that you think would be
good for us, why not head over there and post it!
"""

import numpy as np
import itertools as it


def main():
    mat = np.array([[0, 1, 1, 1, 1, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 0]])

    for column in np.transpose(mat):
        """ method 1 """
        # count = 0
        # for e in column:
        #     if e:
        #         count += 1
        #     elif count:
        #         print(count, end=' ')
        #         count = 0
        # if count:
        #     print(count, end=' ')
        # print('')

        """ method 2 """
        for x, y in it.groupby(column, lambda x: x == 1):
            if x:
                print(sum(y), end=' ')
        print('')

    print('')

    for row in mat:
        """ method 1 """
        count = 0
        for e in row:
            if e:
                count += 1
            elif count:
                print(count, end=' ')
                count = 0
        if count:
            print(count, end=' ')
        print('')

        """ method 2 """
        # for x, y in it.groupby(row, lambda x: x == 1):
        #     if x:
        #         print(sum(y), end=' ')
        # print('')


if __name__ == "__main__":
    main()
