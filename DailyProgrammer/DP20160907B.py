"""
[2016-09-07] Challenge #282 [Intermediate] The final Quixo move

https://www.reddit.com/r/dailyprogrammer/comments/51l1j1/20160907_challenge_282_intermediate_the_final/

#Description
[Quixo](https://boardgamegeek.com/boardgame/3190/quixo) is a grid based game. The game is played by 2 groups, one being
`x` and other being `o`.
The goal of the game is to get 5 blocks in a row.
The blocks can only be taken from the sides and must be placed in a line, pushing all the other blocks.
from [boardgamegeek](https://boardgamegeek.com/boardgame/3190/quixo):
> On a turn, the active player takes a cube that is blank or bearing his symbol from the outer ring of the grid,
rotates it so that it shows his symbol (if needed), then adds it to the grid by pushing it into one of the rows from
which it was removed. Thus, a few pieces of the grid change places each turn, and the cubes slowly go from blank to
crosses and circles. Play continues until someone forms an orthogonal or diagonal line of five cubes bearing his
symbol, with this person winning the game.
If the block comes from a corner, you have 2 options
Start:
  | A | B | C | D | E 
---|---|----|----|----|----
1 | **x** | _ | _ | _ | o
2 | _ | _ | _ | _ | _
3 | _ | _ | _ | _ | _
4 | x | _ | _ | _ | o
5 | _ | _ | _ | _ | _
Option 1:
  | A | B | C | D | E 
---|---|----|----|----|----
1 | _ | _ | _ | o | **x**
2 | _ | _ | _ | _ | _
3 | _ | _ | _ | _ | _
4 | x | _ | _ | _ | o
5 | _ | _ | _ | _ | _
Option 2:
  | A | B | C | D | E 
---|---|----|----|----|----
1 | _ | _ | _ | _ | o
2 | _ | _ | _ | _ | _
3 | x | _ | _ | _ | _
4 | _ | _ | _ | _ | o
5 | **x** | _ | _ | _ | _
If the block is from the middle of the row, you have 3 options
Start:
  | A | B | C | D | E 
---|---|----|----|----|----
1 | x | _ | _ | _ | o
2 | _ | _ | _ | _ | _
3 | _ | _ | _ | _ | _
4 | **x** | _ | _ | _ | o
5 | _ | _ | _ | _ | _
Option 1:
  | A | B | C | D | E 
---|---|----|----|----|----
1 | x | _ | _ | _ | o
2 | _ | _ | _ | _ | _
3 | _ | _ | _ | _ | _
4 | _ | _ | _ | _ | o
5 | **x** | _ | _ | _ | _
Option 2:
  | A | B | C | D | E 
---|---|----|----|----|----
1 | **x** | _ | _ | _ | o
2 | x | _ | _ | _ | _
3 | _ | _ | _ | _ | _
4 | _ | _ | _ | _ | o
5 | _ | _ | _ | _ | _
Option 3:
  | A | B | C | D | E 
---|---|----|----|----|----
1 | x | _ | _ | _ | o
2 | _ | _ | _ | _ | _
3 | _ | _ | _ | _ | _
4 | _ | _ | _ | o | **x**
5 | _ | _ | _ | _ | _
You can only move your own blocks or blanco block directly. If you use a blanco block, then that block becomes yours.
For those who can't make up the rules by reading this, you can watch [this 2 min instruction
video](https://www.youtube.com/watch?v=cZT5N6hIFYM).
If your move causes the other players block to line up as well as yours, then it's called a `draw`
#Challenge
You will be given a 5 by 5 grid with a game on that is almost finished, you only need to make the winning move.
You are always the player with `x`
##Input
The grid with the current game
    x_xxx
    _xo_o
    o_ooo
    oxox_
    oooo_
## Output
The move that will make you have won the game
    B1 -> B5
Here you have me doing this with the actual game
 - [step 1](http://imgur.com/NywAMsM)
 - [step 2](http://imgur.com/tb4sFIU)
 - [step 3](http://imgur.com/zldLzcN)
##Challenge input 1
    x_xxx
    _xo_o
    o_ooo
    oxooo
    ooxx_
##Challenge output 1
    B1 -> A1
##Inputs from /u/zandekar
no winning moves
    
    xxxox
    __ooo
    oooxo
    xxxoo
    xxooo
more than one winning move
    
    xxxox
    xxxxo
    ___ox
    oooxo
    xxx_o
a draw
    oooxx
    xxx_x
    oooxo
    xoxox
    xoxox
#Note
Sometimes there is more then 1 correct answer, giving just one is fine.
#Bonus
Give all possible answers to win.
##Input 1
    x_xxx
    _xo_o
    o_ooo
    oxox_
    oooo_
##Output 1
    B1 -> B5
    B1 -> A1
    B1 -> E1
#Finally
Have a good challenge idea?
Consider submitting it to /r/dailyprogrammer_ideas
#Edits
Some additional challenges and info from /u/zandekar
"""


def main():
    pass


if __name__ == "__main__":
    main()
