"""
[2017-10-18] Challenge #336 [Intermediate] Repetitive Rubik's Cube

https://www.reddit.com/r/dailyprogrammer/comments/776lcz/20171018_challenge_336_intermediate_repetitive/

# Description
The Rubik's Cube is a pleasant and challenging pastime. In this exercise however, we don't want to solve the cube. We
want to (mindlessly) execute the same sequence over and over again. We would like to know how long it will take us to
go back to the original starting position.
Write a program which, given a series of moves, outputs the number of times that sequence must be executed to reach the
original state again.
# Input Description 
A space separated series of movies in the official [WCA
Notation](https://www.worldcubeassociation.org/regulations/#article-12-notation) will be given.
Summary (from [Challenge
#157](https://www.reddit.com/r/dailyprogrammer/comments/22k8hu/492014_challenge_157_intermediate_puzzle_cube/?st=j8kfmdyb&sh=9f0157fe)
* There are 6 faces. U (up, the top face). D (down, the bottom face). L (left). R (right). F (front). B (back).
* Each face is turned like you were looking at it from the front.
* A notation such as X means you turn the X face clockwise 90'. So R L means turn the right face clockwise 90' (from
its perspective), then the left face clockwise 90' (from its perspective).
* A notation such as X' (pronounced prime) means you turn the X face anticlockwise 90'. So R U' means turn the right
face clockwise 90', then the top face anticlockwise 90'.
* notation such as X2 means you turn the X face 180'.
Example (each line is a separate challenge):
    R F2 L' U D B2
# Output Description 
The output should be the number of times you have to execute the input sequence to arrive at the original state.
# Challenge Inputs
    R
    R F2 L' U D B2
    R' F2 B F B F2 L' U F2 D R2 L R' B L B2 R U
# Challenge Outputs
    4
    18
    36
                
# Credit
This challenge was suggested by user /u/snow_in_march, many thanks! If you have an idea for a challenge please share it
on /r/dailyprogrammer_ideas and there's a good chance we'll use it. 
"""


def main():
    pass


if __name__ == "__main__":
    main()
