"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

'''
Borrowed from online. Helped me shave down my script from
5 hours down to 24 seconds. This script runs in about 9
seconds.

The idea I borrowed is if the current prime's square does
not exist, I do not need to continue after that, since all
non-primes have been eradicated.

def eratosthene(N):
    L1 = [i for i in range(2,N+1)]
    i = 0
    while L1[i]**2 <= L1[-1]:
        L2 = [a for a in L1 if a%L1[i]!=0 or a<=L1[i]]
        L1 = L2 #avoid assignment issues between L1 and L2
        i+=1
    return L1

def pb10():
    return sum(eratosthene(2000000))

print(pb10())
'''

prime = []

for i in range(2,2000000):
    prime.append(i)

p = 0
p_sum = 0
t = True
while prime[p]**2 <= prime[-1]:
    p_hold = prime
    prime = []
    for j in range(len(p_hold)):
        if p_hold[j] == p_hold[p]:
            prime.append(p_hold[j])
        elif p_hold[j] % p_hold[p] == 0:
            pass
        else:
            prime.append(p_hold[j])

    p += 1

print(sum(prime))
