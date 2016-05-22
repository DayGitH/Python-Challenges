"""
If you list all positive integers less than or equal to 20, you get this:
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

If you count the number of times the digit "1" appears in that list, you get 12. Define a function f(n) which gives the
number of 1's needed to write out all numbers 1 to n in decimal notation.

Here is a couple of example values for f(n):
f(20) = 12
f(1234) = 689
f(5123) = 2557
f(70000) = 38000
f(123321) = 93395
f( 3^35 ) = 90051450678399649

By the way, all numbers in this problem, inputs and outputs alike, fit into 64-bit integers.
Can you implement f(n) in a way that is faster than just listing the values less than n and counting the instances of 1?
What is f( 5^20 )?

Bonus: A curious thing happens when you try and calculate f(35199981). You get 35199981, the same number you put in.
You can prove that the number of times f(n) is equal to n is finite. What is the sum of all n such that f(n) == n?

Since this problem is harder than most problems here, I'll give you two hints for solving it.

Hint for calculating f(n):
The numbers f(10^n - 1) (i.e. f(9), f(99), f(999), f(9999), ....) all follow a very regular pattern that is
trivial to evaluate. If you figure out this pattern (it's not very complicated), you should
be able to figure out what (for instance) f(99999) is instantaneously.
Once you have f(99999), what is f(100000)? What is f(200000)? What is f(299999)?

Hint for the bonus:
There are 83 such numbers, and they are all less than 10^11

Good luck!
Thanks to Rinfiyks for posting this problem in /r/dailyprogrammer_ideas! Do you have a problem you think would be good
for us? Head over there and post it!
"""

def f(n):
    # # s = ' '.join([str(i) for i in range(1, n+1)])
    sum1 = 0
    for i in range(1, n+1):
        sum1 += str(i).count('1')
    print(sum1)

    l = len(str(n))
    sum2 = 0
    if str(n) == '9' * l:
        # return l * (10 ** (l - 1))
        sum2 = l * (10 ** (l - 1))
    else:
        l -= 1
        sum2 = l * (10 ** (l - 1))

        for j in range(int('9'*l),n+1):
            sum2 += str(j).count('1')
    print(sum2)
    # while True:
    #     op =  n - (l * (10 ** (l-1)))
    #     if op > 0:
    #         n = op
    #         break
    # return l, s.count('1')
    # return sum1, sum2
    n = str(n)
    l = len(n) - 1
    res = 0
    prev = False
    for e, i in enumerate(n):
        bin = int(l * (10 ** (l - 1)))
        res += (int(i)) * bin
        if int(i) > 1:
            res += 10 ** l
        if prev:
            res += (int(i)) * (10 ** l) + (1*int(i))
        if int(i) == 1:
            prev = True
        else:
            prev = False
        l -= 1
    else:
        if int(i) == 1:
            res += 1
    return res


num = f(199)

print(num)
# print(5**20)