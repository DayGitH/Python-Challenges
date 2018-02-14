"""
[2016-09-23] Challenge #284 [Hard] Winning the Tournament

https://www.reddit.com/r/dailyprogrammer/comments/545a7x/20160923_challenge_284_hard_winning_the_tournament/

# Description
The basket weaving world championships are finally about to begin, and
everybody is bubbling with excitement. The tournament will be an intense
battle between **16** people. Each competitor has a weaving skill level,
a positive integer below 10^(6). We'll denote the n^th person's skill level
as `A[n]`.
Here’s how the winner of the championship will be decided:
1. The *remaining* competitors are randomly paired off with each other (a
pairing is chosen uniformly from all possible pairings at random).
2. Each pair has an intense one-on-one weaving battle! The probability that
person `n` wins a battle against person `k` is `A[n] / (A[n] + A[k])`.
3. The loser of each one-on-one battle is ejected from the tournament.
4. Repeat steps 1-3 until only one competitor remains. That remaining person
wins! (Note that with 16 people there will always be exactly four rounds of
pairings)
You can hardly wait for the matches to begin, so you would like to know
beforehand the probability that each competitor will win the tournament given
all their skill levels.
# Formal Inputs and Outputs
## Input description
Your input will be a space separated list of 16 integers in the range 1 to
10^(6)-1 inclusive.
## Output description
Output 16 real numbers between 0 and 1, where the n^th value is the
probability that the n^th person will win the tournament. Make sure each
number has at least 6 places after the decimal point.
## Sample Inputs and Outputs
### Sample 1 Input
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
### Sample 1 Output
    0.000106 0.001101 0.003752 0.008352 0.014896 0.023237 0.033171 0.044485
    0.056975 0.070457 0.084769 0.099768 0.115334 0.131363 0.147766 0.164466
### Sample 1 Input
    5 10 13 88 45 21 79 9 56 21 90 55 17 35 85 34
### Sample 1 Output
    0.000124 0.001200 0.002616 0.180212 0.054654 0.009631 0.151723 0.000867
    0.083360 0.009631 0.186620 0.080611 0.005531 0.032281 0.170648 0.030291
# Bonus
If you're stuck, try these easier versions of the same problem:
## Intermediate Sample Input
    1 2 3 4 5 6 7 8
## Intermediate Sample Output
    0.004884 0.024842 0.056171 0.094499 0.136913 0.181597 0.227421 0.273674
## Easy Sample Input
    1 2 3 4
## Easy Sample Output
    0.063862 0.185608 0.312857 0.437672
# Challenge
Get your code to run as quickly as possible. For languages with a speed
comparable to C++, try to get it to run in under 10 seconds.
# Credit
This challenge [was suggested](https://redd.it/3drz14) by /u/Cephian. If you
have a challenge idea, please share it in /r/dailyprogrammer_ideas and there's
a good chance we'll use it.
"""


def main():
    pass


if __name__ == "__main__":
    main()
