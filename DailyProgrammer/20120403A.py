"""
Write a program that will take a number and print a right triangle attempting to use all numbers from 1 to that number.
Sample Run:
Enter number: 10
Output:
7 8 9 10
4 5 6
2 3
1
Enter number: 6
Output:
4 5 6
2 3
1
Enter number: 3
Output:
2 3
1
Enter number: 12
Output:
7 8 9 10
4 5 6
2 3
1
"""

import math


def is_square(apositiveint):
    """
    Checks if number is a square

    Taken verbatim from https://stackoverflow.com/questions/2489435/how-could-i-check-if-a-number-is-a-perfect-square
    """
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True


def home_in_right_triangle(n):
    """
    Homes in on right triangle number, if given number is not right triangle
    """
    while not is_square((8*n)+1):
        if (((8*n)+1) % 1) < 0.5:
            n -= 1
        else:
            n += 1

    return n


def right_triangle_root(n):
    """
    Returns root of right triangle number

    Formula taken from wikipedia
    """
    return int((math.sqrt((8*n)+1)-1)/2)


def right_triangle_calc(n):
    """
    Returns right triangle of level n

    Formula derived from right triangle definition (n+1)choose2
    """
    return int((n*(n+1))/2)


def print_right_triangle(n):
    """
    Prints right triangle based on specs

    Also contains formatting so that shorter numbers are spaced out to match longer numbers
    """
    l = len(str(right_triangle_calc(n)))
    for i in reversed(range(1, n+1)):
        a = right_triangle_calc(i-1)+1
        for j in range(a, right_triangle_calc(i)+1):
            l0 = len(str(j))
            if l0 < l:
                print(' ' * (l-l0), end='')
            print(j, end=' ')
        print('\n')

if __name__ == '__main__':
    number = home_in_right_triangle(200)
    level = right_triangle_root(number)
    print_right_triangle(level)

