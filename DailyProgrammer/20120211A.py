'''
Welcome to cipher day!
write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore numbers, symbols, and whitespace.
for extra credit, add a "decrypt" function to your program!
'''

import sys

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Input the text for encryption,')
inp = input('> ').upper()

print('Shift left or right? (L/R)')
dir = input('> ')
if dir not in 'LR':
    sys.exit('Bad input. Please input L or R.')
print('Input the number of letters to shift by')
shift = int(input('> '))

output = ''

if dir == 'L':
    shift = 26 - shift

for i in inp:
    if i in alphabet:
        shifted = (alphabet.index(i) + shift) % 26
        print(i, alphabet.index(i)+1, shifted+1, alphabet[shifted])
        output += alphabet[shifted]
    else:
        output += i

print(inp, ' ', output)