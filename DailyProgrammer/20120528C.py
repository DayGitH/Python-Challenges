"""
A type of pseudo-random number generator is the so-called lagged fibonacci generator
[http://en.wikipedia.org/wiki/Lagged_fibonacci_generator], which has become somewhat popular because it is very simple
to implement, can have an extremely long period, and produces high quality random numbers.

The idea is this: to calculate s(n) (i.e. the nth random number), you evaluate:
s(n) = (s(n - a) + s(n - b)) mod M

For some positive constants a and b (it is thus similar to the fibonacci numbers, but it "lags" behind) and some
modulus M. One popular choice for a and b is a = 24 and b = 55. Lets use those numbers and a modulus of 1073741824
(i.e. 230 ), and the generator becomes:
s(n) = (s(n - 24) + s(n - 55)) mod 1073741824

In order for this formula to work, you need to initialize the values s(0),s(1),...,s(54), so that the recursion has
somewhere to bottom out. Often, another random number generator is used to supply the inital values. Lets use the
random number generator from the intermediate challenge #53
[http://www.reddit.com/r/dailyprogrammer/comments/tpxqc/5162012_challenge_53_intermediate/].

That is to say, for values s(0) through s(54), s is defined as follows:
s(0) = 123456789
s(n) = (22695477 * s(n-1) + 12345) mod 1073741824

But for values s(55) and above, s is defined as follows:
s(n) = (s(n - 24) + s(n - 55)) mod 1073741824

Here are a few example values:
s(10)     = 1048156299
s(20)     = 472459921
s(55)     = 827614689
s(56)     = 530449927
s(100)    = 515277845
s(1000)   = 985063932
s(10000)  = 304605728
s(100000) = 434136346

Find s( 10 ** 18 )
"""

import numpy as np

A = 7
B = 10
M = 2 ** 30
d = {}


def s_init(n, sp):
    """ from 20120516B """
    if n == 0:
        return 123456789
    else:
        return (22695477 * sp + 12345) % M


def s(n, list):
    if n < B:
        return list[n]
    return (s(n-A, list) + s(n-B, list)) % M


def d_s(n):
    if n < B:
        return d[n]
    if n-A in d:
        s_a = d[n-A]
    else:
        s_a = d_s(n-A)
        d[n-A] = s_a
    if n-B in d:
        s_b = d[n-B]
    else:
        s_b = d_s(n-B)
        d[n-B] = s_b
    return (s_a + s_b) % M


def gen_A():
    big = max(A, B)
    res = np.concatenate(([np.zeros(big)], np.identity(big)[:-1]), axis=0)
    res[0][A-1] = 1
    res[0][B-1] = 1
    return res


def gen_X():
    big = max(A, B)
    res = np.zeros(big, dtype='object')
    res[0] = s_init(0, -1)
    for i in range(1, big):
        res[i] = s_init(i, res[i-1])
    return res[::-1]


def lfg_main(n):
    big = max(A, B)
    A_mat = gen_A()
    X_mat = gen_X()

    if n < big:
        print(X_mat[big-n-1])
    else:
        m = n-big+1
        A_mat = np.linalg.matrix_power(A_mat, m)
        print(m)
        for a in A_mat:
            for b in a:
                print(b, type(b))
        X_out = np.remainder(np.dot(A_mat, X_mat), M)
        print(int(X_out[0]))


def d_main(n):
    d[0] = s_init(0, -1)
    for i in range(1, B):
        d[i] = s_init(i, d[i-1])

    print(d_s(n))


def main(n):
    l = [s_init(0, -1)]
    for i in range(1, B):
        l.append(s_init(i, l[-1]))

    print(s(n, l))

if __name__ == "__main__":
    n = 1000
    # main()
    # d_main(n)
    lfg_main(n)