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

Find s( 1018 )
"""

A = 24
B = 55
M = 2 ** 30

def s_init(n, sp):
    """ from 20120516B """
    if n == 0:
        return 123456789
    else:
        return (22695477 * sp + 12345) % 1073741824


def s(n, list):
    if n < B:
        return list[n]
    return (s(n-A, list) + s(n-B, list)) % M


def main():
    l = [s_init(0, -1)]
    for i in range(1,B):
        l.append(s_init(i, l[-1]))

    print(s(10000, l))

if __name__ == "__main__":
    main()
