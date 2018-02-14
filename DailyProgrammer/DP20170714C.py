"""
[2017-07-14] Challenge #323 [Hard] Difference coverage

https://www.reddit.com/r/dailyprogrammer/comments/6n8qb7/20170714_challenge_323_hard_difference_coverage/

# Description
Given a positive integer N, return a set of integers between 0 and N such that every integer is equal to difference of
two in the set, [modulo
N](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/congruence-modulo). Make the set
as small as you can.
For example, given N = 26, you might return the set `{ 0, 3, 9, 11, 21, 22 }`, (which has a size of 6). Every integer
is the difference between two (not necessarily unique) integers in this set, modulo 26. For instance, 7 = 3 - 22 (mod
26).
It's not good enough to write a program that will eventually complete. You must be able to actually run your program to
completion for five-digit values of N. Post (or link to) your output for N = 12345 along with your solution.
As far as I know, the size of the optimal (smallest) set is an open question, so your program does not have to be
optimal. But it needs to be pretty close. The best I've found for N = 12345 is a set of size 179, so aim for that.
# Challenge
When this post is seven days old, +1 gold medal flair will be awarded to the submitter who posts the smallest valid
output for N = 123456. Smallest here refers to the size of the set of integers in the output.
If this turns out to be easier than I anticipate, there may be a tie. In that case, as a tiebreaker, also post your
output for N = 1234567. If there's still a tie, post for 12345678, 123456789, 1234567890, 12345678901, etc. I'll also
look at time of posting to break a tie if necessary.
# Inspiration
This problem was inspired by me trying to make a minimal set of rows for a [Caesar shift
cipher](https://learncryptography.com/classical-encryption/caesar-cipher) key. The set `{ 0, 3, 9, 11, 21, 22 }`
corresponds to the rows:
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    XYZABCDEFGHIJKLMNOPQRSTUVW
    RSTUVWXYZABCDEFGHIJKLMNOPQ
    PQRSTUVWXYZABCDEFGHIJKLMNO
    FGHIJKLMNOPQRSTUVWXYZABCDE
    EFGHIJKLMNOPQRSTUVWXYZABCD
Now I have a key for any Caesar cipher by comparing two rows. For instance, the shift A->H (shifting by 7 places)
corresponds to mapping the 2nd row to the 6th row, because 7 = 3 - 22 (mod 26). You didn't need to know this in order
to solve the problem, but I thought I'd mention it.
"""


def main():
    pass


if __name__ == "__main__":
    main()
