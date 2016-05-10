'''
Your task is to implement the interactive game of hangman [http://en.wikipedia.org/wiki/Hangman_(game)]

bonus point for making the game unique. be more creative!
'''

import random

def hangman(n):
    body_parts = ['(_)', '|', '/', '\\', '\\', '/']

    for i in range(n,6):
        body_parts[i] = ' '
    print('  _______')
    print(' |/      |')
    print(' |      {}'.format(body_parts[0]))
    print(' |      {}{}{}'.format(body_parts[4], body_parts[1], body_parts[5]))
    print(' |       {}'.format(body_parts[1]))
    print(' |      {} {}'.format(body_parts[2], body_parts[3]))
    print(' |')
    print('_|___')

with open('wordlist.txt', 'r') as f:
    words = f.read().splitlines()

rng = random.SystemRandom()
target = words[rng.randint(0, len(words) - 1)]

# print(target)

gameover = False

sol = '*' * len(target)
tries = 6
MAX_TRIES = tries
wrong = ''

while not gameover:
    hangman(MAX_TRIES - tries)
    print(sol)
    print(wrong)

    l = input('> ')

    if (not l.isalpha()) or len(l) > 1:
        print('Please enter a letter')
    elif (l in wrong) or (l in sol):
        print('This letter has already been attempted')
    elif l in target:
        print('Correct!')
        for n, t in enumerate(target):
            if t == l:
                sol = sol[:n] + l + sol[n+1:]
    else:
        print('Incorrect!')
        tries -= 1
        wrong += l + ' '

    if sol == target:
        gameover = True
        print('Solution: {}'.format(target))
        print('Winner!!!')
    if tries == 0:
        gameover = True
        print('Loser!')
        print('Solution: {}'.format(target))