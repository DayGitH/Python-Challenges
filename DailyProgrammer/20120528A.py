"""
As computer programmers are well aware, it can be very useful to write numbers using numerical bases other than the
familiar base 10 notation we use in everyday life. In computer programming, base 2
[http://en.wikipedia.org/wiki/Binary_number] and base 16 [http://en.wikipedia.org/wiki/Hexadecimal] are especially
handy. In base 2, the number 1234 becomes 10011010010 and in base 16 it becomes 4D2.

Because there are only 10 regular digits, when numbers are written in base 16, the first few letters of the alphabet
are added to represent the remaining required digits, so 'A' stands in for 10, 'B' for 11, 'C' for 12, 'D' for 13, 'E'
for 14 and 'F' for 15.

Of course, this trick of adding letters to stand in for numbers allows us to represent higher bases than 16; if you can
use all letters of the alphabet, you can represent bases up to base 36 (because there are ten regular digits and 26
"letter-digits"). So for instance, 12345678 becomes 1L2FHE in base 23 and 4IDHAA in base 19.

Write a program that will take a number and convert it to any base between 2 and 36. Have the program print out
19959694 in base 35 and 376609378180550 in base 29.

NOTE: Many languages have this built in as a library function. For instance, in Java, the function Integer.toString(i,
radix) does exactly this. However, the entire point of this challenge is to write the program yourself, so you are not
allowed to use any library functions like this.

BONUS: A number is said to be "palindromic in base N" if, when written in base N the number is the same backwards and
forwards. So, for instance, the number 16708 is palindromic in base 27, because in base 27 the number is written as
MOM, obviously a palindrome. The number 12321 is a palindrome in in base 10, because 12321 written backwards is 12321.
Some numbers are palindromic in several bases, the number 15167 for instance is palindromic in bases 9, 27, 28, 35 and
36.

In what bases is the number 10858 palindromic?

Thanks to Hannoii for suggesting this problem and /r/dailyprogrammer_ideas! If you have a problem that you think would
be good for this subreddit, why not head over there and suggest it?
"""

START_BASE = '0123456789'
END_BASE = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'


def to_decimal(num):
    num = str(num)[::-1]
    base = len(START_BASE)
    s = 0
    for n in range(len(num)):
        s += int(num[n]) * (base ** n)
    return s


def to_base(dec, base):
    r = ''
    l = len(base)
    while dec:
        r = base[dec % l] + r
        dec //= l
    return r


def arb_base_convertor(num, b):
    dec = to_decimal(num)
    res = to_base(dec, END_BASE[:b])
    return res


def find_palindromes(num):
    res = []
    for n in range(2, 64+1):
        r = arb_base_convertor(num, n)
        if palin(r):
            res.append((n, r))

    return res


def palin(num):
    return str(num) == str(num)[::-1]


def main():
    print(arb_base_convertor(19959694, 35))
    print(arb_base_convertor(376609378180550, 29))

    print(find_palindromes(10858))

if __name__ == "__main__":
    main()
