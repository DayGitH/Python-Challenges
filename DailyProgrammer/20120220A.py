'''
Write a small program that can take a string:
"hi!"
and print all the possible permutations of the string:
"hi!"
"ih!"
"!hi"
"h!i"
"i!h"
etc...
thanks to hewts for this challenge!
'''

import itertools

# word = input('Enter word:')
#
# perm = itertools.permutations(word)
#
# for p in perm:
#     final_word = ''
#     for i in p:
#         final_word += i
#     print(final_word)

# One line implementation of my solution above
print('\n'.join([''.join(x) for x in itertools.permutations(input('Enter word:'))]))