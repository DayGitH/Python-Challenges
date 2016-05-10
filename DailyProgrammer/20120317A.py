"""
Write a program that accepts a year as input and outputs the century the year belongs in (e.g. 18th century's year
ranges are 1701 to 1800) and whether or not the year is a leap year. Pseudocode for leap year can be found
here[https://en.wikipedia.org/wiki/Leap_year#Algorithm].

Sample run:
Enter Year: 1996
Century: 20
Leap Year: Yes

Enter Year: 1900
Century: 19
Leap Year: No
"""


def leap(year):
    if not year % 4 == 0:
        return False
    elif not year % 100 == 0:
        return True
    elif not year % 400 == 0:
        return False
    else:
        return True


def century(year):
    if year % 100:
        return (year // 100) + 1
    else:
        return year // 100

if __name__ == '__main__':
    while True:
        inp = int(input('Enter Year: '))

        print('Century: {}'.format(century(inp)))

        print('Leap Year: {}\n'.format(leap(inp)))
