"""
For the easy part of today's challenge, we considered numbers that are palindromes in different bases. For this
problem, lets only concern ourselves with numbers that are palindromes in base 10.

Define a function P(N) that takes as input a number N, and returns the smallest base 10 palindrome larger than N (i.e.
it returns the "next" palindrome after N). So, for instance:
P(808) = 818
P(999) = 1001
P(2133) = 2222
What is P( 339 )?
BONUS: What is P( 7100 )

Thanks to ashashwat for suggesting this problem at /r/dailyprogrammer_ideas! (problem originally from here) If you have
a problem that you think would be good for this subreddit, why not head over there and suggest it?
"""

def P(num):
    num += 1
    num = str(num)
    l = len(num)

    if l % 2:
        mir = num[:int(l/2)] + num[l//2::-1]
    else:
        mir = num[:int(l/2)] + num[l//2-1::-1]
    if int(mir) < int(num):
        if l % 2:
            return mir[:l//2] + str(int(mir[l//2])+1) + mir[l//2+1:]

        else:
            return mir[:l//2-1] + str(int(mir[l//2-1:l//2+1])+11) + mir[l//2+1:]
    return mir

def main():
    print(808, P(808))
    print(999, P(999))
    print(2133, P(2133))
    print(3 ** 39, P(3 ** 39))
    print('')

    print(7**100)
    print(P(7**100))

if __name__ == "__main__":
    main()
