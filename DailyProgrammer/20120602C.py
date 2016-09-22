"""
Two strings A and B are said to have a common substring called C, if C is embedded somewhere in both A and B. For
instance, "ble" is a common substring for "Double, double, toil and trouble" and "Fire burn and cauldron bubble"
(because, as you can see, "ble" is part of both "Double" and "Bubble"). It is, however, not the longest common
substring, the longest common substring is " and " (5 characters long for vs. 3 characters long for "ble").

Define two pseudo-random number generators, P(N) and Q(N), like this:
P(0) = 123456789
P(N) = (22695477 * P(N-1) + 12345) mod 1073741824
Q(0) = 987654321
Q(N) = (22695477 * Q(N-1) + 12345) mod 1073741824

Thus, they're basically the same except for having different seed values. Now, define SP(N) to be the first N values of
P concatenated together and made into a string. Similarly, define SQ(N) as the first N values of Q concatenated
together and made into a string. So, for instance:

SP(4) = "123456789752880530826085747576968456"
SQ(4) = "987654321858507998535614511204763124"

The longest common substring for SP(30) and SQ(30) is "65693".

Find the longest common substring of SP(200) and SQ(200)

BONUS: Find the longest common substring of SP(4000) and SQ(4000).
"""

import numpy as np

def get_string(N, P, Q):
    P, Q = [P], [Q]
    for i in range(N - 1):
        P.append((22695477 * P[-1] + 12345) % 1073741824)
        Q.append((22695477 * Q[-1] + 12345) % 1073741824)
    SP = ''.join(map(str, P))
    SQ = ''.join(map(str, Q))

    return SP, SQ


def longest_common_substring(str1, str2):
    l1 = len(str1)
    l2 = len(str2)

    if l2 < l1:
        l1, l2 = l2, l1
        str1, str2 = str2, str1

    L = np.zeros((l1, l2))
    z = 0
    ret = []
    """ based on pseudocode from wikipedia """
    for i in range(l1):
        for j in range(l2):
            if str1[i] == str2[j]:
                if i == 0 or j == 0:
                    L[i, j] = 1
                else:
                    L[i, j] = L[i-1, j-1] + 1
                if L[i, j] > z:
                    z = int(L[i, j])
                    ret = [str1[i-z+1:i+1]]
                elif L[i, j] == z:
                    ret.append(str1[i-z+1:i+1])
            else:
                L[i, j] = 0

    if len(ret) == 1:
        return ret[0]
    else:
        return ret


def main():
    N = 200
    P_init, Q_init = 123456789, 987654321
    SP, SQ = get_string(N, P_init, Q_init)

    print(longest_common_substring(SP, SQ))

if __name__ == "__main__":
    main()
