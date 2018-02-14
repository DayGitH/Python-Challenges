"""
[2016-09-09] Challenge #282 [Hard] Hidato

https://www.reddit.com/r/dailyprogrammer/comments/51wg0j/20160909_challenge_282_hard_hidato/

#Description
From [wikipedia](https://en.wikipedia.org/wiki/Hidato)
> Hidato (Hebrew: חידאתו‎‎, originating from the Hebrew word Hida = Riddle) is a logic puzzle game invented by Dr.
Gyora M. Benedek, an Israeli mathematician. The goal of Hidato is to fill the grid with consecutive numbers that
connect horizontally, vertically, or diagonally. Numbrix puzzles, created by Marilyn vos Savant, are similar to Hidato
except that diagonal moves are not allowed. Jadium puzzles (formerly Snakepit puzzles), created by Jeff Marchant, are a
more difficult version of Numbrix with fewer given numbers and have appeared on the Parade magazine web site regularly
since 2014. The name Hidato is a registered trademark of Doo-Bee Toys and Games LTD, a company co-founded by Benebek
himself. Some publishers use different names for this puzzle such as Number Snake.
Further info:
> In Hidato, a grid of cells is given. It is usually square-shaped, like Sudoku or Kakuro, but it can also include
irregular shaped grids like hearts, skulls, and so forth. It can have inner holes (like a disc), but it has to be made
of only one piece.
The goal is to fill the grid with a series of consecutive numbers adjacent to each other vertically, horizontally, or
diagonally.
In every Hidato puzzle the smallest and the highest numbers are given on the grid. There are also other given numbers
on the grid (with values between the smallest and the highest) to help direct the player how to start the solution and
to ensure that Hidato has a single solution.
Note: the above condition on the smallest or highest numbers are sometimes relaxed: only their values can be given,
without their positions on the grid (of course, the difference between these values must be equal to the number of
cells in the grid minus one). This may lead to harder puzzles.
Every well-formed Hidato puzzle is supposed to have a unique solution. Moreover, a Hidato puzzle intended for human
solvers should have a solution that can be found by (more or less) simple logic. However, there exist very hard Hidato
puzzles, even of small size.
Hidato puzzles are published in newspapers such as the Daily Mail and Detroit Free Press.
So basically:
You'll recieve a grid with numbers, empty spaces and blocked spaces.
You need to fill in all empty spaces with numbers. These numbers must be consecutive that connect in any direction.
#Formal Inputs & Outputs
##Input description
A Hidato puzzle to solve.
###Input 1
    . 33 35 . . x x x
    . . 24 22 . x x x
    . . . 21 . . x x
    . 26 . 13 40 11 x x
    27 . . . 9 . 1 x
    x x . . 18 . . x
    x x x x . 7 . .
    x x x x x x 5 .
###Input 2
    . . 3 . . . . .
    x x x x x x x .
    . . . . . . . .
    . x x x x x x x
    . . . . . . . .
    x x x x x x x .
    . . . . . . . .
    . x x x x x x x
    . . . . . . . .
###Input 3
    1 .
###Input 4
    1 .
    x .
    5 .
###Input 5
    . 4 5 16
    8 6 . .
    . 12 . 14
    10 . 13 1
###Input 6
    1 . . 23 . .
    11 . 3 . . 18
    . 13 . . . .
    . . . . 26 .
    8 . . 15 . 30
    . . 36 . . 31
##Output description
A solved Hidato
###Output 1
    32 33 35 36 37 x x x
    31 34 24 22 38 x x x
    30 25 23 21 12 39 x x
    29 26 20 13 40 11 x x
    27 28 14 19 9 10 1 x
    x x 15 16 18 8 2 x
    x x x x 17 7 6 3
    x x x x x x 5 4
###Output 2
    1 2 3 4 5 6 7 8
    x x x x x x x 9
    17 16 15 14 13 12 11 10
    18 x x x x x x x
    19 20 21 22 23 24 25 26
    x x x x x x x 27
    35 34 33 32 31 30 29 28
    36 x x x x x x x
    37 38 39 40 41 42 43 44
###Output 3
    1 2
###Output 4
    1 2
    x 3
    5 4
###Output 5
    7 4 5 16
    8 6 3 15
    9 12 2 14
    10 11 13 1
###Output 6
    1 2 22 23 20 19
    11 12 3 21 24 18
    10 13 4 25 17 27
    9 5 14 16 26 28
    8 6 34 15 29 30
    7 35 36 33 32 31
#Notes/Hints
Also from [wikipedia](https://en.wikipedia.org/wiki/Hidato)
> As in many logic puzzles, the basic resolution technique consists of analyzing the possibilities for each number of
being present in each cell. When a cell can contain only one number (Naked Single) or when a number has only one
possible place (Hidden Single), it can be asserted as belonging to the solution.
> One key to the solution is, it does not have to be built in ascending (or descending) order; it can be built
piecewise, with pieces starting from different givens.
> As in the Sudoku case, the resolution of harder Hidato or Numbrix puzzles requires the use of more complex techniques
- in particular of various types of chain patterns.
#Finally
Have a good challenge idea?
Consider submitting it to /r/dailyprogrammer_ideas
"""


def main():
    pass


if __name__ == "__main__":
    main()
