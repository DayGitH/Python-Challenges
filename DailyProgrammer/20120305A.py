"""
Often times in commercials, phone numbers contain letters so that they're easy to remember (e.g. 1-800-VERIZON).
Write a program that will convert a phone number that contains letters into a phone number with only numbers and the
appropriate dash. Click here[https://en.wikipedia.org/wiki/Telephone_keypad] to learn more about the telephone keypad.

Example Execution: Input: 1-800-COMCAST Output: 1-800-266-2278
"""

import re

l_to_n = {'a': '2', 'b': '2', 'c': '2',
          'd': '3', 'e': '3', 'f': '3',
          'g': '4', 'h': '4', 'i': '4',
          'j': '5', 'k': '5', 'l': '5',
          'm': '6', 'n': '6', 'o': '6',
          'p': '7', 'q': '7', 'r': '7', 's': '7',
          't': '8', 'u': '8', 'v': '8',
          'w': '9', 'x': '9', 'y': '9', 'z': '9'}


number = input('Enter phone number: ').lower()

chars = '-() '
number = re.sub({}.format(chars), '', number)
# number = number.replace('-', '')
# number = number.replace('(', '')
# number = number.replace(')', '')
# number = number.replace(' ', '')

output = ''
for l in number:
    if l.isnumeric():
        output += l
    else:
        output += l_to_n[l]

if len(output) == 11:
    print('{}-{}-{}'.format(output[0:1], output[1:4], output[4:11]))
elif len(output) == 10:
    print('{}-{}'.format(output[0:3], output[3:10]))
else:
    print(output)