"""
A tetrahedral number[https://en.wikipedia.org/wiki/Tetrahedral_number] is is a figurate number that represents a
pyramid with a triangular base and three sides.
Write a program to find the base of the tetrahedron that contains an input number of balls.
example: 169179692512835000 balls
taken from programmingpraxis.com
"""

import sympy
# import math

solve = sympy.solvers.solve
x = sympy.Symbol('x')


def get_tetrahydral_level(num):
    return int(solve((x**3 + (3 * x**2) + (2 * x))/6 - num, x)[0])


def calc_triangular_number(num):
    return int(num * (num + 1) / 2)


if __name__ == '__main__':
    while True:
        inp = int(input('Enter number: '))
        try:
            n = get_tetrahydral_level(inp)
            tri = calc_triangular_number(n)
            print(tri)
        except TypeError:
            print('Non-valid tetrahydral number')


# Super slow method
# def nCr(n,r):
#     f = math.factorial
#     return f(n) / (f(r) * f(n-r))
#
# if __name__ == '__main__':
#     n = 1
#     inp = int(input('Enter number: '))
#     tri = nCr(n+1,2)
#     while tri != inp and inp > 0:
#         print(inp)
#         inp -= tri
#         n += 1
#         tri = nCr(n+1,2)
#
#     if inp >= 0:
#         print('Base: {}'.format(inp))
#     else:
#         print('Non tetrahedral number')
