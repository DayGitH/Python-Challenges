"""
The Monty Hall Problem [http://en.wikipedia.org/wiki/Monty_Hall_problem] is a probability brain teaser that has a
rather unintuitive solution.

The gist of it, taken from Wikipedia:
Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others,
goats. You pick a door, say No. 1 [but the door is not opened], and the host, who knows what's behind the doors, opens
another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your
advantage to switch your choice? (clarification: the host will always reveal a goat)

Your task is to write a function that will compare the strategies of switching and not switching over many random
position iterations. Your program should output the proportion of successful choices by each strategy. Assume that if
both unpicked doors contain goats the host will open one of those doors at random with equal probability.

If you want to, you can for simplicity's sake assume that the player picks the first door every time. The only aspect
of this scenario that needs to vary is what is behind each door.

Thanks to SleepyTurtle for posting this idea at /r/dailyprogrammer_ideas! Do you have a problem you think would be good
for us! Head on over there and post it!
"""

import numpy as np
import numpy.random as nprnd
import time

TRIALS = 1000000
doors = [1, 0, 0]

start_time = time.time()
keep = 0
switch = 0
for _ in range(TRIALS):
    """ permutes doors to create random combination of doors and then runs the keep and switch scenarios simultaneously.
    in the case of initially selecting the correct door, the choice of removing one of the other doors does not matter,
    so it just chooses the first one.
    """
    perm = nprnd.permutation(doors)
    keep += perm[0]

    zero = np.where(perm[1:] == 0)[0]
    perm = np.delete(perm, zero[0]+1)
    switch += perm[1]

print('Kept:         {}%'.format(100*keep/TRIALS))
print('Switched:     {}%'.format(100*switch/TRIALS))
print('Elapsed time: {}'.format(time.time()-start_time))

start_time = time.time()
keep = 0
switch = 0
for _ in range(TRIALS):
    """ optimization so that it doesn't actually simulate the monty hall problem. instead it is based on the realization
    that if the permutation's first door is correct, the keep scenario always wins and if the first is incorrect the
    switch scenario always wins. Time reduced to less than half of the above method.
    """
    perm = nprnd.permutation(doors)
    if perm[0]:
        keep += 1
    else:
        switch += 1

print('Kept:     {}%'.format(100*keep/TRIALS))
print('Switched: {}%'.format(100*switch/TRIALS))
print('Elapsed time: {}'.format(time.time()-start_time))
