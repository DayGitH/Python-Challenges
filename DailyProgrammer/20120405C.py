"""
Let's play Lingo! Click here [dead link] for an idea of how the game works. Now write a program that reads a random
5-letter word from a dictionary file and plays the game Lingo. If you're doing a text-based version, you can surround
the correct letters at the correct location with [] and correct letters at the wrong location with ().
"""

import random
import copy


def gen_face(guess, state):
    w = []
    for a in state:
        if a == "0":
            w += [" ", " "]
        elif a == "1":
            w += ["(", ")"]
        elif a == "2":
            w += ["[", "]"]

    for b in reversed(range(len(guess))):
        w.insert((2*b)+1, guess[b])
    return ''.join(w)


def check_guess(word, inp):
    word_length = len(word)
    guess = word_length * ["."]
    state = word_length * ["0"]
    rem_word = copy.deepcopy(guess)
    rem_inp = copy.deepcopy(guess)
    for n, x in enumerate(zip(word, inp)):
        # print(n, x)
        if x[0] == x[1]:
            guess[n] = x[0]
            state[n] = "2"
        else:
            rem_word[n] = x[0]
            rem_inp[n] = x[1]
    for y in (set(rem_word) & set(rem_inp)):
        for n, x in enumerate(rem_inp):
            if x == y and x != '.':
                guess[n] = x
                state[n] = "1"
    return guess, state

word_length = 5
with open("wordlist.txt", "r") as f:
    data = f.read().split()

five_list = []
for d in data:
    if len(d) == word_length:
        five_list.append(d)

word = random.choice(five_list)
guess = word[0] + ((word_length-1) * ".")
state = "2" + ((word_length-1) * "0")

for i in range(10):
    print(gen_face(guess, state))
    print("Input attempt:")
    w = input("> ")
    if word == w:
        print('Congrats! You correctly guessed {} after {} tries'.format(word, i+1))
        break
    else:
        guess, state = check_guess(word, w)
else:
    print('Fail! The word was {}'.format(word))
