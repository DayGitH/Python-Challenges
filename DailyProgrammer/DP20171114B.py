"""
[2017-11-14] Challenge #340 [Intermediate] Walk in a Minefield

https://www.reddit.com/r/dailyprogrammer/comments/7d4yoe/20171114_challenge_340_intermediate_walk_in_a/

#Description
You must remotely send a sequence of orders to a robot to get it out of a minefield.
You win the game when the order sequence allows the robot to get out of the minefield without touching any mine.
Otherwise it returns the position of the mine that destroyed it.
A mine field is a grid, consisting of ASCII characters like the following:
    +++++++++++++
    +000000000000
    +0000000*000+
    +00000000000+
    +00000000*00+
    +00000000000+
    M00000000000+
    +++++++++++++
The mines are represented by * and the robot by M.
The orders understandable by the robot are as follows:
* N moves the robot one square to the north
* S moves the robot one square to the south
* E moves the robot one square to the east
* O moves the robot one square to the west
* I start the the engine of the robot
* - cuts the engine of the robot
If one tries to move it to a square occupied by a wall `+`, then the robot stays in place.
If the robot is not started (`I`) then the commands are inoperative.
It is possible to stop it or to start it as many times as desired (but once enough)
When the robot has reached the exit, it is necessary to stop it to win the game.
# The challenge
Write a program asking the user to enter a minefield and then asks to enter a sequence of commands to guide the robot
through the field.
It displays after won or lost depending on the input command string.
##Input
The mine field in the form of a string of characters, newline separated. 
##Output
Displays the mine field on the screen
    +++++++++++
    +0000000000
    +000000*00+
    +000000000+
    +000*00*00+
    +000000000+
    M000*00000+
    +++++++++++
##Input 
Commands like:
    IENENNNNEEEEEEEE-
## Output
Display the path the robot took and indicate if it was successful or not. Your program needs to evaluate if the route
successfully avoided mines and both started and stopped at the right positions. 
#Bonus
Change your program to randomly generate a minefield of user-specified dimensions and ask the user for the number of
mines.
In the minefield, randomly generate the position of the mines. No more than one mine will be placed in areas of 3x3
cases. We will avoid placing mines in front of the entrance and exit. 
Then ask the user for the robot commands. 
# Credit
This challenge was suggested by user /u/Preferencesoft, many thanks! If you have a challenge idea, please share it at
/r/dailyprogrammer_ideas  and there's a chance we'll use it. 
"""


def main():
    pass


if __name__ == "__main__":
    main()
