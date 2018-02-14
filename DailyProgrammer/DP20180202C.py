"""
[2018-02-02] Challenge #349 [Hard] Divide Polygons into Equal Regions

https://www.reddit.com/r/dailyprogrammer/comments/7us3w7/20180202_challenge_349_hard_divide_polygons_into/

# Description
You are given a number of points, forming the hull of a convex polygon.  You are also given a number _N_. 
Your goal is to partition the original polygon into _N_ smaller polygons,  all containing equal amount of space
(surface, volume, ...), by adding at most one node, and as many edges as required.
If it is impossible to find a valid solution by adding the single node,  you may give a result for the max number <
_N_, for which a equitable partitioning is possible.
# Input Description
First line is the number _N_, the second line contains coordinates of the nodes of the convex polygon. The third line
contains the edges, where the numbers represent the index of the nodes.
For example:
    2
    (0 0)(0.5 0.5)(0 1)
    (1 2)(2 3)(3 1)
# Output Description
You should return all added nodes.
Optional: Display your result by plotting the nodes and edges.
For example:
    (0 0.5)
# Challenge inputs
    3 
    (0.49 0.7)(0.23 0.64) (0.95 0.48)
    (1 2)(2 3)(3 1)
    4 
    (0.49 0.7)(1.23 0.64) (0.95 1.48)
    (1 2)(2 3)(3 1)
    2 
    (1.49 0.7)(0.23 0.64) (0.95 1.48)
    (1 2)(2 3)(3 1)
    5
    (1 0)(0 1)(0 2)(1 3)(2 1)
    (1 2)(2 3)(3 4)(4 5)(5 1)
## Note an edit to fix an error
This last challenge input had previously been this, and this does not work as a convex polygon.
    5
    (1 0)(0 1)(2 1)(0 2)(1 3)
    (1 2)(2 3)(3 4)(4 5)(5 1)
This has been fixed, thanks all. 
# Bonus Challenge Inputs
    2
    (0)(1)
    (1 2)
    4
    (1 2 3)(3 2 1)(2 1 3)
    (1 2)(2 3)(3 1)
    3
    (0 0 1)(0 1 0)(0 0 1)(1 1 1)
    (1 2)(1 3)(1 4)(2 3)(2 4)(3 4)
    3
    (0 0 1 39789)(0 1 0 39872)(0 0 1 41234)(1 1 1 42546)
    (1 2)(1 3)(1 4)(2 3)(2 4)(3 4)    
# Bonus++
In case you can't find a valid solution by adding a single point,  you may add as many nodes as you need, as long as
these are on the faces of the polygon.
# Credit
This challenge was suggested by use /u/tomekanco, many thanks. If you have a challenge idea, please share it on
/r/dailyprogrammer_ideas and there's a good chance we'll use it.
"""


def main():
    pass


if __name__ == "__main__":
    main()
