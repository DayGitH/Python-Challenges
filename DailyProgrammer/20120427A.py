"""
Your challenge today is to write a program that can draw a checkered grid (like a chessboard) to any dimension. For
instance, a 3 by 8 board might look like this:

*********************************
*   *###*   *###*   *###*   *###*
*   *###*   *###*   *###*   *###*
*   *###*   *###*   *###*   *###*
*********************************
*###*   *###*   *###*   *###*   *
*###*   *###*   *###*   *###*   *
*###*   *###*   *###*   *###*   *
*********************************
*   *###*   *###*   *###*   *###*
*   *###*   *###*   *###*   *###*
*   *###*   *###*   *###*   *###*
*********************************

Yours doesn't have to look like mine, you can make it look any way you want (now that I think of it, mine looks kinda
bad, actually). Also try to make it scalable, so that if you want to make a 2 by 5 board, but with bigger squares, it
would print out:

*******************************
*     *#####*     *#####*     *
*     *#####*     *#####*     *
*     *#####*     *#####*     *
*     *#####*     *#####*     *
*     *#####*     *#####*     *
*******************************
*#####*     *#####*     *#####*
*#####*     *#####*     *#####*
*#####*     *#####*     *#####*
*#####*     *#####*     *#####*
*#####*     *#####*     *#####*
*******************************
Have fun!
"""

HEIGHT = 5
WIDTH = 5
char = [' ', '#']
div = '*'
x = 8
y = 3

c = 1
print(div * (((WIDTH-1) * x) + 1))
for i in range(y):
    for j in range(HEIGHT-2):
        print(div, end='')
        for k in range(x):
            print(char[c]*(WIDTH-2) + div, end='')
            c = (c+1) % 2
        print('')
    c = (c+1) % 2
    print(div * (((WIDTH - 1) * x) + 1))
