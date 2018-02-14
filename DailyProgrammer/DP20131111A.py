"""
[11/11/13] Challenge #142 [Easy] Falling Sand

https://www.reddit.com/r/dailyprogrammer/comments/1rdtky/111113_challenge_142_easy_falling_sand/

# [](#EasyIcon) *(Easy)*: Falling Sand
[Falling-sand Games](http://en.wikipedia.org/wiki/Falling-sand_game) are particle-simulation games that focus on the
interaction between particles in a 2D-world. Sand, as an example, might fall to the ground forming a pile. Other
particles might be much more complex, like fire, that might spread depending on adjacent particle types.
Your goal is to implement a mini falling-sand simulation for just sand and stone. The simulation is in 2D-space on a
uniform grid, where we are viewing this grid from the side. Each type's simulation properties are as follows:
* Stone always stays where it was originally placed. It never moves.
* Sand keeps moving down through air, one step at a time, until it either hits the bottom of the grid, other sand, or
stone.
# Formal Inputs & Outputs
## Input Description
On standard console input, you will be given an integer N which represents the N x N grid of ASCII characters. This
means there will be N-lines of N-characters long. This is the starting grid of your simulated world: the character ' '
(space) means an empty space, while '.' (dot) means sand, and '#' (hash or pound) means stone. Once you parse this
input, simulate the world until all particles are settled (e.g. the sand has fallen and either settled on the ground or
on stone). "Ground" is defined as the solid surface right below the last row.
## Output Description
Print the end result of all particle positions using the input format for particles.
# Sample Inputs & Outputs
## Sample Input
    5
    .....
      #  
    #    
         
        .
## Sample Output
      .  
    . #  
    #    
        .
     . ..
"""


def main():
    pass


if __name__ == "__main__":
    main()
"""
[11/11/13] Challenge #141 [Easy] Checksums

https://www.reddit.com/r/dailyprogrammer/comments/1qwkdz/111113_challenge_141_easy_checksums/

# [](#EasyIcon) *(Easy)*: Checksums
[Checksums](http://en.wikipedia.org/wiki/Checksum) are a tool that allow you to verify the integrity of data (useful
for networking, security, error-correction, etc.). Though there are *many* different Checksum algorithms, the general
usage is that you give raw-data to your algorithm of choice, and a block of data (usually smaller than the given data)
is generated and can later be used by re-computing the checksum and comparing the original and recent values.
A classic example for how helpful Checksums are is with data-networking: imagine you have a packet of information that
must be guaranteed the same after receiving it. Before sending the data, you can compute its checksum, and send both
blocks together. When received, the data can be used to re-compute a checksum, and validate that the given checksum and
your own checksum are the same. The subject is much more complex, since there are issues of
[data-entropy](http://en.wikipedia.org/wiki/Entropy_(information_theory\)) and the importance of the checksum's size
compared to the raw data size.
This example is so common in network programming, one of the [basic Internet networking protocols
(TCP)](http://en.wikipedia.org/wiki/Transmission_Control_Protocol#Checksum_computation) has it built-in!
Your goal will be more modest: you must implement a specific checksum algorithm ([Fletcher's 16-bit
Checksum](http://en.wikipedia.org/wiki/Fletcher%27s_checksum)) for given lines of text input. The [C-like language
pseudo-code found on Wikipedia](http://en.wikipedia.org/wiki/Fletcher%27s_checksum#Straightforward) is a great starting
point!
**Note:** Make sure to explicitly implement this algorithm, and not call into other code (libraries). The challenge
here is focused on your implementation of the algorithm.
# Formal Inputs & Outputs
## Input Description
On standard console input, you will first be given an integer N which ranges inclusively from 1 to 256. After this
line, you will receive N-lines of ASCII text. This text will only contain regular printable characters, and will all be
on a single line of input.
## Output Description
For each line of input, print the index (starting from 1) and the 16-bit Fletcher's checksum as a 4-digit hexadecimal
number.
# Sample Inputs & Outputs
## Sample Input
    3
    Fletcher
    Sally sells seashells by the seashore.
    Les chaussettes de l'archi-duchesse, sont-elles seches ou archi-seches ?
## Sample Output
    1 D330
    2 D23E
    3 404D
"""


def main():
    pass


if __name__ == "__main__":
    main()
"""
[11/11/13] Challenge #141 [Easy] Monty Hall Simulation

https://www.reddit.com/r/dailyprogrammer/comments/1qdw40/111113_challenge_141_easy_monty_hall_simulation/

# [](#EasyIcon) *(Easy)*: Monty Hall Simulation
The [Monty Hall Problem](http://en.wikipedia.org/wiki/Monty_Hall_problem) is a probability puzzle that has a very
non-intuitive answer for the average person. Here's the problem description taken from Wikipedia:
*"Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the
others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No.
3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your
choice?"*
AsapScience has a great [YouTube video describing this game](http://www.youtube.com/watch?v=9vRUxbzJZ9Y). If you don't
understand *why* switching doors is the best tactic, feel free to discuss it here or on other great subreddits, like
/r/Math, /r/ComputerScience, or even /r/AskScience!
Your goal is to simulate two tactics to this puzzle, and return the percentage of successful results. The first tactic
is where you stick with your initial choice. The second tactic is where you always switch doors.
**Edit:** Make sure to actually simulate *both* techniques. Write that code out in its entirety, don't compute the
second result being '100% - first techniques percentage', though that's certainly true mathematically.
# Formal Inputs & Outputs
## Input Description
On standard console input, you will be given a single integer ranging inclusively from 1 to 4,294,967,295 (unsigned
32-bit integer). This integer is the number of times you should simulate the game for both tactics. Remember that a
single "game simulation" is your program randomly placing a car behind one door and two goats behind the two remaining
doors. You must then randomly pick a door, have one of the two remaining doors open, but only open if it's a goat
behind said door! After that, if using the first tactic, you may open the picked door, or if using the second tactic,
you may open the other remaining door. Keep track if your success rates in both simulations.
## Output Description
On two seperate lines, print "Tactic 1: X% winning chance" and "Tactic 2: Y% winning chance", where X and Y are the
percentages of success for the respective tactics
# Sample Inputs & Outputs
## Sample Input
    1000000
## Sample Output
    Tactic 1: 33.3% winning chance
    Tactic 2: 66.6% winning chance
## Difficulty++
For an extra challenge, visualize the simulation! Using whatever tools and platform you want, let the simulation
visually show you the doors it's picking over time. Try to aim for one simulation a second, keeping it fast-paced.
"""


def main():
    pass


if __name__ == "__main__":
    main()
