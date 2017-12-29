"""
Implement the hyperoperator [http://en.wikipedia.org/wiki/Hyperoperation#Definition] as a function hyper(n, a, b), for
non-negative integers n, a, b.

hyper(1, a, b) = a + b, hyper(2, a, b) = a * b, hyper(3, a, b) = a ^ b, etc.

Bonus points for efficient implementations.

    thanks to noodl for the challenge at /r/dailyprogrammer_ideas ! .. If you think yo have a challenge worthy for our
    sub, do not hesitate to submit it there!

Request: Please take your time in browsing /r/dailyprogrammer_ideas and helping in the correcting and giving suggestions
to the problems given by other users. It will really help us in giving quality challenges!

Thank you!
"""


def hyper(n, a, b, cache):
    # expect n >= 0
    args = list(map(str, [n, a, b]))

    if ','.join(args) in cache:
        return cache[','.join(args)]

    if not n:
        answer = b + 1
    elif n == 1:
        answer = a + b
    elif n == 2:
        answer = a * b
    elif n == 3:
        answer = a ** b
    elif not b:
        answer = 1
    else:
        answer = hyper(n-1, a, hyper(n, a, b-1, cache), cache)

    cache[','.join(args)] = answer
    return answer


def main():
    print(hyper(5, 3, 2, {}))


if __name__ == "__main__":
    main()
