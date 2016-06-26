"""
For this challenge, make a program that finds the determinant of a square matrix
[http://en.wikipedia.org/wiki/Determinant#Calculation]. You do not need to use any exceedingly complex methods, using
expansion by cofactors is entirely sufficient (if you have no idea what that is, the always helpful Khan Academy here
[http://www.khanacademy.org/math/linear-algebra/v/linear-algebra--3x3-determinant] to help
[http://www.khanacademy.org/math/linear-algebra/v/linear-algebra--nxn-determinant]. Wikipedia also
[http://en.wikipedia.org/wiki/Laplace_expansion] has you covered
[http://en.wikipedia.org/wiki/Cofactor_(linear_algebra)]).

What is the determinant of the following matrix?
 -5   0   1  -3   0  -4   2  -2   0   2
 -5  -1  -4   4  -2  -5   0  -4   3  -3
 -4   5   3   3   0   0  -2  -2   2   2
 -4  -1   5  -3  -3  -5  -2  -5   3  -1
  4   5   2  -5   2  -4   1  -1   0  -3
 -2  -4  -3  -1   4  -5  -4   2   1   4
  5   5   2  -5   1  -3  -2  -1  -5   5
  1   4  -2   4   3   2   1   0   3  -2
  3   0  -4  -3   0   1  -3   0   1   2
 -1  -4  -3  -1  -4   1   2  -5   2  -1

Note: the whole purpose of this challenge is to write the code for calculating the determinant yourself. Therefore, you
are not allowed to use library functions that are designed to calculate things like this. The matrix should be
represented by the native array construct of your language, not any special data type designed to operate on
mathematical matrices. That means no NumPy, no using fancy functions in Mathematica or Matlab! You are allowed to use
these to test whether or not your function works, but that's it.
"""

import numpy as np


def determinant(array):
    if array.size == 4:
        return (array[0][0] * array[1][1]) - (array[0][1] * array[1][0])
    else:
        sum = 0
        for n, i in enumerate(array[0]):
            minor = (np.delete(np.delete(array, n, 1), 0, 0))
            sum += i * ((-1) ** (1+n+1)) * determinant(minor)
        return sum


def main():
    arr = np.array([[-5,   0,   1,  -3,   0,  -4,   2,  -2,   0,   2],
                    [-5,  -1,  -4,   4,  -2,  -5,   0,  -4,   3,  -3],
                    [-4,   5,   3,   3,   0,   0,  -2,  -2,   2,   2],
                    [-4,  -1,   5,  -3,  -3,  -5,  -2,  -5,   3,  -1],
                    [ 4,   5,   2,  -5,   2,  -4,   1,  -1,   0,  -3],
                    [-2,  -4,  -3,  -1,   4,  -5,  -4,   2,   1,   4],
                    [ 5,   5,   2,  -5,   1,  -3,  -2,  -1,  -5,   5],
                    [ 1,   4,  -2,   4,   3,   2,   1,   0,   3,  -2],
                    [ 3,   0,  -4,  -3,   0,   1,  -3,   0,   1,   2],
                    [-1,  -4,  -3,  -1,  -4,   1,   2,  -5,   2,  -1]])
    # arr = np.array([[1, 2, 3],
    #                 [3, 2, 1],
    #                 [2, 1, 3]])

    print(arr)
    # print(np.linalg.det(arr))
    print(determinant(arr))

if __name__ == "__main__":
    main()
