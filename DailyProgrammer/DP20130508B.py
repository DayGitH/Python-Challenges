"""
[05/08/13] Challenge #124 [Intermediate] Circular Graphs

https://www.reddit.com/r/dailyprogrammer/comments/1ee664/050813_challenge_124_intermediate_circular_graphs/

# [](#IntermediateIcon) *(Intermediate)*: Circular Graphs
A classic problem in computer science & [graph-theory](http://en.wikipedia.org/wiki/Graph_theory) is to detect if there
are any [circular paths](http://en.wikipedia.org/wiki/Cycle_(graph_theory\)) in a given directed graph (sometimes
called a cycle). Your goal is to write a program that takes in a series of edges, which defines a graph, and then print
all sets of cycles onto a console or text file.
For the sake of clarity, we define a cycle as a set of vertices that have at least one incoming edge and one outgoing
edge, where each node is only directly connected to at most two other nodes within the list.
*Author: nint22*
# Formal Inputs & Outputs
## Input Description
You will first be given an integer N, which represents the number of edges that will be given on each following
new-line. Edges are defined as two integer numbers, where the direction of the edge always goes from the left vertex to
the right vertex.
## Output Description
Simply print all vertices in a directed cycle; make sure that the cycle is closed (see sample output).
# Sample Inputs & Outputs
## Sample Input
    4
    1 2
    2 3
    3 1
    3 4
## Sample Output
    1 2 3 1
# Note
As usual with these kind of problems, the challenge isn't in writing a solution, but writing a *fast*-solution. If you
post a solution, please discuss the big-O notation of your search function. Good luck, and have fun programming!
"""


def main():
    pass


if __name__ == "__main__":
    main()
"""
[05/08/13] Challenge #123 [Intermediate] Synchronizing Calendars

https://www.reddit.com/r/dailyprogrammer/comments/1dx3wj/050813_challenge_123_intermediate_synchronizing/

# [](#IntermediateIcon) *(Intermediate)*: Synchronizing Calendars
You're trying to plan out your family's Easter dinners for the next few centuries.
Your grandparents use the Lunar calendar, but your parents use the Julian calender, so you only have dinner with your
grandparents when the calendars synchronize.
To help you figure that out, you're going to need to compute when M Julian years has the same amount of days as N Lunar
months. As it turns out, these calendars synchronize with cycles of certain numbers of years.
**Some information you will need:**
* The time between full moons is 29.53059 days, so that is the length of one Lunar month.
* A Julian year is 365 days for three years, the fourth year is a leap year of 366 days, and then the cycle repeats.
* When taking the days in a number of Lunar months, you will likely get a decimal answer. _Round to the nearest day._
*Author: Zamarok*
# Formal Inputs & Outputs
## Input Description
You will be given two numbers `(M, N)`, where  
`M` is the number of Julian years, and  
`N` is the number of Lunar months.
You need to confirm that the number of days in `M` Julian years is equal to the number of days in `N` Lunar months.
## Output Description
You will take `M` and `N` and discover if the calendars synchronize after `M` Julian years and `N` Lunar months.
When looking at how many days `N` Lunar months will have, round to the nearest day.
If they do synchronize with the given input, print out the number of days that will pass before this occurs.
If the calendars don't synchronize with the given input, print `0`.
# Sample Inputs & Outputs
## Sample Input
    38, 470
## Sample Output
13879
# Challenge Input
    114, 2664
    30, 82
## Challenge Input Solution
    41638
    0
# Note
This was a problem in my homework for an astronomy class. I decided to code a solution to generate solutions, rather
than figuring out it by hand. Turned out to be a good problem to solve, and I learned a bunch while doing it. It's
difficult enough to provide a good challenge and to make you think about how to approach the problem from different
angles.
Let me know if anyone wants to see the original homework assignment, or my solution (about 5 lines of Haskell).
# Extra Credit (optional):
Right now your program just confirms when the calendars will synchronize. You can modify your program to generate `(M,
N)` to sequentially discover solutions. Find the largest solution for `M` where `M` is less than `500`.
For even more extra credit, point out the number of years that it takes for one cycle, a cycle being the time between
when these calendars synchronize. There are multiple correct answers here.
				
"""


def main():
    pass


if __name__ == "__main__":
    main()
