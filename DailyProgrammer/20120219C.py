'''
Create a program which prints out a table with the month's calendar in it, when the month and year is given as input.
Extra points for highlighting the current day and providing links to next and previous months.
Happy coding :)
'''

import datetime
import calendar

month_dict = {11: ['January', 31], 12: ['February', 'leap'], 1: ['March', 31], 2: ['April', 30], 3: ['May', 31],
              4: ['June', 30], 5: ['July', 31], 6: ['August', 31], 7: ['September', 30], 8: ['October', 31],
              9: ['November', 30], 10: ['December', 31]}
day_dict = {0: ' S', 1: ' M', 2: ' T', 3: ' W', 4: ' T', 5: ' F', 6: ' S'}

current_date = str(datetime.date.today()).split('-')

run = True


# For implementing march = 1 to february = 12
m = (int(current_date[1]) + 9) % 12 + 1
# January and february are considered part of the previous year
Y = int(current_date[0]) if m <= 10 else int(current_date[0]) - 1

y = int(str(Y)[2:4])
c = int(str(Y)[0:2])

while run:
    # casting to int since all variables need to be rounded down
    w_first = (1 + int((2.6 * m) - 0.2) + y + int(y / 4) + int(c / 4) - (2 * c)) % 7

    date = '  '
    # rows
    print(Y, month_dict[m][0])
    for a in range(7):
        # columns
        for b in range(13):
            if isinstance(date, int):
                max_date = month_dict[m][1] if m != 12 else 29 if calendar.isleap(int(current_date[0])) else 28
                if date >= max_date:
                    break
            if (b % 2) == 1:
                print(' ', end='')
            else:
                if a == 0:
                    print(day_dict[b // 2], end='')
                else:
                    if not isinstance(date, int) and (b // 2) == w_first:
                        date = 0
                    if isinstance(date, int):
                        date += 1
                        print('{:02d}'.format(date), end='')
                    else:
                        print(date, end='')

        print('')

    while True:
        print('(N)ext, (P)revious, (D)efine, or (S)top?')
        user_inp = input('> ')
        if user_inp.lower() == 'n':
            if m + 1 > 12:
                m = 1
                Y += 1
                y = int(str(Y)[2:4])
                c = int(str(Y)[0:2])
            else:
                m += 1
            break
        elif user_inp.lower() == 'p':
            if m - 1 < 1:
                m = 12
                Y -= 1
                y = int(str(Y)[2:4])
                c = int(str(Y)[0:2])
            else:
                m -= 1
            break
        elif user_inp.lower() == 'd':
            month = 0
            while True:
                print('Enter a year between 0 and 9999')
                year = int(input('> '))
                if 0 <= year <= 9999:
                    break
                print('invalid')
            while True:
                print('Enter month')
                month = int(input('> '))
                if 1 <= month <= 12:
                    break
                print('invalid')
            # For implementing march = 1 to february = 12
            m = (month + 9) % 12 + 1
            # January and february are considered part of the previous year
            Y = year if m <= 10 else year - 1

            y = int(str(Y)[2:4])
            c = int(str(Y)[0:2])
            break
        elif user_inp.lower() == 's':
            print('Stopping')
            run = False
            break
        else:
            print('invalid input')
