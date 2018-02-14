"""
[05/10/13] Challenge #123 [Hard] Robot Jousting

https://www.reddit.com/r/dailyprogrammer/comments/1ej32w/051013_challenge_123_hard_robot_jousting/

# [](#HardIcon) *(Hard)*: Robot Jousting
You are an expert in the new and exciting field of *Robot Jousting*! Yes, you read that right: robots that charge one
another to see who wins and who gets destroyed. Your job has been to work on a simulation of the joust matches and
compute *when* there is a collision between the two robots and *which* robot would win (the robot with the higher
velocity), thus preventing the destruction of very expensive hardware.
Let's define the actual behavior of the jousting event and how the robots work: the event takes place in a long
hallway. Robots are placed initially in the center on the far left or far right of the hallway. When robots start, they
choose a given starting angle, and keep moving forward until they hit a wall. Once a robot hits a wall, they stop
movement, and rotate back to the angle in which they came into the wall. Basically robots "reflect" themselves off the
wall at the angle in which they hit it. For every wall-hit event, the robot loses 10% of its speed, thus robots will
slow down over time (but never stop until there is a collision).
[Check out these two images as examples of the described scene](http://imgur.com/a/NSzpY). Note that the actual robot
geometry you want to simulate is a perfect circle, where the radius is 0.25 meters, or 25 centimeters.
# Formal Inputs & Outputs
## Input Description
You will be given three separate lines of information: the first has data describing the hallway that the robots will
joust in, and then the second and third represent information on the left and right robots, respectively.
The first line will contain two integers: how long and wide the hallway is in meters. As an example, given the line "10
2", then you should know that the length of the hallway is 10 meters, while the width is just 2 meters.
The second and third lines also contain two integers: the first is the initial angle the robot will move towards (in
degrees, as a signed number, where degree 0 always points to the center of the hallway, negative points to the left,
and positive points to the right). The second integer is the speed that the robot will initially move at, as defined in
millimeters per second. As an example, given the two lines "45 5" and "-45 2", we know that the left robot will launch
at 45 degrees to its left, and that the second robot will launch 45 degrees to its left (really try to understand the
angle standard we use). The left robot starts with an initial speed of 5 mm/s with the right robot starting at 2 mm/s.
Assume that the robot radius will always be a quarter of a meter (25 centimeters).
## Output Description
Simply print "Left robot wins at X seconds." or "Right robot wins at X seconds." whenever the robots collide: make sure
that the variable X is the number of seconds elapsed since start, and that the winning robot is whichever robot had the
higher velocity. In case the robots never hit each other during a simulation, simply print "No winner found".
# Sample Inputs & Outputs
## Sample Input
    10 2
    30 5
    -10 4
## Sample Output
*Please note that this is FAKE data; I've yet to write my own simulation...*
    Left robot wins at 32.5 seconds.
# Challenge Note
Make sure to keep your simulation as precise as possible! Any cool tricks with a focus on precision management will get
bonus awards! This is also a very open-ended challenge question, so feel free to ask question and discuss in the
comments section.
"""


def main():
    pass


if __name__ == "__main__":
    main()
