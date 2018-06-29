"""
[7/23/2012] Challenge #80 [easy] (Anagrams)

https://www.reddit.com/r/dailyprogrammer/comments/x0v3e/7232012_challenge_80_easy_anagrams/

As all of us who have read "Harry Potter and the Chamber of Secrets" knows, the reason He-Who-Must-Not-Be-Named chose
his creepy moniker is that "I Am Lord Voldemort" is an anagram for his birthname, "Tom Marvolo Riddle". 
I've never been good at these kinds of word-games (like anagrams), I always find it hard to figure out that stuff
manually. I find it much more enjoyable to write computer programs to solve these problems for me. In the spirit of
that, today's problem is to find simple one-word anagrams for other words.
Write a program that given a word will find all one-word anagrams for that word. So, for instance, if you put in
"LEPROUS", it should return "PELORUS" and "SPORULE". As a dictionary, use [this file]
(http://code.google.com/p/dotnetperls-controls/downloads/detail?name=enable1.txt), which is a 1.8 mb text-file
with one word listed on each line, each word listed in lower-case. In this problem description, I've used upper-case
for all words and their anagrams, but that is entirely optional, it's perfectly all right to use lower-case if you want
to. 
Using your program, find all the one-word anagrams for "TRIANGLE".
***
*(by the way, in case anyone is curious: a "PELORUS" is "a sighting device on a ship for taking the relative bearings
of a distant object", which I imagine basically is a telescope bolted onto a compass, and a "SPORULE" is "a small
spore")*
***
Bonus: if you looked up the anagrams for "PAGERS", you'd find that there was actually quite a few of them: "GAPERS",
"GASPER", "GRAPES", "PARGES" and "SPARGE". Those five words plus "PAGERS" make a six-word "anagram family". 
Here's another example of an anagram family, this time with five words: "AMBLERS", "BLAMERS", "LAMBERS", "MARBLES" and
"RAMBLES".
What is the largest anagram family in the dictionary I supplied? What is the second largest?
"""

from collections import defaultdict


def build_dict(file):
    return_dict = defaultdict(list)
    with open(file, 'r') as f:
        data = f.read()
    for d in data.split():
        d = d.upper()
        return_dict[sort_word(d)].append(d)
    return return_dict


def sort_word(word):
    return ''.join(sorted(word))


def find_anagrams(word, word_dict):
    return word_dict[sort_word(word.upper())]


def top_anagram_families(word_dict, n=3):
    sort = sorted(word_dict, key=lambda k: len(word_dict[k]), reverse=True)
    for i in range(n):
        print(word_dict[sort[i]])


def main():
    word_dict = build_dict('enable1.txt')
    print(find_anagrams('triangle', word_dict))
    print('\ntop anagram families: ')
    top_anagram_families(word_dict)


if __name__ == "__main__":
    main()
