"""
[2016-09-30] Challenge #285 [Hard] Math Proofs

https://www.reddit.com/r/dailyprogrammer/comments/557wyy/20160930_challenge_285_hard_math_proofs/

# Description
Determine if a mathematical expression is logically equivalent
		
# Part 1
Determine if a mathematical expression is logically equivalent
Our first program will only support 4 basic operators; `+`,`-`,`*`,`/`.
Examples of logically equivalent expressions:
    x + x = 2x
    2*x = 2x
    2(x + y) = 2x + 2y
    a + b = b + a
    x - x = 0
    y/2 = (1/2)*y
    -(-x) = x
		
Examples of *not* logically equivalent expressions:
    2 = 3
    a - b - c = a - (b - c)
    x + y = a + b
# Part 2
Support more advanced operators such as `^`,`log`, derivatives, bit shifts, booleans, or whatever you can come up with.
 This part is more open, so feel free to show off your additions.
Examples of extensions:
    x^2 * x^3 = x^5
    (x + 2)^(y + 2) = 4x(2 + x)^y + 4(2 + x)^y + (2 + x)^y * x^2
    !(a && b) = !a || !b
    x << 1 << 2 = x << 3
    
		
# Part 3
Your solution should create a proof of the steps your program took to show the expression was valid or invalid.
Statements|Reasons
:--|:--
2(x + y) + 0 = 2x + 2y | 1. Given
2x + 2y + 0 = 2x + 2y | 2. Distributive Property of Multiplication
2x + 2y = 2x + 2y | 3. Identity Property of Addition
Statements|Reasons
:--|:--
x + y = a + b|1. Given
3 = 7|2. Contradiction for x=1, y=2, a=3, b=4
# Notes
I'm inclined to treat undefined expressions as not equivalent to anything.  Such as divide by zero:
    x/0 = x/0
# thanks
Thanks to u/wizao for submitting this idea through r/dailyprogrammer_ideas 
"""


def main():
    pass


if __name__ == "__main__":
    main()
