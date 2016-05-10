'''
Find the number of the year for the given date. For example, january 1st would be 1, and december 31st is 365.
for extra credit, allow it to calculate leap years, as well.
'''

month_len = {1: 31, 2: 28, 3: 31, 4: 30, 5:31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

month = int(input('Enter month: '))
day = int(input('Enter day: '))
leap = input('Leap (Y/N)? ').lower() in ['y']

sum_days = sum([month_len[n] for n in range(1,month)]) + day

print('days:', sum_days)