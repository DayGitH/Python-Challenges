"""
Make a function that generates an array of 1,000 2-dimensional points, where both the x-coordinate and the y-coordinate
are between 0.0 and 1.0. So (0.735, 0.167) and (0.456, 0.054) would be examples. (Most computer languages have a simple
random function that returns a double precision floating point number in this range, so you can use that to generate
the coordinates. Python has random.random(), Java has Math.random(), Perl has rand(), etc. )

Create a program that finds the two points in this array that are closest to each other, and print that distance. As a
reminder, the distance between the two points (x1, y1) and (x2, y2) is sqrt( (x1 - x2)2 + (y1 - y2)2 ).

Bonus 1: Do the same thing, but instead of using 1,000 points, use 1,000,000 points and see if you can create an
algorithm that runs in a reasonable amount of time [edit: something like one minute or less].

Bonus 2: Do the same thing but for 3-dimensional points.

thanks to oskar_s for today's challenge at /r/dailyprogrammer_ideas ...
LINK [http://www.reddit.com/r/dailyprogrammer_ideas/comments/rjdi1/difficult_find_the_closest_pair_of_points/]
"""

import cProfile
import numpy.random as nprnd
import numpy as np
import sys


def div_and_conq(working_list):
    l1 = []
    l2 = []
    working_list = working_list[working_list[:, 0].argsort()]
    length = len(working_list)
    list_l, list_r = working_list[:int(length/2)], working_list[int(length/2):]
    if length > 3:
        d_l_min, pll1, pll2 = div_and_conq(list_l)
        d_r_min, prl1, prl2 = div_and_conq(list_r)
        min_dist = min(d_l_min, d_r_min)
        if min_dist == d_l_min:
            l1, l2 = pll1, pll2
        elif min_dist == d_r_min:
            l1, l2 = prl1, prl2
        mid = list_l[-1][0]
        rem = working_list[((mid+min_dist)>working_list[:,0]) & (working_list[:,0]>(mid-min_dist))]
        for a in rem:
            for b in rem:
                if a[0] != b[0] or a[1] != b[1]:
                    d = dist(np.concatenate(([a],[b])))
                    if d < min_dist:
                        min_dist = d
                        l1, l2 = a, b
        return min_dist, l1, l2
    elif length == 3:
        one = dist(working_list[:2])
        two = dist(working_list[1:])
        three = dist(np.concatenate(([working_list[0]], [working_list[2]])))
        min_dist = min(one, two, three)
        if min_dist == one:
            return one, working_list[0], working_list[1]
        elif min_dist == two:
            return two, working_list[1], working_list[2]
        elif min_dist == three:
            return two, working_list[0], working_list[2]
        else:
            print('something went wrong in length==3')
    elif length == 2:
        return dist(working_list), working_list[0], working_list[1]


def dist(working_list):
    length = len(working_list)
    if length == 2:
        add = 0
        for i in working_list.T:
            add += (i[0]-i[1]) ** 2
        return add
    else:
        print(working_list)
        print('error in dist(working_list)')


l = nprnd.random([1000000, 2])
l = l[l[:, 0].argsort()]
length = len(l)

r, l1, l2 = div_and_conq(l)
print(r, l1, l2)

from random import random
from math import *

npoints = 1000000

ps = [(random(), random()) for _ in range(npoints)]
ps.sort()
mind, mind2 = 10, 100
for i, (x0, y0) in enumerate(ps):
    for j in range(i+1,npoints):
        x1, y1 = ps[j]
        if x1 > x0 + mind: break
        d2 = (x0 - x1) ** 2 + (y0 - y1) ** 2
        if d2 < mind2:
            mind2 = d2
            mind = sqrt(d2)
print(mind)