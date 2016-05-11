"""
I wouldn't call this exactly a difficult question .. but it is a fun one :)
You are all familiar with the game snake and ladders [http://en.wikipedia.org/wiki/Snakes_and_Ladders]
This is the Board [http://imgur.com/6DyXQ] you are to refer.

Your task is to write programs that will answer the following questions
First, what is the minimum number of rolls required to reach space 100.
Second, for a single player, what is the average number of rolls required to reach space 100.
And third, for k players, what is the average number of rolls until one of the players reaches space 100 and wins the
game.

Note: Space 100 must be reached by exact roll of the die; if the roll of the die would take the token past space 100,
the token remains where it is and play passes to the next player. The winner of the game is the first token to reach
space 100.

These are some of the questions from the paper "How Long Is a Game of Snakes and Ladders?" by S. C. Althoen, L. King
and K. Schilling
source: programmingpraxis.com
"""

from random import randint
from numpy import mean
from PIL import Image, ImageFont, ImageDraw

portal = { 1:  38,
           4:  14,
           9:  31,
          16:   6,
          21:  42,
          28:  84,
          36:  44,
          47:  26,
          49:  11,
          51:  67,
          56:  53,
          62:  19,
          64:  60,
          71:  91,
          80: 100,
          87:  24,
          93:  73,
          95:  75,
          98:  78
         }


def play(player):
    m = randint(1, 6)
    sum = players[player] + m
    if sum <= 100:
        players[player] = sum
    if players[player] in portal.keys():
        players[player] = portal[players[player]]


probs = {i: 0 for i in range(1, 101)}
num = 5
trials = 10000

winner = []
for t in range(trials):
    players = {i: 0 for i in range(num)}
    roll = 0
    win = False
    while not win:
        roll += 1
        for p in players:
            if players[p] < 100:
                play(p)
            else:
                win = True
                if not winner:
                    winner = [roll]
                else:
                    winner.append(roll)
            probs[players[p]] += 1

print(mean(winner))
print(probs)

max = 0
for b in probs:
    if probs[b] > max:
        max = probs[b]

for b in probs:
    probs[b] = int((probs[b]/max) * 255)

print(max)

im = Image.new('RGB', (1000,1000), (0,0,0))
dr = ImageDraw.Draw(im)

x = 0
y = 1000
plus = True
for i in range(1,101):
    dr.rectangle(((x, y), (x+100, y-100)), fill=(int(1*probs[i]),int(0.5*probs[i]),int(1*probs[i])), outline="black")
    if x == 900 and plus:
        y -= 100
        plus = False
    elif x == 0 and not plus:
        y -= 100
        plus = True
    elif plus:
        x += 100
    else:
        x -= 100

im.save("board.png")
