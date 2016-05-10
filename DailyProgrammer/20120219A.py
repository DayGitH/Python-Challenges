'''
The program should take three arguments. The first will be a day, the second will be month, and the third will be year.
Then, your program should compute the day of the week that date will fall on.
'''

import datetime

day_list = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

year = int(input('Year  >>  '))
month = int(input('Month >>  '))
day = int(input('Day   >>  '))

print(day_list[datetime.date(year, month, day).weekday()])