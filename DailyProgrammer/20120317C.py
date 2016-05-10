"""
Write a program that will perform date/time addition. Input can be interactive using standard input or command line. 3
parameters are required: a whole number, a unit of time using the following values: year, month, week, day, hour,
minute, second, and a date and time (you choose the date format). The result will be the new date and time.

Example (using ISO 8601 date/time format without time zone designator):
Enter a date and time (YYYY-MM-DDThh:mm:ss): 2012-03-17T09:00:00
Enter value to add: 10
Enter unit of time (year, month, week, day, hour, minute, second): minute
New date and time is 2012-03-17T09:10:00

Enter a date and time (YYYY-MM-DDThh:mm:ss): 2012-11-29T15:00:00
Enter value to add: 5
Enter unit of time (year, month, week, day, hour, minute, second): day
New date and time is 2012-12-04T15:00:00

Enter a date and time (YYYY-MM-DDThh:mm:ss): 2012-06-01T09:00:00
Enter value to add: -2
Enter unit of time (year, month, week, day, hour, minute, second): week
New date and time is 2012-05-18T09:00:00
"""

import sys
import datetime
from dateutil.relativedelta import relativedelta

while True:
    inp = input('Enter a date and time (YYYY:MM:DDThh:mm:ss): ')
    offset = int(input('Enter a value to add: '))
    unit = input('Enter a unit of time (years, months, weeks, days, hours, minutes, seconds): ')

    try:
        date = datetime.datetime.strptime(inp, '%Y-%m-%dT%H:%M:%S')
        exec('new_date = date + relativedelta({}=offset)'.format(unit))
        print('New date and time is {}\n'.format(new_date.isoformat()))
    except:
        print(sys.exc_info())