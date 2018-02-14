"""
[2017-09-15] Challenge #331 [Hard] Interactive Interpreter

https://www.reddit.com/r/dailyprogrammer/comments/7096nu/20170915_challenge_331_hard_interactive/

#Description
Make an interactive interpreter with 2 different capabilities
1. It should be able to take a mathematical string (fx "5 + 2") and return the result of it
2. It should be capable of assigning variables (fx "x = 5 + 2") store the value for the variable for later use and
return the value
3. Using assigned variables instead of numbers (fx "y = x * 2")
Variable names must start with a character a-z and can be continued by any alphanumeric character.
All variables will be numerical (can be either floats or integers), feel free to support arbitrarily large numbers.
The mathematical evaluator shall be capable of adding, subtracting, multiplying, dividing, exponents and handling
nested parenthesis.
exponents will be using ^ as symbol.
The usual order of mathematics apply, so PEMDAS shall be applied in evaluations.
**PLEASE** refrain from using your languages built in evaluators.
#Input description
A list of strings such as (divided by \n):
    5 + 5
    (2 * 5 + 1) / 10
    x =  1 / 2
    y = x * 2
Assume all inputs to be written properly, i.e. no undefined variables or wrong placed parenthesis
Assume all whitespace as negligible so "1 2" and "12" can be assumed the same
#Output description
Output for each input line, fx from above would be:
    10
    1.1
    0.5
    1
#Challenge input
    9 + 10
    (2 * 5 + 1) / 10
    x =  1 / 2
    y = x * 2
    (x + 2) * (y * (5 - 100))
    z = 5*-3.14
    2.6^(2 + 3/2) * (2-z)
#Challenge output
    19
    1.1
    0.5
    1
    -237.5
    -15.7
    501.625937332
#Bonus
##Bonus 1 - Functions
Variables are nice, but it's all quite limited until we got functions
functions doesnt eval on declaration, so just make a newline as output from a funtion declaration
functions and variables can exist with the same name.
functions either look like 'func()' or 'func(arg1, arg2, arg3)' with any number of arguments needed
arguments given for functions are only used within the function themself and overwrites any variable with the given
name.
    a = 2
    func(a) = a
    func(1) will return 1
    func(1) + a will return 3
if the function requires no arguments
###Bonus input
    a = 10
    a() = 2
    a() + a
    avg(a, b) = (a + b) / 2
    x = avg(69, 96)
    avg(x, avg(a(), a)) + a
###Bonus output
    10
    
    12
    
    82.5
    54.25
##Bonus 2 - Errors
Handle errors 'gracefully'
Errors include but are likely not limited to:
1. Undefined variables (fx "pi * 2", pi has never been defined)
2. Wrong variable naming
3. parenthesis placed wrongly (too many open, too many closing, closing when none open etc)
4. dividing by 0
5. Functions calling itself or calling functions that end up calling itself
Return error description as output if an error occurred
#Extra
If you have any challenges, please share it at /r/dailyprogrammer_ideas!
"""


def main():
    pass


if __name__ == "__main__":
    main()
