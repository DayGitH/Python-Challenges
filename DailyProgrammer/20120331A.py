"""
A very basic challenge:
In this challenge, the
input is are : 3 numbers as arguments
output: the sum of the squares of the two larger numbers.
Your task is to write the indicated challenge.
"""

"""
NOTE: This script requires three input arguments!!!
"""
import sys

arguments = len(sys.argv)
if arguments != 4:
    print('Invalid number of arguments:\t{}'.format(arguments - 1))
    print('Required number of arguments:\t3')
else:
    l = sorted(list(map(int, sys.argv[1:])))
    print(sum(l[1:]))