# -*- coding: utf-8 -*-

"""
Hi folks! We are in the midst of discussing how this subreddit will go about but for now how about we just concentrate
on challenges!

Write a function that takes two strings and removes from the first string any character that appears in the second
string. For instance, if the first string is “Daily Programmer” and the second string is “aeiou ” the result is
“DlyPrgrmmr”.

note: the second string has [space] so the space between "Daily Programmer" is removed
"""

string_one = 'Daily programmer'
string_two = 'aeiou '

working_set = list(string_one)
for a in string_two:
    working_set[:] = [x for x in working_set if x != a]

print(''.join(working_set))