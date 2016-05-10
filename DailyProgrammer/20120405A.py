"""
1000 Lockers Problem.
In an imaginary high school there exist 1000 lockers labelled 1, 2, ..., 1000. All of them are closed. 1000 students
are to "toggle" a locker's state. * The first student toggles all of them * The second one toggles every other one
(i.e, 2, 4, 6, ...) * The third one toggles the multiples of 3 (3, 6, 9, ...) and so on until all students have
finished.

To toggle means to close the locker if it is open, and to open it if it's closed.
How many and which lockers are open in the end?
Thanks to ladaghini for submitting this challenge to /r/dailyprogrammer_ideas!
"""

import math

N = 1000
working_list = [False] * N

for i in range(1,1000+1):
    for n, j in enumerate(working_list):
        if n%i == 0:
            working_list[n] = not working_list[n]

for n, j in enumerate(working_list):
    if j:
        print(n)
print(working_list.count(True))

"""
/u/prophile's solution

requires dev to already know that the solution is all squares between 0 and N
"""
opens = [n*n for n in range(int(math.sqrt(N)) + 1) if n*n < N]
print(len(opens), opens)
