"""
[2017-08-03] Challenge #325 [Intermediate] Arrow maze

https://www.reddit.com/r/dailyprogrammer/comments/6rb98p/20170803_challenge_325_intermediate_arrow_maze/

#Description
We want to return home, but we have to go trough an [arrow maze](http://imgur.com/TjYhSB4).
We start at [a certain point](http://imgur.com/QTxERGr) an in a arrow maze you can only follow [the direction of the
arrow](http://imgur.com/a097dDJ).
At each node in the maze we can decide to change direction (depending on the new node) or follow the direction we where
going.
When done right, we should have a path to [home](http://imgur.com/UqD5Brf) 
#Formal Inputs & Outputs
##Input description
You recieve on the first line the coordinates of the node where you will start and after that the maze.
`n ne e se s sw w nw` are the direction you can travel to and `h` is your target in the maze.
    (2,0)
     e se se sw  s
     s nw nw  n  w
    ne  s  h  e sw
    se  n  w ne sw
    ne nw nw  n  n
I have added extra whitespace for formatting reasons
##Output description
You need to output the path to the center.
    (2,0)
    (3,1)
    (3,0)
    (1,2)
    (1,3)
    (1,1)
    (0,0)
    (4,0)
    (4,1)
    (0,1)
    (0,4)
    (2,2)
you can get creative and use acii art or even better
#Notes/Hints
If you have a hard time starting from the beginning, then backtracking might be a good option.
#Finally
Have a good challenge idea?
Consider submitting it to /r/dailyprogrammer_ideas
"""


def main():
    pass


if __name__ == "__main__":
    main()
