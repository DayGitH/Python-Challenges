"""
Happy St. Patrick's Day! Write a program that accepts a year as input and outputs what day St. Patrick's Day falls on.
Bonus: Print out the number of times St. Patrick's Day falls on a Saturday for this century.
Sample Run:
Enter Year: 2012
St. Patrick's Day is on a Saturday.
Enter Year: 2010
St. Patrick's Day is on a Wednesday.
"""

import datetime

days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}


def pattys(year):
    return days[datetime.date(year, 3, 17).weekday()]

if __name__ == '__main__':
    while True:
        inp = int(input('Enter Year: '))
        print('St. Patrick\'s Day is on a {}\n'.format(pattys(inp)))
