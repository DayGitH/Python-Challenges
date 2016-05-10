"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10
are given:

1/2	 = 	0.5
1/3	 = 	0.(3)
1/4	 = 	0.25
1/5  = 	0.2
1/6	 = 	0.1(6)
1/7  = 	0.(142857)
1/8	 = 	0.125
1/9	 = 	0.(1)
1/10 =	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring
cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""

import re
from decimal import *

MAX_LENGTH = 10000
getcontext().prec = MAX_LENGTH
getcontext().rounding = ROUND_DOWN

d_max = 0
drec_max = 0

D = 1000

for d in range(2,D+1):
    div = 1 / Decimal(d)
    check = "{0:.2000f}".format(div)[2:]
    seq = re.findall(r'^(.*?)((.*?)\3+)$',check)
    non_rep = seq[0][0]
    rep = seq[0][-1]
    t = True
    print("0.{}({})".format(non_rep,rep))
    while t:
        if non_rep and (non_rep[-1] == rep[-1]):
            non_rep = non_rep[:-1]
            rep = rep[-1] + rep[:-1]
        else:
            t = False

    print("1/{}".format(d))
    print(len(non_rep),len(rep))
    print("0.{}({})\n".format(non_rep,rep))

    if len(rep) > drec_max:
        drec_max = len(rep)
        d_max = d

    # if seq[0][0][-1] == seq[0][-1][-1]:


print(d_max,drec_max)
