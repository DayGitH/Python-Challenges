"""
[2017-09-13] Challenge #331 [Intermediate] Sum of digits of x raised to n

https://www.reddit.com/r/dailyprogrammer/comments/6zvjre/20170913_challenge_331_intermediate_sum_of_digits/

#Description
For some x^n, find the sum of its digits. The solution to this problem is extremely simple. Say, I give you 3^4. You
could calculate 3^n and add the digits.
However things might get a bit complex for 5^100. It's a 70-digit  number. You could come up with a larger data type
that could handle the product of that number and then you could add each number... but where's the fun in that?
This is today's challenge. Find the sum of the digits of some x^n without directly calculating the number and adding
the digits.
Some simple examples with values that you're familiar with:
2^5 = 32 = 3 + 2 = 5
5^3 = 125 = 1 + 2 + 5 = 8
2^7 = 1 + 2 + 8 = 11 
Note that I have not summed the digits of 11. 
We'll work with powers and bases greater than zero. 
# Input Description 
> Base Power
means base^power
> 2 ^ 1000
means 2^1000
# Output Description
Display the sum of the digits of base^power.
# Challenge Input
> 2 1234
> 11 4000 
> 50 3000
# Challenge Output 
>1636
>18313
> 9208
----------------------------
If you have any challenges, please share it at /r/dailyprogrammer_ideas!
Edit : If you're unable to come up with an idea, like the one is Project eulers 16, then feel free to solve it using
your own data types (if required). Please consider it as the last option. 
"""


def main():
    pass


if __name__ == "__main__":
    main()
