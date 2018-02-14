"""
[2014-12-3] Challenge #191 [Intermediate] Space Probe. Alright Alright Alright.

https://www.reddit.com/r/dailyprogrammer/comments/2o5tb7/2014123_challenge_191_intermediate_space_probe/

#Description:
NASA has contracted you to program the AI of a new probe. This new probe must navigate space from a starting location
to an end location. The probe will have to deal with Asteroids and Gravity Wells. Hopefully it can find the shortest
path.
#Map and Path:
This challenge requires you to establish a random map for the challenge. Then you must navigate a probe from a starting
location to an end location.
#Map:
You are given N -- you generate a NxN 2-D map (yes space is 3-D but for this challenge we are working in 2-D space)
* 30% of the spots are "A" asteroids
* 10% of the spots are "G" gravity wells (explained below)
* 60% of the spots are "." empty space.
When you generate the map you must figure out how many of each spaces is needed to fill the map. The map must then be
randomly populated to hold the amount of Gravity Wells and Asteroids based on N and the above percentages.
## N and Obstacles
As n changes so does the design of your random space map. Truncate the amount of obstacles and its always a min size of
1. (So say N is 11 so 121 spaces. At 10% for wells you need 12.1 or just 12 spots) N can be between 2 and 1000. To keep
it simple you will assume every space is empty then populate the random Asteroids and Gravity wells (no need to compute
the number of empty spaces - they will just be the ones not holding a gravity well or asteroid)
## Asteroids
Probes cannot enter the space of an Asteroid. It will just be destroyed.
## Empty Spaces
Probes can safely cross space by the empty spaces of space. Beware of gravity wells as described below.
## Gravity Wells
Gravity wells are interesting. The Space itself is so dense it cannot be travelled in. The adjacent spaces of a Gravity
well are too strong and cannot be travelled in. Therefore you might see this.
. = empty space, G = gravity well
     .....
     .....
     ..G..
     .....
     .....
But due to the gravity you cannot pass (X = unsafe)
     .....
     .XXX.
     .XGX.
     .XXX.
     .....
You might get Gravity wells next to each other. They do not effect each other but keep in mind the area around them
will not be safe to travel in.
     ......
     .XXXX.
     .XGGX.
     .XXXX.
     ......
#Probe Movement:
Probes can move 8 directions. Up, down, left, right or any of the 4 adjacent corners. However there is no map wrapping.
Say you are at the top of the map you cannot move up to appear on the bottom of the map. Probes cannot fold space. And
for whatever reason we are contained to only the spots on the map even thou space is infinite in any direction. 
#Output:
Must show the final Map and shortest safe route on the map. 
* . = empty space
* S = start location
* E = end location
* G = gravity well
* A = Asteroid
* O = Path.
If you fail to get to the end because of no valid path you must travel as far as you can and show the path. Note that
the probe path was terminated early due to "No Complete Path" error.
#Challenge Input:
using (row, col) for coordinates in space.
Find solutions for:
* N = 10, start = (0,0) end = (9,9)
* N = 10, start = (9, 0) end = (0, 9)
* N= 50, start = (0,0) end = (49, 49)
#Map Obstacle %
I generated a bunch of maps and due to randomness you will get easy ones or hard ones. I suggest running your solutions
many times to see your outcomes. If you find the solution is always very straight then I would increase your asteroid
and gravity well percentages. Or if you never get a good route then decrease the obstacle percentages. 
#Challenge Theme Music:
If you need inspiration for working on this solution listen to this in the background to help you.
https://www.youtube.com/watch?v=4PL4kzsrVX8
Or
https://www.youtube.com/watch?v=It4WxQ6dnn0
"""


def main():
    pass


if __name__ == "__main__":
    main()
