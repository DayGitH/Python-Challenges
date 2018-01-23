"""
The factorial of 10 is 3628800. The last non-zero digit of that factorial is 8.

Similarly, the last non-zero digit of the factorial of 10**3 is 2.

Compute the last non-zero digit of the factorial of 10**9.

Bonus: Compute the last non-zero digit of the factorial of 10**100.

    Thanks to ashashwat for suggesting this problem at /r/dailyprogrammer_ideas! If you have a problem that you think
    would be good for us, why not head over there and suggest it?

"""


def factorial_prod_lookup(n, results={}):
    if n in results:
        return results[n]
    res = 1
    for i in range(1, n + 1):
        res *= i
    return int(res)


def get_digit(n, i):
    """ i=0 for units, i=1 for tens, t=2 for hundreds... """
    return int(str(n)[::-1][i])


def last_non_zero_of_factorial(n):
    if n == 0:
        return 1
    elif n < 10:
        return last_non_zero(factorial_prod_lookup(n))

    tens = get_digit(n, 1)
    if tens % 2 == 0:
        return last_non_zero(6 * last_non_zero_of_factorial(n // 5) * last_non_zero_of_factorial(get_digit(n, 0)))
    else:
        return last_non_zero(4 * last_non_zero_of_factorial(n // 5) * last_non_zero_of_factorial(get_digit(n, 0)))


def last_non_zero(n):
    return int(str(n).strip('0')[-1])


def main():
    print(last_non_zero_of_factorial(10**100))


if __name__ == "__main__":
    main()
