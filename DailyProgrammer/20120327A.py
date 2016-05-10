"""
Write a function that takes two base-26 numbers in which digits are represented by letters with A=0, B=1, ... Z=25 and
returns their product using the same notation. As an example, CSGHJ x CBA = FNEUZJA.

Your task is to write the base-26 multiplication function.

Try to be very efficient in your code!
"""

import string


def decode_to_decimal(number):
    number = number.upper()
    final = 0
    for n, a in enumerate(reversed(number)):
        # ord returns ascii number and -65 brings down number to decimal number
        final += (26**n) * (ord(a) - 65)
    return final


def encode_from_decimal(number):
    result = ''
    while number != 0:
        remainder = number % 26
        number = number // 26
        result += string.ascii_uppercase[remainder]

    return result[::-1]


if __name__ == '__main__':
    multiply = decode_to_decimal('CSGHJ') * decode_to_decimal('CBA')

    print(multiply)
    print(encode_from_decimal(int(multiply)))
