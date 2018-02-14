"""
[2016-08-26] Challenge #280 [Hard] Free Flow Solver

https://www.reddit.com/r/dailyprogrammer/comments/4zog32/20160826_challenge_280_hard_free_flow_solver/

# Description
Flow Free is a game that consists of an n*m grid with some cells that have a color (the other cells are initially
empty). For every colored cell, there is exactly one other cell on the grid that has the same color -- there can't be 3
cells with the same color, or a cell that is unique in its color.
The objective of the player is to connect all the matching colors in the grid, by making "pipes" between them, that go
through empty cells.
The pipes must not cross or overlap, and they have to cover the whole board.
[Here](http://i.imgur.com/xLQXz.jpg)'s an example of a Flow Free puzzle (to the left) and its solution (right). For
additional clarification, [Here](https://www.youtube.com/watch?v=83g8pDQg_Ng)'s somebody solving some puzzles.
Your objective is to write a program that, given a Flow Free puzzle, outputs its solution.
# Formal Inputs and Outputs
We will represent the positions of the grid using Cartesian coordinates: the upper leftmost cell is (0, 0), and the
cell that is located n cells to the right of it and m cells underneath it, is called (n, m).
## Input Description
The first line consists 3 numbers, *A*, *N*, and *M*, separated by space. *A* is the number of colors, *N* is the width
of the grid and *M* is its height.
The next *A* lines specify the matching cells - each line contains two cartesian coordinates (for matching cells),
separated by a space `(x1, y1) (x2, y2)`.
Example (for [the puzzle](http://i.imgur.com/xLQXz.jpg) that was previously given as an example):
    5 5 5
    (1, 0) (0, 3)
    (2, 0) (0, 4)
    (3, 0) (3, 4)
    (3, 1) (2, 2)
    (2, 4) (3, 3)
## Output Description
The output consists of *A* lines, each line is a sequence of some cartesian coordinates (separated by a space), that
specifies the path of a pipe between two matching cells.
The first and last cells of an output line are the matching cells that were initially colored, everything between them
consists of the cells of the pipe. The order of the output's lines doesn't matter - it doesn't have to correspond to
the input.
Possible example output (Again, the lines don't have to be sorted in a certain way):
    (2, 0) (2, 1) (1, 1) (1, 2) (1, 3) (1, 4) (0, 4)
    (1, 0) (0, 0) (0, 1) (0, 2) (0, 3)
    (3, 0) (4, 0) (4, 1) (4, 2) (4, 3) (4, 4) (3, 4)
    (2, 4) (2, 3) (3, 3)
    (3, 1) (3, 2) (2, 2)
# Credit
This challenge was suggested by /u/Avnerium. If you have a challenge idea, please share it in /r/dailyprogrammer_ideas
and there's a good chance we'll use it.
"""


def main():
    pass


if __name__ == "__main__":
    main()
