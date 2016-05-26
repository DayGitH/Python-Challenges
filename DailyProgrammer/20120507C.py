"""
When you roll two regular six-sided dice, the total number of pips that can come up ranges from 2 (if both dice show 1)
to 12 (if both dice show 6), but as all experienced gamblers know, some numbers are more likely than others. In fact,
the most likely number to come up is 7, with a probability of 1/6. By contrast, the probability of 12 showing is only
1/36, so it is six times more likely that the dice will show 7 than it is that they will show 12.

The reason for this is of course that there are more ways that two dice can sum to 7. In fact, there are exactly six
ways two dice can sum to 7: the first die can show 1 and the second 6, the first 2 and the second 5, the first 3 and
the second 4, the first 4 and the second 3, the first 5 and the second 2, and finally the first die can show 6 and the
second 1. Given that there are a total of 6*6 = 36 different ways the dice can land, this gives us the probability:
6/36 = 1/6. In contrast, there is only one way two dice can form 12, by throwing two sixes.

Define a function f(d, n) that gives the number of ways d six-sided dice can be thrown to show the number n. So, in the
previous example, f(2,7) = 6. Here are a few other values of that function:
f(1,n) = 1 (for 1≤n≤6, 0 otherwise)
f(2,7) = 6
f(2,10) = 3
f(2,12) = 1
f(3,10) = 27
f(5,20) = 651
f(7,30) = 12117
f(10,50) = 85228
Find f(20, 100)

Note: the answer fits into a 64-bit integer

Bonus: Find f(1100, 5000) mod 107
"""

import itertools
from scipy import convolve


def f(d, n):
    """
    my itertools solution. too slow for final solution
    """
    dice = '123456'
    comb = itertools.product(dice, repeat=d)
    perm_list = []

    def sum_check(x, n):
        return sum(x) == n

    for c in comb:
        intd = list(map(int, c))
        if sum_check(intd, n):
            perm_list.append(intd)
    return len(perm_list)


def crawphish(d, n):
    """
    Recursive solution from /u/crawphish ported to python by me. too slow for final solution
    """
    out = 0
    for i in range(1, 6+1):
        if d:
            out += crawphish(d - 1, n - i)
        else:
            if n:
                return 0
            else:
                return 1
    return out


def ttl(d, n, m=10**7):
    """
    /u/ttl's solution. Mathematical solution, no idea of how it works but it returns the solution and bonus solution
    very quickly.
    """
    p = q = [1]*6+[0]
    i = 1
    while i < d:
        q, i = (convolve(q, q) % m, i*2) if 2*i < d else (convolve(q, p) % m, i+1)
    return q[-n-1]


def main():
    # print(f(20,100))
    # print(crawphish(20, 100))
    print(ttl(1100, 5000))

if __name__ == "__main__":
    main()
