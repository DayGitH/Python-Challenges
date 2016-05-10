'''
You're challenge for today is to create a program that can calculate pi accurately to at least 30 decimal places.
Try not to cheat :)

3.141592653589793238462643383279
'''

# sum = 0
#
# for i in range(1,100000000):
#     sum += 4 * (((-1) ** (i + 1))/((2 * i)- 1))
#     print(i,'100000000')
#
# print('3.141592653589793238462643383279')
# print(sum)

from decimal import getcontext,Decimal

sum1 = 0
sum2 = 0

getcontext().prec = 40

for n in range(100):
    sum1 += ((-1) ** n) * (((Decimal(1) / Decimal(5)) ** ((2 * n)+ 1))/((2 * n)+ 1))
    sum2 += ((-1) ** n) * (((Decimal(1) / Decimal(239)) ** ((2 * n)+ 1))/((2 * n)+ 1))

answer = 4 * ((4 * sum1) - sum2)
print('3.141592653589793238462643383279')
print(answer)