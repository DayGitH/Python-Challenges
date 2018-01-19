"""
Write a program that, given an ASCII binary matrix of 0's and 1's like this:

0000000000000000
0000000000000000
0000011001110000
0000001111010000
0000011001110000
0000011011100000
0000000000110000
0000101000010000
0000000000000000
0000000000000000
0000000000000000

Outputs the smallest cropped sub-matrix that still contains all 1's (that is, remove all borders of 0's):

01100111
00111101
01100111
01101110
00000011
10100001
"""


def main():
    matrix = ("0000000000000000\n"
              "0000000000000000\n"
              "0000011001110000\n"
              "0000001111010000\n"
              "0000011001110000\n"
              "0000011011100000\n"
              "0000000000110000\n"
              "0000101000010000\n"
              "0000000000000000\n"
              "0000000000000000\n"
              "0000000000000000")

    matrix = matrix.split('\n')
    top = -1
    bottom = 0
    right = 0
    left = len(matrix[0])

    for n, m in enumerate(matrix):
        if '1' in m:
            if top == -1:
                top = n
            bottom = n

            left_find = m.find('1')
            right_find = m.rfind('1')
            if left_find < left:
                left = left_find
            if right_find > right:
                right = right_find

    for m in matrix[top:bottom+1]:
        print(m[left:right+1])


if __name__ == "__main__":
    main()
