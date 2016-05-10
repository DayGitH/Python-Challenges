"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

prime = []

for i in range(2,1000000):
    prime.append(i)
    
p = 0

for i in range(10001):
    p_hold = prime
    prime = []    
    for j in range(len(p_hold)):
        if p_hold[j] == p_hold[p]:
            prime.append(p_hold[j])
        elif p_hold[j] % p_hold[p] == 0:
            pass
        else:
            prime.append(p_hold[j])
     
    print(p_hold[p])
    p += 1
           
x=1
x=2