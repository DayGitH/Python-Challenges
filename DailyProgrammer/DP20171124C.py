"""
[2017-11-24] Challenge #341 [Hard] Finding a Map Subsection

https://www.reddit.com/r/dailyprogrammer/comments/7f5uyg/20171124_challenge_341_hard_finding_a_map/

# Description
Imagine that you're working on an application to track boats as they travel across the ocean.  For this application,
you're given a square map with a fixed size (i.e. 2000x2000), and a set of coordinates that represent the ship's path
across the map.  You can assume the ship's path will be entirely within the bounds of the map.  The path *can* include
the very edge of the map.
However, viewing the entire map at once means the ship's path is quite small.  Your task is to write an algorithm that
outputs a smaller square area that contains the ship's path.  This smaller area will be used to display the path on a
viewing terminal.  
Your boss has asked for the following features:    
* The entire path must be contained within the output area.
* The smaller area must not extend beyond the edge of the larger map.
* Because the viewing terminal display is square, the output bounds must be square.
* If possible, add a 30 pixel border around the path, so the path doesn't go right to the edge of the screen.  If a
point is within 30 pixels of the edge, go up to the edge.
* The path should be centered within the smaller bounds, when possible.
**NOTE:**  These requirements are listed in order of importance.  The output being square is more important than the 30
pixel border, etc.  This means there may be cases where 30px border is not possible (the path is very close to an edge
of the map), or where it's not possible to be centered (path is in a corner of the map), etc.
**NOTE:** I have a solution to generate the chalenge outputs.  Depending how you do centering, the results might be off
by a pixel or two.  It doesn't have to be exact.
# Input Description
You will be given the following pieces of information separated by a comma:
1. Size of map
3. Set of points that describe the path of the ship
*Example:*
    2000, [(1000,1500),(1200, 1500),(1400,1600),(1600,1800)]
# Output Description
Your program should output a bounding square that contains all of the points in the format:
1. Lower left corner coordinates (X, Y)
2. Size of bounding box        
*Example:*
    (970, 1320), 660
# Challenge Inputs
    2000, [(600, 600), (700, 1200)]
    2000, [(300, 300), (1300, 300)]
    2000, [(825, 820), (840, 830), (830, 865), (835, 900)]
    
# Challenge Outputs
    (320, 570), 660
    (270, 0), 1060
    (763, 790), 140
Here are images of the challenge inputs/outputs:   
 
1. [https://i.imgur.com/WZ39Vlf.png](https://i.imgur.com/WZ39Vlf.png)
2. [https://i.imgur.com/HyMh3wv.png](https://i.imgur.com/HyMh3wv.png)
3. [https://i.imgur.com/M23z5gZ.png](https://i.imgur.com/M23z5gZ.png)
    
## Edge Cases
Here are some extra test cases that will test the literal edge and corner cases for this problem.
    # along the sides of the map, should push square towards the center
    5079, [(5079, 2000), (5079, 3000)]
    5079, [(10, 2000), (10, 3000)]
    5079, [(2000, 10), (3000, 10)]
    5079, [(2000, 5079), (3000, 5079)]
    # corners
    5079, [(0, 0), (600, 600)]
    5079, [(5079, 5079), (4479, 4479)]
    5079, [(0, 5079), (600, 4479)]
    5079, [(5079, 0), (4479, 600)]
    # entire width
    5079, [(1000, 0), (1000, 5079)]
    # entire height
    5079, [(0, 1000), (5079, 1000)]
    # entire area
    5079, [(0, 0), (5079, 5079)]
## Edge Cases Outputs
    (4019, 1970), 1060
    (0, 1970), 1060
    (1970, 0), 1060
    (1970, 4019), 1060
    (0, 0), 660
    (4419, 4419), 660
    (0, 4419), 660
    (4419, 0), 660
    (0, 0), 5079
    (0, 0), 5079
    (0, 0), 5079
### EDIT:
Some of the test cases aren't lining up with the requirements I stated above in cases where the padding is reduced
because it's close the edge.  Here are the updated test cases:
    (4019, 1970), 1060
    (0, 1970), 1060
    (1970, 0), 1060
    (1970, 4019), 1060
    (0, 0), 630
    (4449, 4449), 630
    (0, 4449), 630
    (4449, 0), 630
    (0, 0), 5079
    (0, 0), 5079
    (0, 0), 5079
"""


def main():
    pass


if __name__ == "__main__":
    main()
