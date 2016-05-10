'''
Create a program that will factor a number. for example:
12 = 2 * 2 * 3
14 = 7 * 2
20 = 2 * 2 * 5
thanks to bears_in_bowlers for todays challenge!
'''

import math

num = int(input('Enter number: '))
active_num = num

factors = []
n = 2
while active_num != 1:
    if active_num % n == 0:
        active_num /= n
        factors.append(str(n))
    else:
        n += 1

if len(factors) == 0:
    factors = [str(num)]

print(num, '=', ' * '.join(factors))
