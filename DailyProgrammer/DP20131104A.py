"""
[11/4/13] Challenge #140 [Easy] Variable Notation

https://www.reddit.com/r/dailyprogrammer/comments/1q6pq5/11413_challenge_140_easy_variable_notation/

# [](#EasyIcon) *(Easy)*: Variable Notation
When writing code, it can be helpful to have a standard ([Identifier naming
convention](http://en.wikipedia.org/wiki/Identifier_naming_convention)) that describes how to define all your variables
and object names. This is to keep code easy to read and maintain. Sometimes the standard can help describe the type
(such as in [Hungarian notation](http://en.wikipedia.org/wiki/Hungarian_notation)) or make the variables visually easy
to read ([CamcelCase notation](http://en.wikipedia.org/wiki/CamelCase) or
[snake_case](http://en.wikipedia.org/wiki/Snake_case)).
Your goal is to implement a program that takes an english-language series of words and converts them to a specific
variable notation format. Your code must support CamcelCase, snake_case, and capitalized snake_case.
# Formal Inputs & Outputs
## Input Description
On standard console input, you will be given an integer one the first line of input, which describes the notation you
want to convert to. If this integer is zero ('0'), then use CamcelCase. If it is one ('1'), use snake_case. If it is
two ('2'), use capitalized snake_case. The line after this will be a space-delimited series of words, which will only
be lower-case alpha-numeric characters (letters and digits).
## Output Description
Simply print the given string in the appropriate notation.
# Sample Inputs & Outputs
## Sample Input
    0
    hello world
    1
    user id
    2
    map controller delegate manager
## Sample Output
    0
    helloWorld
    1
    user_id
    2
    MAP_CONTROLLER_DELEGATE_MANAGER
## Difficulty++
For an extra challenge, try to convert from one notation to another. Expect the first line to be two integers, the
first one being the notation already used, and the second integer being the one you are to convert to. An example of
this is:
Input:
    1 0
    user_id
Output:
    userId
"""


def main():
    pass


if __name__ == "__main__":
    main()
"""
[11/4/13] Challenge #139 [Easy] Pangrams

https://www.reddit.com/r/dailyprogrammer/comments/1pwl73/11413_challenge_139_easy_pangrams/

# [](#EasyIcon) *(Easy)*: Pangrams
[Wikipedia](http://en.wikipedia.org/wiki/Pangram) has a great definition for Pangrams: "*A pangram or holoalphabetic
sentence for a given alphabet is a sentence using every letter of the alphabet at least once.*" A good example is the
English-language sentence "[The quick brown fox jumps over the lazy
dog](http://en.wikipedia.org/wiki/The_quick_brown_fox_jumps_over_the_lazy_dog)"; note how all 26 English-language
letters are used in the sentence.
Your goal is to implement a program that takes a series of strings (one per line) and prints either True (the given
string is a pangram), or False (it is not).
**Bonus:** On the same line as the "True" or "False" result, print the number of letters used, starting from 'A' to
'Z'. The format should match the following example based on the above sentence:
    a: 1, b: 1, c: 1, d: 1, e: 3, f: 1, g: 1, h: 2, i: 1, j: 1, k: 1, l: 1, m: 1, n: 1, o: 4, p: 1, q: 1, r: 2, s: 1,
t: 2, u: 2, v: 1, w: 1, x: 1, y: 1, z: 1
# Formal Inputs & Outputs
## Input Description
On standard console input, you will be given a single integer on the first line of input. This integer represents the
number of lines you will then receive, each being a string of alpha-numeric characters ('a'-'z', 'A'-'Z', '0'-'9') as
well as spaces and [period](http://en.wikipedia.org/wiki/Period_(punctuation\)).
## Output Description
For each line of input, print either "True" if the given line was a pangram, or "False" if not.
# Sample Inputs & Outputs
## Sample Input
    3
    The quick brown fox jumps over the lazy dog.
    Pack my box with five dozen liquor jugs
    Saxophones quickly blew over my jazzy hair
## Sample Output
    True
    True
    False
# Authors Note: [Horay, we're back with a queue of new challenges](http://i.imgur.com/chKCAPM.jpg)! Sorry fellow
r/DailyProgrammers for the long time off, but we're back to business as usual.
"""


def main():
    pass


if __name__ == "__main__":
    main()
