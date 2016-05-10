"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

MAX =10**6
active = 0
n = 0
nmax = 0
xmax = 0

for x in range(500001,MAX,2):
    active = x
    n = 0

    while active != 1:
        active = (active/2) if (active % 2 == 0) else ((3 * active) + 1)
        n += 1

    if n > nmax:
        nmax = n
        xmax = x
    print(x,n)

print('result:',xmax,nmax)