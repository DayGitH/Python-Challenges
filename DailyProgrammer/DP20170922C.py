"""
[2017-09-22] Challenge #332 [Hard] Skyscrapers and CEO's peculiar requirements

https://www.reddit.com/r/dailyprogrammer/comments/71pzlb/20170922_challenge_332_hard_skyscrapers_and_ceos/

#Description
Skyscraper is a logic puzzle similar to Sudoku.
You have an NxN grid that you'll fill such that every row and column contains 1...N
fx:
    1 2 3 4
    2 3 4 1
    3 4 1 2
    4 1 2 3
	
There is however a catch, since we're working with a grid of Skyscrapers we cant just place them willy nilly.
The Mayor sits in his office and demands that you can only see so many skyscrapers from different directions (only
looking across columns and rows)
To solve this issue we have to abuse that each skyscraper is only as high as its number, and can hide lower skyscrapers
behind it.
For example looking either from the left or right in this row:
 
    1 4 3 2
From the left can 2 skyscrapers be seen, 1, and 4.
From the right can 3 skyscrapers be seen, 2, 3, and 4.
#Input example
First we will get an N telling us how big the grid is in NxN. (10 > N > 0)
N will only be different from 4 in the bonus, so you can assume N is always 4 outside of the bonus
Secondly we get all the view demands in a single array (N >= X_i >= 0)
The array is always of length N * 4
0's mean that there are no demands for the view of the given row/column
0's means no constraint in number of buildings in view
You must be able to see EXACTLY the amount that is told, no more, no less
The array should be read as such:
Going clockwise around the grid starting at the top-left
    3
    0 1 0 2 1 3 2 0 1 0 2 2
    - 0 1 0 -
    2 ? ? ? 2
    2 ? ? ? 1
    0 ? ? ? 3
    - 1 0 2 -
Or as displayed with indexes
    -- 0 1 2 -
    11 ? ? ? 3
    10 ? ? ? 4
    09 ? ? ? 5
    -- 8 7 6 -
	
Where each number is looking inwards at their respective column/row
#Output example
The output is the filled out city grid
For the input above we get:
    1 3 2
    2 1 3
    3 2 1
#Challenge input
##Challenge 1
    4
    3 1 2 2 2 2 1 3 2 2 3 1 1 2 3 2
##Challenge 2
    4
    0 0 0 0 0 2 0 0 3 0 0 0 1 3 0 3
#Challenge output
##Challenge 1
    
    2 4 1 3
    1 3 4 2
    3 1 2 4
    4 2 3 1
##Challenge 2
    2 1 3 4
    3 4 1 2
    1 2 4 3
    4 3 2 1
#Bonus
Make it solve for an n by n game
Some tiles may already be filled in
After the array of ints there will be an NxN 2D array of ints with some prefilled tiles
all 0 tiles are empty ones your solver need to fill out
## Bonus input
### Bonus 1
    8
    1 3 2 5 4 2 2 3 3 2 5 2 3 1 3 3 3 4 2 2 1 2 3 3 3 4 2 2 3 3 4 1
    0 6 0 0 5 0 1 0
    0 2 1 0 0 0 0 0
    2 0 0 0 6 0 3 0
    0 0 0 0 0 8 0 0
    0 0 6 0 0 3 7 0
    0 0 5 0 0 0 0 0
    0 0 0 0 0 0 0 3
    0 0 0 0 3 0 0 0
### Bonus 2
    6
    4 3 0 3 2 2 0 0 0 3 0 0 0 2 0 2 0 0 2 3 0 0 0 0
    2 0 0 0 0 0
    0 0 0 0 4 0
    0 0 0 0 0 0
    0 2 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
## Bonus output
### Bonus 1
    8 6 2 3 5 7 1 4
    3 2 1 5 4 6 8 7
    2 7 8 4 6 5 3 1
    5 4 3 1 7 8 2 6
    4 8 6 2 1 3 7 5
    7 3 5 6 2 1 4 8
    1 5 4 7 8 2 6 3
    6 1 7 8 3 4 5 2
### Bonus 2
    2 3 6 4 5 1
    3 5 1 2 4 6
    5 1 2 3 6 4
    6 2 4 5 1 3
    1 4 3 6 2 5
    4 6 5 1 3 2
#Hint
A better explanation than I ever could do and some helpful hints can be found here:
https://www.brainbashers.com/skyscrapershelp.asp
#Extra
If you have any challenges, please share it at /r/dailyprogrammer_ideas!
And remember to upvote challenges you like :)
"""


def main():
    pass


if __name__ == "__main__":
    main()
