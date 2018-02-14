"""
[2016-07-08] Challenge #274 [Hard] ∞ Loop solver

https://www.reddit.com/r/dailyprogrammer/comments/4rug59/20160708_challenge_274_hard_loop_solver/

#Description
∞ Loop is a mobile game that consists of n\*m tiles, placed in a n\*m grid. There are 16 different tiles:
┃, ━, ┏, ┓, ┛, ┗, ┣, ┳, ┫, ┻, ╋, ╹, ╺, ╻, ╸, and the empty tile.
(If some of the Unicode characters aren't shown, [here](http://i.imgur.com/PWyeW5r.png) is a screenshot of this
paragraph).
In other words, every tile may or may not have a "pipe" going up, a "pipe" going right, a "pipe" going down, and a
"pipe" going left. All combinations of those are valid, legal tiles.
At the beginning of the game, the grid is filled with those tiles. The player may then choose some tile and rotate it
90 degrees to the right. The player may do this an unlimited amount of times. For example, ┣ becomes ┳ and ┛ becomes ┗,
but ╋ stays ╋.
The objective is to create a closed loop: every pipe must have another tile facing it in the adjacent tile — for
example if some tile has a pipe going right, its adjacent tile to the right must have a pipe going left. 
In case you need clarification, [here's](https://www.youtube.com/watch?v=TlR1hfiIk10) some random guy playing it.
Your task is to write a program that, given an initial grid of tiles, outputs a solution to that grid.
#Formal Inputs &amp; Outputs
An easy way to represent tiles without having to deal with Unicode (or ASCII art) is to use the bitmask technique to
encode the tiles as numbers 0...15. 
To encode a tile:  
* Start with 0.  
* If the tile has a pipe going up, add 1.  
* If the tile has a pipe going right, add 2.  
* If the tile has a pipe going down, add 4.  
* If the tile has a pipe going left, add 8.  
For example, ┫ becomes 1+4+8=13.
If we look at the binary representation of that number, we see that:  
* The first digit from the right shows whether the tile has a pipe going up;  
* The second digit from the right shows whether the tile has a pipe going right;   
* The third digit from the right shows whether the tile has a pipe going down;  
* The fourth digit from the right shows whether the tile has a pipe going left.  
13 in binary is 1101, from which it is evident that all pipes are present except the pipe going right.
##Input description
The input consists of n rows, each row having m space-separated numbers in it. Those numbers are the tiles, encoded in
the bitmask technique discussed above.
You may also include the number of rows and columns in the input, if that makes it easier to read the input.
##Output description
Output a similar grid which is obtained by rotating some or all tiles in the input grid. A tile may be rotated multiple
times. The output grid must be a closed loop.
##Sample input 1
    9 12 12 6
    10 13 13 5
    3 3 9 3
##Sample output 1
    6 12 6 12
    5 7 13 5
    3 9 3 9
The sample input corresponds to:
    ┛┓┓┏
    ━┫┫┃
    ┗┗┛┗
By rotating some tiles, we get:
    ┏┓┏┓
    ┃┣┫┃
    ┗┛┗┛,
which corresponds to the sample output and is a closed loop.
(Again, if Unicode characters don't load, [here](http://i.imgur.com/lqCGY3e.png) is the first sample input).
##Sample input 2
    0 8 8 0
##Sample output 2
    0 2 8 0
The input corresponds to ╸╸, surrounded by two empty tiles.  
The corresponding output is ╺╸.
#Notes
It is easiest to use the bitwise and/or/xor operators to rotate and check for pipes. Most programming languages have
such operators. The bitwise shift operators may also be helpful to rotate the tiles.
[Here's](https://en.wikipedia.org/wiki/Mask_(computing\)) a Wikipedia article on using them on bitmasks.
#Finally
This challenge was suggested by /u/A858DE57B86C2F16F, many thanks! Have a good challenge idea?   Consider submitting it
to /r/dailyprogrammer_ideas
"""


def main():
    pass


if __name__ == "__main__":
    main()
