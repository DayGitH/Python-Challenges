"""
[8/30/2012] Challenge #93 [difficult] (15-puzzle)


https://www.reddit.com/r/dailyprogrammer/comments/z3a9x/8302012_challenge_93_difficult_15puzzle/

Write a program that can solve a standard ['15-puzzle'](http://en.wikipedia.org/wiki/Fifteen_puzzle).
The program should read in a hex string describing the puzzle state from left to right top to bottom, where F is a
blank...for example,:
    0FD1C3B648952A7E 
    
would describe the puzzle
	+----+----+----+----+
	| 0  |    | 13 | 1  |
	+----+----+----+----+
	| 12 | 3  | 11 | 6  |
	+----+----+----+----+
	| 4  | 8  | 9  | 5  |
	+----+----+----+----+
	| 2  | 10 | 7  | 14 |
	+----+----+----+----+
The program should output the final solution 0123456789ABCDEF, and ALSO output EACH intermediate board state as a
string on the way to finding a solution.
Warning: I don't know if the above puzzle is actually solvable.
"""


def main():
    pass


if __name__ == "__main__":
    main()
