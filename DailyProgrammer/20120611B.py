"""
You can use the reverse(N, A) procedure defined in today's easy problem [20120611A] to completely sort a list. For
instance, if we wanted to sort the list [2,5,4,3,1], you could execute the following series of reversals:

A = [2, 5, 4, 3, 1]

reverse(2, A)       (A = [5, 2, 4, 3, 1])
reverse(5, A)       (A = [1, 3, 4, 2, 5])
reverse(3, A)       (A = [4, 3, 1, 2, 5])
reverse(4, A)       (A = [2, 1, 3, 4, 5])
reverse(2, A)       (A = [1, 2, 3, 4, 5])

And the list becomes completely sorted, with five calls to reverse(). You may notice that in this example, the list is
being built "from the back", i.e. first 5 is put in the correct place, then 4, then 3 and finally 2 and 1.

Let s(N) be a random number generator defined as follows:

s(0) = 123456789
s(N) = (22695477 * s(N-1) + 12345) mod 1073741824

Let A be the array of the first 10,000 values of this random number generator. The first three values of A are then
123456789, 752880530 and 826085747, and the last three values are 65237510, 921739127 and 926774748

Completely sort A using only the reverse(N, A) function.
"""


def s(n, sp):
    if n == 0:
        return 123456789
    else:
        return (22695477 * sp + 12345) % 1073741824


def reverse(n, a):
    return a[:n][::-1] + a[n:]


def basic_revsort(a):
    copy_a = a[:]

    sort_loc = len(a)
    count = 0
    while copy_a:
        num = max(copy_a)
        copy_a.remove(num)

        i = a.index(num)+1
        if i == sort_loc:
            pass
        elif i == 0:
            a = reverse(sort_loc, a)
            count += 1
        else:
            a = reverse(i, a)
            a = reverse(sort_loc, a)
            count += 2
        sort_loc -= 1
    print(count)
    return a


def main():
    generate = 10000
    result = -1
    out = []
    for i in range(generate):
        result = s(i, result)
        out.append(result)
    # out = [2, 5, 4, 3, 1]

    out = basic_revsort(out)
    print(sorted(out))
    print(out)


if __name__ == "__main__":
    main()
