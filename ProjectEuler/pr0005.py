"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def LCM(n):
    num_list = []
    factor_list = []
    prime = [2,3,5,7,11,13,17,19,23,29,31,37,43,47,53,59,61,67,71,73,79,83,89,97,101]
    p = 0
    chng_flg = 0
    for i in range(2, n + 1):
        num_list.append(i)
    while True:
        print(num_list)
        chng_flg = 0
        for e in range(len(num_list)):
            if num_list[e] % prime[p] == 0:
                num_list[e] = int(num_list[e] / prime[p])
                chng_flg+= 1
        if chng_flg > 0:
            factor_list.append(prime[p])
        else:
            p += 1
            
        if p == 24:
            return factor_list
        
def list_multiply(list):
    prod = 1
    for l in list:
        prod *= l
    
    return prod
        
x = LCM(20)
print(x)
print(list_multiply(x))