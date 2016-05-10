"""Write a program to do the following:
input: a base ten (non-fractional) number at the command line
output: the binary representation of that number.
"""

# The inbuilt binary convertor
# print("{0:b}".format(int(input('Enter number: '))))


def binary(n):
    """Returns n in binary form.

    First while loop finds the largest '1' bit, and the second while loop incrementally fills the lower value bits.
    """
    if n == 0:
        return 0
    ans = '1'
    a = 0
    while n - (2 ** a) >= 0:
        a += 1

    a -= 2
    n -= (2 ** (a+1))

    while a >= 0:
        if n - (2 ** a) < 0:
            ans += '0'
            a -= 1
        else:
            ans += '1'
            n -= (2 ** a)
            a -= 1

    return ans

while True:
    print(binary(int(input('Enter number: '))))
