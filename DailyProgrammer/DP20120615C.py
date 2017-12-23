"""
A magic square is a square of size NxN with the numbers 1 through n2 put in so that all rows, all columns and both
diagonals sum to the same number. For instance, this is a 3x3 magic square:

8 1 6
3 5 7
4 9 2

As you can see all rows, all columns and both diagonals (8+5+2 and 4+5+6) sum to the same number, 15.

Write a program that draws a magic square of size 18x18.

    Thanks to /u/SwimmingPastaDevil for submitting this problem in /r/dailyprogrammer_ideas! And on behalf of the
    moderators, I'd like to thank everyone who submitted problems the last couple of days, it's been really helpful,
    and there are some great problems there! Keep it up, it really helps us out a lot!


"""

import numpy as np


def magic_square_4(n):
    arr = np.arange(1, n*n + 1)
    arr.resize(n, n)
    n //= 4
    mask = np.array([[0, 1, 1, 0],
                     [1, 0, 0, 1],
                     [1, 0, 0, 1],
                     [0, 1, 1, 0]])
    mask = np.tile(mask, (n, n))
    antimask = 1 - mask

    return (mask * arr) + np.rot90((antimask * arr), 2)


def siamese_square(n, start=1):
    arr = np.zeros((n, n), dtype=int)
    x, y = 0, n // 2
    arr[x, y] = start
    for i in range(1+start, (n**2) + start):
        x, y = (x-1) % n, (y+1) % n
        if arr[x, y]:
            x, y = (x+2) % n, (y-1) % n
        arr[x, y] = i
    return arr


def medjig():
    size = 3
    arr = np.arange(0, size+1)
    np.random.shuffle(arr)
    arr.resize(2, 2)
    return arr


def medjig_creator(n):
    s = n // 2

    target = 3 * s
    retry = False
    while True:
        med = np.array([0])

        for _1 in range(s):
            temp = medjig()
            for _2 in range(s - 1):
                temp = np.concatenate((temp, medjig()), 1)
            for t in temp:
                if sum(t) != target:
                    # print(sum(t), target)
                    retry = True
                    break
            if retry:
                break
            if med.any():
                med = np.concatenate((med, temp), 0)
            else:
                med = temp[:]
        if retry:
            continue
        if validate_square(med):
            break

    return med


def concat_siamese(n):
    return np.repeat(np.repeat(siamese_square(n), 2, 0), 2, 1)


def magic_square_2(n):
    siam = concat_siamese(n//2)
    med = medjig_creator(n)

    res = np.zeros((n, n), dtype=int)
    for a in range(n):
        for b in range(n):
            res[a, b] = siam[a, b] + (9 * med[a, b])
    return res


def magic_square_2nd(n):
    """ http://www.math.wichita.edu/~richardson/mathematics/magic%20squares/even-ordermagicsquares.html """
    size = n // 2
    start = size * size
    arr0 = np.concatenate((siamese_square(size), siamese_square(size, (2 * start) + 1)), 1)
    arr1 = np.concatenate((siamese_square(size, (3 * start) + 1), siamese_square(size, start + 1)), 1)
    res = np.concatenate((arr0, arr1), 0)

    exchanger = (n - 2) // 4
    for x in range(exchanger-1):
        res[:, x] = np.roll(res[:, x], size, 0)
        res[:, n - x - 1] = np.roll(res[:, n - x - 1], size, 0)
    res[:, exchanger-1] = np.roll(res[:, exchanger-1], size, 0)
    res[n//4, exchanger-1], res[(3*n)//4, exchanger-1] = res[(3*n)//4, exchanger-1], res[n//4, exchanger-1]
    res[n//4, exchanger], res[(3*n)//4, exchanger] = res[(3*n)//4, exchanger], res[n//4, exchanger]
    return res


def validate_square(sq):
    s = sum(np.diagonal(sq, axis1=1, axis2=0))
    for column in sq:
        if s != sum(column):
            return False
    for row in np.rot90(sq):
        if s != sum(row):
            return False
    return s


def main():
    # required: n >= 3
    n = 18
    magic = -1
    if n % 4 == 0:
        magic = magic_square_4(n)
    elif n % 2 != 0:
        magic = siamese_square(n)
    elif n % 2 == 0:
        # magic = magic_square_2(n)
        magic = magic_square_2nd(n)
    print(magic, validate_square(magic))


if __name__ == "__main__":
    main()
