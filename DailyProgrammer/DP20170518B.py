"""
[2017-05-18] Challenge #315 [Intermediate] Game of life that has a twist

https://www.reddit.com/r/dailyprogrammer/comments/6bumxo/20170518_challenge_315_intermediate_game_of_life/

So for the first part of the description I am borrowing /u/Elite6809 challenge of a while ago
[link](https://www.reddit.com/r/dailyprogrammer/comments/271xyp/622014_challenge_165_easy_ascii_game_of_life/)
This challenge is based on a game (the mathematical variety - not quite as fun!) called [Conway's Game of
Life](http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). This is called a cellular automaton. This means it is
based on a 'playing field' of sorts, made up of lots of little cells or spaces. For Conway's game of life, the grid is
square - but other shapes like hexagonal ones could potentially exist too. Each cell can have a value - in this case,
on or off - and for each 'iteration' or loop of the game, the value of each cell will change depending on the other
cells around it. This might sound confusing at first, but looks easier when you break it down a bit.
* A cell's "neighbours" are the 8 cells around it.
* If a cell is 'off' but exactly 3 of its neighbours are on, that cell will also turn on - like reproduction.
* If a cell is 'on' but less than two of its neighbours are on, it will die out - like underpopulation.
* If a cell is 'on' but more than three of its neighbours are on, it will die out - like overcrowding.
Fairly simple, right? This might sound boring, but it can generate fairly complex patterns - [this one, for
example](http://upload.wikimedia.org/wikipedia/commons/e/e5/Gospers_glider_gun.gif), is called the Gosper Glider Gun
and is designed in such a way that it generates little patterns that fly away from it. There are other examples of such
patterns, like ones which grow indefinitely.
We are going to extend this by giving it some additional rules:
There are two parties on the grid, say red and blue.
When a cell only has neighbours that are of his own color, nothing changes and it will folow the rules as explained
before.
When a cell has neighbours that are not of his own 1 of two things can happen:
    - The total amount of cells in his neighbourhood of his color (including himself) is greater then the amount of
cells not in his color in his neighbourhood 
        -> apply normal rules, meaning that you have to count in the cells of other colors as alive cells
    - If the amout of the other colors is greater then amount of that cell's own color then it just changes color.
Last if a cell is 'off' and has 3 neighbour cells that are alive it will be the color that is the most represented. 
Your challenge is, given a width and heigth to create a grid and a number of turns to simulate this variant
# Formal Inputs and Outputs
## Input Description
You will be given three numbers **W** and **H** and **N**. These will present the width and heigth of the grid. With
this you can create a grid where on the grid, a period or full-stop `.` will represent 'off', and a hash sign `#`/`*`
will represent 'on' (for each color). 
These states you can generate at random.
The grid that you are using must 'wrap around'. That means, if something goes off the bottom of the playing field, then
it will wrap around to the top, like this: http://upload.wikimedia.org/wikipedia/en/d/d1/Long_gun.gif See how those
cells act like the top and bottom, and the left and right of the field are joined up? In other words, the neighbours of
a cell can look like this - where the lines coming out are the neighbours:
    #-...-  ......  ../|\.
    |\.../  ......  ......
    ......  |/...\  ......
    ......  #-...-  ......
    ......  |\.../  ..\|/.
    |/...\  ......  ..-#-.
    
## Output Description
Using that starting state, simulate **N** iterations of Conway's Game of Life. Print the final state in the same format
as above - `.` is off and `#` is on.
# Sample Inputs & Output
## Sample Input
    10 10 7
    
# Challenge
## Challenge Input
    32 17 17
    
    50 50 21
## note
For the initial state I would give it a 45% procent chance of being alive with dividing the red and blue ones to be
50/50
Also look what happens if you change up these numbers
"""


def main():
    pass


if __name__ == "__main__":
    main()
