"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
from time import time
def divisor(n):
    l = []
    for i in range(1,n):
        if n%i == 0:
            l.append(i)

    return l

def abundant(n):
    l = []
    for i in range(2,n):
        if sum(divisor(i)) > i:
            l.append(i)

    return l

startTime = time()

LIMIT = 28124

print('building abundant numbers list')
ab = abundant(LIMIT)
print('done')
# print(ab)

print('numbers list')
final_list = [i for i in range(1,LIMIT+1)]
check_list = [True] * LIMIT
for i in range(48,len(check_list),2):
    check_list[i] = False
print('done')

# print(final_list)

# for i in range(len(ab)//2): #should only be first half
#     for j in range(i,len(ab)): #should start at i
#         check = ab[i] + ab[j]
#         if check > LIMIT:
#             # print('break')
#             break
#         elif check in final_list:
#             # print(ab[i],'+',ab[j],'=',check)
#             final_list[final_list.index(check)] = -1
#             final_list.remove(check)

print('starting list')
for a in range(ab[0]*2,LIMIT):
    if check_list[a]:
        for b in ab:
            if (a-b) <= 0:
                break
            elif (a-b) in ab:
                # print(a,'-',b,'=',a-b)
                check_list[a:LIMIT:a] = [False] * len(range(a,LIMIT,a))


answer = []
for x in range(len(final_list)):
    if check_list[x]:
        answer.append(x)
print(sum(answer))
print(time() - startTime)