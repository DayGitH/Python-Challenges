"""
Most credit card numbers, and many other identification numbers including the Canadian Social Insurance Number, can be
validated by an algorithm developed by Hans Peter Luhn of IBM, described in U. S. Patent 2950048 in 1954 (software
patents are nothing new!), and now in the public domain. The Luhn algorithm will detect almost any single-digit error,
almost all transpositions of adjacent digits except 09 and 90, and many other errors.

The Luhn algorithm works from right-to-left, with the right-most digit being the check digit. Alternate digits,
starting with the first digit to left of the check digit, are doubled. Then the digit-sums of all the numbers, both
undoubled and doubled, are added. The number is valid if the sum is divisible by ten.

For example, the number 49927398716 is valid according to the Luhn algorithm. Starting from the right, the sum is
6 + (2) + 7 + (1 + 6) + 9 + (6) + 7 + (4) + 9 + (1 + 8) + 4 = 70, which is divisible by 10; the digit-sums of the
doubled digits have been shown in parentheses.

Your task is to write two functions, one that adds a check digit to a identifying number and one that tests if an
identifying number is valid.

source: programmingpraxis.com
"""


def get_check_number(inp):
    total = 0
    for n, i in enumerate(reversed(inp)):
        if n % 2 == 0:
            total = add_digits(total, 2*int(i))
        else:
            total = add_digits(total, int(i))

    return inp + str(10 - (total % 10))


def add_digits(total, number):
    if number // 10 > 0:
        while number:
            total, number = total + number % 10, number // 10
        return total
    else:
        return total + int(number)


def validate_check_number(inp):
    total = 0
    for n, i in enumerate(reversed(inp)):
        if n % 2 == 1:
            total = add_digits(total, 2*int(i))
        else:
            total = add_digits(total, int(i))

    return total % 10 == 0


if __name__ == '__main__':
    num = '4992739871'

    checked = get_check_number(num)
    print(checked)

    print(validate_check_number('49927398716'))
