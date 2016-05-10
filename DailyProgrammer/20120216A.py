'''
write a program that will print the song "99 bottles of beer on the wall".
for extra credit, do not allow the program to print each loop on a new line.
'''

count = 99

while True:
    if count > 1:
        print('{} bottles of beer on the wall, {} bottles of beer. '
              'Take one down and pass it around, {} bottles of beer on the wall.'.format(count, count, count-1))
    elif count == 1:
        print('{} bottle of beer on the wall, {} bottle of beer. '
              'Take one down and pass it around, {} bottles of beer on the wall.'.format(count, count, 'no more'))
    elif count == 0:
        count = 100
        print('{} bottles of beer on the wall, {} bottles of beer. '
              'Go to the store and buy some more, '
              '{} bottles of beer on the wall.'.format('No more', 'no more', count-1))
    count -= 1