"""
[05/10/13] Challenge #122 [Hard] Subset Sum Insanity

https://www.reddit.com/r/dailyprogrammer/comments/1e2rcx/051013_challenge_122_hard_subset_sum_insanity/

# [](#HardIcon) *(Hard)*: Subset Sum 
The [subset sum](http://en.wikipedia.org/wiki/Subset_sum_problem) problem is a classic computer science challenge:
though it may appear trivial on its surface, there is no known solution that runs in [deterministic polynomial
time](http://en.wikipedia.org/wiki/P_(complexity)) (basically this is an
[NP-complete](http://en.wikipedia.org/wiki/Subset_sum_problem) problem). To make this challenge more "fun" (in the same
way that losing in Dwarf Fortress is "fun"), we will be solving this problem in a three-dimensional matrix and define a
subset as a set of integers that are directly adjacent!
**Don't forget our [previous
week-long](http://www.reddit.com/r/dailyprogrammer/comments/1dk7c7/05213_challenge_121_hard_medal_management/) [Hard]
challenge competition ends today!**
# Formal Inputs & Outputs
## Input Description
You will be given three integers `(U, V, W)` on the first line of data, where each is the length of the matrices'
respective dimensions (meaning U is the number of elements in the X dimension, V is the number of elements in the Y
dimension, and W is the number of elements in the Z dimension). After the initial line of input, you will be given a
series of space-delimited integers that makes up the 3D matrix. Integers are ordered first in the X dimension, then Y,
and then Z ( [the coordinate system is clarified here](http://i.imgur.com/nxChpUZ.png) ).
## Output Description
Simply print all sets of integers that sum to 0, if this set is of directly-adjacent integers (meaning a set that
travels vertically or horizontally, but never diagonally). If there are no such sets, simply print "No subsets sum to
0".
# Sample Inputs & Outputs
## Sample Input
    2 2 3
    -1 2 3 4 1 3 4 5 4 6 8 10
## Sample Output
    -1 1
*Note:* This is set of positions (0, 0, 0), and (0, 0, 1).
# Challenge Input
    8 8 8
    -7 0 -10 -4 -1 -9 4 3 -9 -1 2 4 -6 3 3 -9 9 0 -7 3 -7 -10 -9 4 -6 1 5 -1 -8 9 1 -9 6 -1 1 -8 -6 -5 -3 5 10 6 -1 2
-2 -7 4 -4 5 2 -10 -8 9 7 7 9 -7 2 2 9 2 6 6 -3 8 -4 -6 0 -2 -8 6 3 8 10 -5 8 8 8 8 0 -1 4 -5 9 -7 -10 1 -7 6 1 -10 8 8
-8 -9 6 -3 -3 -9 1 4 -9 2 5 -2 -10 8 3 3 -1 0 -2 4 -5 -2 8 -8 9 2 7 9 -10 4 9 10 -6 5 -3 -5 5 1 -1 -3 2 3 2 -8 -9 10 4
10 -4 2 -5 0 -4 4 6 -1 9 1 3 -7 6 -3 -3 -9 6 10 8 -3 -5 5 2 6 -1 2 5 10 1 -3 3 -10 6 -6 9 -3 -9 9 -10 6 7 7 10 -6 0 6 8
-10 6 4 -4 -1 7 4 -9 -3 -10 0 -6 7 10 1 -9 1 9 5 7 -2 9 -8 10 -8 -7 0 -10 -7 5 3 2 0 0 -1 10 3 3 -7 8 7 5 9 -7 3 10 7
10 0 -10 10 7 5 6 -6 6 -9 -1 -8 9 -2 8 -7 -6 -8 5 -2 1 -9 -8 2 9 -9 3 3 -8 1 -3 9 1 3 6 -6 9 -2 5 8 2 -6 -9 -9 1 1 -9 5
-4 -9 6 -10 10 -1 8 -2 -6 8 -9 9 0 8 0 4 8 -7 -9 5 -4 0 -9 -8 2 -1 5 -6 -5 5 9 -8 3 8 -3 -1 -10 10 -9 -10 3 -1 1 -1 5
-7 -8 -5 -10 1 7 -3 -6 5 5 2 6 3 -8 9 1 -5 8 5 1 4 -8 7 1 3 -5 10 -9 -2 4 -5 -7 8 8 -8 -7 9 1 6 6 3 4 5 6 -3 -7 2 -2 7
-1 2 2 2 5 10 0 9 6 10 -4 9 7 -10 -9 -6 0 -1 9 -3 -9 -7 0 8 -5 -7 -10 10 4 4 7 3 -5 3 7 6 3 -1 9 -5 4 -9 -8 -2 7 10 -1
-10 -10 -3 4 -7 5 -5 -3 9 7 -3 10 -8 -9 3 9 3 10 -10 -8 6 0 0 8 1 -7 -8 -6 7 8 -1 -4 0 -1 1 -4 4 9 0 1 -6 -5 2 5 -1 2 7
-8 5 -7 7 -7 9 -8 -10 -4 10 6 -1 -4 -5 0 -2 -3 1 -1 -3 4 -4 -6 4 5 7 5 -6 -6 4 -10 -3 -4 -4 -2 6 0 1 2 1 -7
# Challenge Note
Like any challenge of this complexity class, you are somewhat constrained to solving the problem with brute-force (sum
all possible sub-sets). We really want to encourage any and all new ideas, so really go wild and absolutely do whatever
you think could solve this problem quickly!
"""


def main():
    pass


if __name__ == "__main__":
    main()
