"""
[2018-02-09] Challenge #350 [Hard] Which Number Recurs First

https://www.reddit.com/r/dailyprogrammer/comments/7wfd0n/20180209_challenge_350_hard_which_number_recurs/

# Description
Working with very large data sets is an increasingly common activity in efforts such as web analytics and Internet
advertising. Efficiently keeping track of values when you have around 2^64 possible values is the challenge. 
Today's challenge is to read a steady stream of distinct values and report on the first one that recurs. Your program
should be able to run an arbitrary number of times with distinct, infinite sequences of input and yield the
_probabilisticly_ correct value. 
## Data source
I spent a good chunk of my morning trying to find a stream of random values for you to consume. I could not find one
(e.g. a PRNG as a service) so I decided to use a local PRNG implementation. 
For this challenge, please use the following random number generator based on the Isaac design.
https://github.com/dkull/Isaac-CSPRNG/blob/master/Isaac.py
The above code expects a maximum integer passed to the `rand()` method, and for the purposes of this challenge set it
to `sys.maxsize`. Then emit a steady stream of numbers and use your program to detect the first recurring value.
    import sys
    import Isaac
    i = Isaac.Isaac(noblock=False)
    while True:
        print(i.rand(sys.maxsize))
# Notes
This piece may prove a useful start: [PROBABILISTIC DATA STRUCTURES FOR WEB ANALYTICS AND DATA
MINING](https://highlyscalable.wordpress.com/2012/05/01/probabilistic-structures-web-analytics-data-mining/). 
# Edited to Add
A concrete solution is unlikely to be found since you are sifting through up to 2^64 possible values. As such, a
probabilistically correct solution is adequate. Just no guessing. If you're writing your own PRNG or calling `rand()`,
you're doing this one wrong. Run the above Python code and read the values, that PRNG was chosen because it should
stress your program. Don't use your own calls to your PRNG. If you're using a built-in tree, map, or set implementation
you're doing this one wrong - it'll blow up. 
I developed this challenge because I've been interested in some data science challenges since someone asked for more
practical, real world type of challenges. This is a challenge you'd run into in the real world in a variety of fields. 
"""


def main():
    pass


if __name__ == "__main__":
    main()
