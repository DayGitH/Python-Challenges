"""
If you were to generate all permutations of the first three letters of the alphabet ("a", "b" and "c") and then sort
them, you would get the following list of 6 permutations:
abc
acb
bac
bca
cab
cba

As you can see, the fourth permutation in a sorted list of all the permutations of "a", "b" and "c" is "bca".

Similarly, if we wanted the 30th permutation in a sorted list of all permutations of the first five letters of the
alphabet (i.e. "abcde"), you get "baedc".

Define a function f(n,p) that generates the permutation number p in a sorted list of all permutations of the n first
letters of the alphabet. So, for instance:
f(3, 4) = "bca"
f(5, 30) = "baedc"
f(7, 1000) = "bdcfega"
f(8, 20000) = "dhfebagc"

Find f(11, 20000000)
Bonus:
Find f(20, 10^18 )
"""

import itertools

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def f(a, b):
    answer = []
    C = a
    index = b
    fact = factorial(C)
    print(index)
    total_pos = [i for i in range(C)]
    print(total_pos)
    for n in range(C, 1, -1):
        if fact != 2:
            fact = int(fact/n)
            div = int((index-1)/fact)
        else:
            div = int(index/fact)
        answer.append(str(total_pos[div]))
        total_pos.pop(div)
        index -= (div * fact)
    answer.append(str(total_pos[0]))

    conv = lambda x: alphabet[int(x)]
    return ''.join([conv(i) for i in answer])


def main():
    """ Solution based on previous solution of Euler Problem 24 """
    print(f(20, 10**18))

if __name__ == '__main__':
    main()
