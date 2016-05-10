'''
create a program that will take user input and tell them their age in months, days, hours, and minutes

sample output:

how old are you? 18

months : 216, days : 6480, hours : 155520, and minutes : 388800
'''

inp = int(input('How old are you? '))

print('  Years: {}'.format(int(inp)))
print(' Months: {}'.format(int(inp * 12)))
print('  Weeks: {}'.format(int(inp * 52.14)))
print('   Days: {}'.format(int(inp * 365)))
print('  Hours: {}'.format(int(inp * 8760)))
print('Minutes: {}'.format(int(inp * 525600)))
print('Seconds: {}'.format(int(inp * 31536000)))