"""
Before I get to today's problem, I'd just like to give a warm welcome to our two new moderators, nooodl and Steve132! We
decided to appoint two new moderators instead of just one, because rya11111 has decided to a bit of a break for a while.

I'd like to thank everyone who applied to be moderators, there were lots of excellent submissions, we will keep you in
mind for the next time. Both nooodl and Steve132 have contributed some excellent problems and solutions, and I have no
doubt that they will be excellent moderators.

Now, to today's problem! Good luck!

In 1987, mathematician John Conway invented one of the most curious programming languages ever, which he dubbed FRACTRAN

.

A FRACTRAN program is simply a series of fractions, nothing more, nothing less. As input, the program takes a single
integer. The program runs like this:

    The integer is checked against each fraction in order. If the result of multiplying that integer with the fraction
    is another integer, you start over with the product generated by multiplying with that fraction.

    If none of the fractions multiplied by the input integer results in another integer, the program finishes and
    returns the integer as the result.

Conway was able to show that despite the simplicity of this "programming language", it is in fact Turing-complete,
meaning that any computation you can do in any other language, you can do in FRACTRAN.

The wikipedia article for FRACTRAN [http://en.wikipedia.org/wiki/Fractran] explains very well how this works and how to
write a program in FRACTRAN.

Your task is to first of all write a FRACTRAN interpreter that is able to run FRACTRAN programs (and remember that the
numbers can very easily get very large, so 64-bit integers is not going to be enough, you need big numbers) and then to
write a program in FRACTRAN. Here are a few suggestions of programs you could write, roughly ordered from least
difficult to most difficult:

    Implement the min(a,b) function. So for input 2**a * 3**b the code returns 5**(min(a,b)) where min(a,b) is the
    smallest number of a and b. Example: input 5832 should output 125 ( 2**3 * 3**6 -> 5**3 )

    Implement the max(a,b) function. So for input 2**a * 3**b the code returns 5**(max(a,b)) where max(a,b) is the
    largest number of a and b. Example: input 5832 should output 15625 ( 2**3 * 3**6 -> 5**6 )

    Write a program that takes an input a that is divisible by 3 and divides it by 3. So for input 2**a it returns
    3**(a/3) . Example: input 2097152 should output 2187 ( 2**21 -> 3**7 ). Note: this can be done in a single fraction.

    Write a program that for an input n, returns the sum of all integers less than n. So if the input is 2**5, it should
    output 3**(1+2+3+4) = 3**10. Example: input 32 should output 59049 ( 2**5 -> 3**10 )

    Write a program that generates the nth fibonacci number. So for input 2**n it should output 3**f(n) where f(n) is
    the nth fibonacci number. Example: input 128 should output 1594323 ( 2**7 -> 3**13 ).
"""


def resolve_fraction(f):
    return f[0]/f[1]


def fractran(fractions, n):
    res = []
    for i in range(100):
        for f in fractions:
            if ((n/f[1]) * f[0]) % 1 < 10**-2:
                res.append(n)
                n = round((n/f[1]) * f[0])
                break
        else:
            res.append(n)
            break
    return res


def min_fractran(n):
    f_list = [[ 5,  6], [ 1,  3], [ 1,  2]]
    return fractran(f_list, n)[-1]


def max_fractran(n):
    f_list = [[ 5,  6], [ 5,  3], [ 5,  2]]
    return fractran(f_list, n)[-1]


def div_three_fractran(n):
    f_list = [[ 3,  8]]
    return fractran(f_list, n)[-1]


def almost_factorial_fractran(n):
    f_list = [[231, 10], [ 5, 11], [ 1,  5], [ 2,  7], [ 5,  2]]
    return fractran(f_list, n)


def main():
    f_list = [[17, 91], [78, 85], [19, 51], [23, 38], [29, 33], [77, 29], [95, 23],
              [77, 19], [ 1, 17], [11, 13], [13, 11], [15, 14], [15,  2], [55,  1]]

    # print(fractran(f_list, 4))
    # print(min_fractran(2**3 * 3**6))
    # print(max_fractran(2**3 * 3**6))
    # print(div_three_fractran(2097152))
    print(almost_factorial_fractran(2**5))


if __name__ == "__main__":
    main()
