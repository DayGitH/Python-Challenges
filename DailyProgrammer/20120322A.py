"""
A Palindrome[http://en.wikipedia.com/wiki/Palindrome] is a sequence that is the same in reverse as it is forward.
I.e. hannah, 12321.

Your task is to write a function to determine whether a given string is palindromic or not.

Bonus: Support multiple lines in your function to validate Demetri Martin's 224 word palindrome
poem[http://www.pastemagazine.com/articles/2009/02/demetri-martins-palindrome-poem.html].

Thanks to _lerp for submitting this idea in /r/dailyprogrammer_ideas[3] !
"""

import string


def ispalindrome(txt):
    exc = set(string.punctuation)
    strip = txt.lower().replace('\n', '').replace(' ', '')
    strip = ''.join(c for c in strip if c not in exc)
    print(strip)
    print(strip[::-1])
    return strip == strip[::-1]

if __name__ == '__main__':
    with open('20120322A.txt') as f:
        text = f.read()

    print(ispalindrome(text))
