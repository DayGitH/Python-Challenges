"""
Before I get to today's problem, I'd just like to give a warm welcome to our two new moderators, nooodl and Steve132! We
decided to appoint two new moderators instead of just one, because rya11111 has decided to a bit of a break for a while.

I'd like to thank everyone who applied to be moderators, there were lots of excellent submissions, we will keep you in
mind for the next time. Both nooodl and Steve132 have contributed some excellent problems and solutions, and I have no
doubt that they will be excellent moderators.

Now, to today's problem! Good luck!

If a right angled triangle has three sides A, B and C (where C is the hypothenuse), the pythagorean theorem tells us
that A**2 + B**2 = C**2

When A, B and C are all integers, we say that they are a pythagorean triple. For instance, (3, 4, 5) is a pythagorean
triple because 3**2 + 4**2 = 5**2 .

When A + B + C is equal to 240, there are four possible pythagorean triples: (15, 112, 113), (40, 96, 104),
(48, 90, 102) and (60, 80, 100).

Write a program that finds all pythagorean triples where A + B + C = 504.

Edit: added example.
"""


def pyth_triples(n):
    for a in range(n//2):
        for b in range(a+1, n//2):
            for c in range(b+1, n//2):
                if a+b+c == n and (a**2) + (b**2) == (c**2):
                    print([a, b, c])
                elif a+b+c > n:
                    break
            if a+b > n:
                break


def main():
    pyth_triples(504)


if __name__ == "__main__":
    main()
