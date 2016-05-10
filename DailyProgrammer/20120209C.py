'''
we all know the classic "guessing game" with higher or lower prompts. lets do a role reversal; you create a program that will guess numbers between 1-100, and respond appropriately based on whether users say that the number is too high or too low. Try to make a program that can guess your number based on user input and great code!

'''

import random
import numpy

got_answer = False

max = 100
min = 0

try_count = 0

while not got_answer:
    try_count += 1

    num = -1
    while (num > 1) or (num < 0):
        num = .125 * numpy.random.randn() + 0.5
        print(num)

    guess = int(((max - min) * num) + min)

    print('1. Higher')
    print('2. Correct!')
    print('3. Lower')
    print('\nIs your number {}'.format(guess))
    response = input('> ')


    if response == '2':
        got_answer = True
        if try_count > 1:
            print('\nHurray! I guessed {} in {} tries!!!'.format(guess, try_count))
        else:
            print('\nHurray! I guessed {} in the first try!!! WOOHOO!'.format(guess, try_count))
    elif response == '1':
        min = guess + 1
    elif response == '3':
        max = guess - 1

    if min > max:
        got_answer = True
        print('ERROR! ERROR! ERROR! Master did not answer the questions properly!')