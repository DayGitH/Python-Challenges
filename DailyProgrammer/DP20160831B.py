"""
[2016-08-31] Challenge #281 [Intermediate] Dank usernames

https://www.reddit.com/r/dailyprogrammer/comments/50hbtp/20160831_challenge_281_intermediate_dank_usernames/

# Description
If you're named Danny Kyung or Matthew Emes, it opens up the possibility of justifying your use of usernames such as
[dank](https://github.com/dank) or [memes](https://github.com/memes).
Your task is to find the longest word such that it satisfies the criteria - that is, it is a substring of the given
string but not necessarily consecutively (we can call it a sparse substring). 
If there are multiple words of same maximum length, output all of them.
You may use the [the Enable word list](http://norvig.com/ngrams/enable1.txt), or some other reasonable English word
list. Every word in your output must appear in your word list.
# Formal Inputs & Outputs
## Input description
One string.
## Example Inputs
    Donald Knuth
    Alan Turing
    Claude Shannon
## Output description
A single word (ouptut the lengthiest word/words in case of multiple words satisfying the criteria)
## Example outputs
    Donut (because **Don**ald k**nut**h)
    Alanin, Anting
    Cannon
Note : Your outputs may differ from these outputs depending on the word list you are using
## Challenge Inputs
    Ada Lovelace
    Haskell Curry
    **Your own name!**
# Bonus
Find a combination of words that satisfy the criteria. For example, "AlantRing" in "**Alan T**ur**ing**".
In case of multiple combination of words that satisfy the criteria, find the word with the highest score and print
that, where the score is sum of squares of length of all the constituent words
For example, in "Alan Turing",   
score of AlantRing is  5^2 + 4^2 = 41,  
score of AlAnting is 2^2 + 6^2 = 40,  
score of Alanin is 6^2 = 36
and thus of the three, the first should be printed because of highest score.
## Bonus Inputs
    Donald Knuth
    Alan Turing
    Claude Shannon
    Ada Lovelace
    Haskell Curry
    **Your own name!**
# Finally
Have a good challenge idea like /u/automata-door did?
Consider submitting it to /r/dailyprogrammer_ideas
"""


def main():
    pass


if __name__ == "__main__":
    main()
