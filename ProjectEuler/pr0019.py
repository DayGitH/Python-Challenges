"""
You are given the following information, but you may prefer to do some research for yourself.

    * 1 Jan 1900 was a Monday.
    * Thirty days has September,
      April, June and November.
      All the rest have thirty-one,
      Saving February alone,
      Which has twenty-eight, rain or shine.
      And on leap years, twenty-nine.
    * A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

MONTHS = 12
m_dict = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

year = 1900
day = 1
sun_count = 0

# loop through years
while year < 2001:
    # loop through months
    for m in range(1,MONTHS+1):
        # get number of days in month from dictionary
        DAYS = m_dict[m]
        # make adjustment for leap years
        if m == 2:
            if year%400 == 0:
                DAYS += 1
            elif year%100 == 0:
                pass
            elif year%4 == 0:
                DAYS += 1
        #loop through days
        for n in range(1,DAYS+1):
            # count for first sunday of a month
            if n == 1 and day == 7 and year > 1900:
                sun_count += 1
            # day of the week count
            day = day + 1 if day < 7 else 1
    year += 1

print(sun_count)