"""
Given a 3x3 table where 1 represents on and 0 represents off:
 ABC
A010
B111
C011

Where "inverted match" is defined as a case where the values at the coordinates in the format of (X, Y) and (Y, X) are
the same, the inverted matches are as follows:
[[(A, B), (B, A)], [(A, C), (C, A)], [(B, C), (C, B)]]
Of these, the matches that have a value of 1 are:
[[(A, B), (B, A)], [(B, C), (C, B)]]
Therefore, there are 2 sets of inverted matches that have a value of 1.

Find the amount of inverted matches in the table in table(below) with a value of 1.
Table:
 ABCDEFGHIJKLMNOPQRST
A11110101111011100010
B10010010000010001100
C01101110010001000000
D10110011001011101100
E10100100011110110100
F01111011000111010010
G00011110001011001110
H01111000010001001000
I01101110010110010011
J00101000100010011110
K10101001100001100000
L01011010011101100110
M10110110010101000100
N10001111101111110010
O11011010010111100110
P01000110111101101000
Q10011001100010100000
R11101011100110110110
S00001100000110010101
T01000110011100101011
Thanks to gbchaosmaster for the challenge at /r/dailyprogrammer_ideas :)

UPDATE: I have given some more info on the difficult challenge since it seems to be very tough. you have upto monday to
finish all these challenges. pls note it :)
"""

import numpy as np


def main():
    # array = np.array([[0, 1, 0],
    #                   [1, 1, 1],
    #                   [0, 1, 1]])
    array = np.array([[1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0],
                      [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
                      [0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                      [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0],
                      [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0],
                      [0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
                      [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0],
                      [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                      [0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1],
                      [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
                      [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                      [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0],
                      [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
                      [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
                      [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0],
                      [0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                      [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                      [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
                      [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
                      [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1]])
    side = len(array)
    trans = np.transpose(array)

    """ transpose and zip method """
    zeros = np.zeros((side, side), dtype=bool)
    n = 0
    for x, y in zip(array, trans):
        for a in range(n,side):
            if x[a] == y[a] and x[a]:
                zeros[n][a] = True
        n += 1

    n = 0
    count = 0
    for a in zeros:
        for b in range(n+1, side):
            # print(a, b)
            if zeros[n][b]:
                count += 1
                print('[{}, {}]'.format(chr(n + 65), chr(b + 65)), end='')
                print(' : ', end='')
                print('[{}, {}]'.format(chr(b + 65), chr(n + 65)))
                print(count)
        n += 1

    """ transpose and multiply method """
    out = np.multiply(array, trans)
    count = 0
    n = 0
    for o in out:
        for s in range(n+1, side):
            if out[n][s]:
                count += 1
        n += 1
    print(count)


if __name__ == "__main__":
    main()
