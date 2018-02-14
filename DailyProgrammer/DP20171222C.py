"""
[2017-12-22] Challenge #345 [Hard] 2D Triangle Mesh Generator

https://www.reddit.com/r/dailyprogrammer/comments/7ljqhl/20171222_challenge_345_hard_2d_triangle_mesh/

#Description
You will be given a set of (x,y) coordinates. The goal of this challenge is to connect these points to create a set of
non-overlapping triangles. All points in the set much be connected to at least two other points, no lines may
intersect, and all regions bounded by points/lines must be triangles (bounded by exactly three points/lines). 
As a trivial example, consider the points [A`(0,0)`, B`(0,4)`, C`(4,4)`, D`(4,0)`, and
E`(2,2)`](https://i.imgur.com/rpsyq4w.png). 
To solve this set, draw lines [AB, BC, CD, DA, AE, BE, CE, and DE](https://i.imgur.com/Id1EkfS.png). 
All input sets are strictly bounded by a rectangle with horizontal/vertical edges and one corner at `(0,0)` and the all
corners given as points in the input. Your submission must draw this rectangle (with the rectangle's edges given as
edges in the output), and the rectangle's edges must conform to the above rules. 
*NOTE:* some inputs have multiple solutions. Your submission needs only to generate one solution. 
#Input:
The first line contains the number of points. Each subsequent line contains the x and y coordinates of a point
(separated by a space). 
#Output:
Lines that need to be drawn. I'm leaving this pretty open-ended. Print two points, `x1 y1 x2 y2` or `(x1,y1), (x2,y2)`
per line, or something similar. 
#Bonus:
Draw the input points and output lines to an actual image and post that instead of a huge text list of points.
#Double Bonus:
Generate some random inputs and post the inputs/outputs of the ones that look cool. 
#Triple Bonus:
Have your program fill in your drawn triangles with pretty colors. Pick them at random, or be more artistic than that.
Just have fun with it.
#Challenge inputs
0) [image](https://i.imgur.com/rpsyq4w.png)
    5
    0 0
    0 4
    4 4
    4 0
    2 2
&nbsp;
1) [image](https://i.imgur.com/kBgXVVz.png)
    8
    0 0 
    0 6 
    6 0 
    6 6 
    2 2 
    2 4 
    4 2 
    4 4
&nbsp;
2) [image](https://i.imgur.com/0L2vtk5.png)
    0 0
    0 32
    32 0
    32 32		
    13 13
    13 19
    19 19
    19 13			
    16 5
    16 27
    5 16
    27 16
#Challenge outputs
0) [image](https://i.imgur.com/Id1EkfS.png)  
1) [image](https://i.imgur.com/p0H8HG2.png)  
2) [image](https://i.imgur.com/z0j1t7J.png)
# Credit
This challenge was created by /u/lpreams, many thanks! If you have a challenge idea please share it on
/r/dailyprogrammer_ideas and there's a chance we'll use it.
"""


def main():
    pass


if __name__ == "__main__":
    main()
