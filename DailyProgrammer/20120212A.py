'''
You're challenge for today is to create a random password generator!
For extra credit, allow the user to specify the amount of passwords to generate.
For even more extra credit, allow the user to specify the length of the strings he wants to generate!
'''

import string
import random

print('Please specify password length')
pswd_len = 'x'
while not isinstance(pswd_len, int):
    try:
        pswd_len = int(input('> '))
    except:
        print('Invalid. Try again.')

print('Please specify the number of passwords')
num_of_pswd = 'x'
while not isinstance(num_of_pswd, int):
    try:
        num_of_pswd = int(input('> '))
    except:
        print('Invalid. Try again.')

for num in range(num_of_pswd):
    password = ''
    for n in range(pswd_len):
        password += random.choice(string.ascii_letters + string.punctuation)
    print(password)