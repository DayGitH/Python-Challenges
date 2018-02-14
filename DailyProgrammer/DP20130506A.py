"""
[05/06/13] Challenge #124 [Easy] Edge Sorting

https://www.reddit.com/r/dailyprogrammer/comments/1dsyrk/050613_challenge_124_easy_edge_sorting/

# [](#EasyIcon) *(Easy)*: Edge Sorting
In [graph theory](http://en.wikipedia.org/wiki/Graph_theory), an "edge" is defined as the connection between two
vertices. For example, if we look at the [sample graph](http://en.wikipedia.org/wiki/File:6n-graf.svg) on the Wikipedia
article, we would define the relationship between vertex 4 and 6 as having an edge, but vertices 5 and 3 have no edge
(though they are connected, through {5,4,3} or {5,2,3,} and a few others)
Your goal is to sort a given list of edges in the correct connection-order: to make your job even easier, given edges
will always form one big long line (so basically a very simplified graph, [like this](http://i.imgur.com/KXc00a2.png)
). Lower index integers should be on the left / top of the sorted list, while larger index integers should be on the
right / bottom of the sorted list. All edges are assigned a unique letter to help keep track of ordering.
*Author: nint22*
# Formal Inputs & Outputs
## Input Description
On standard input, you will first be given an integer, which is the number of edges you will then be given. Each given
edge is defined by a letter and two integers: the letter will always be unique and represents the edge. The integers
are the actual edge's vertices, and thus may be duplicate (if a vertex is shared between two edges).
## Output Description
Simply list the sorted edges from the left-most ordered edge to the right-most ordered edge.
# Sample Inputs & Outputs
## Sample Input
The following data is a simple example, with valid output following the next section:
    4
    A 3 4
    B 4 5
    C 1 2
    D 2 3
## Sample Output
    C D A B
# Challenge Input
This is an example of a randomized input:
    6
    F 2 3
    B 1 2
    D 6 5
    C 6 7
    E 5 4
    A 3 4
## Challenge Input Solution
None required.
# Note
None
"""


def main():
    pass


if __name__ == "__main__":
    main()
"""
[05/06/13] Challenge #124 [Easy] New-Line Troubles

https://www.reddit.com/r/dailyprogrammer/comments/1ds3sn/050613_challenge_124_easy_newline_troubles/

# [](#EasyIcon) *(Easy)*: New-Line Troubles
A [newline character](http://en.wikipedia.org/wiki/Newline) is a special character in text for computers: though it is
not a visual (e.g. renderable) character, it is a control character, informing the reader (whatever program that is)
that the following text should be on a new line (hence "newline character").
As is the case with many computer standards, newline characters (and their rendering behavior) were not uniform across
systems until much later. Some character-encoding standards (such as [ASCII](http://en.wikipedia.org/wiki/ASCII)) would
encode the character as hex 0x0A (dec. 10), while [Unicode](http://en.wikipedia.org/wiki/Unicode) has a handful of
subtly-different newline characters. Some systems even define newline characters as a set of characters: Windows-style
new-line is done through two bytes: CR+LF (carriage-return and then the ASCII newline character).
Your goal is to read ASCII-encoding text files and "fix" them for the encoding you want. You may be given a
Windows-style text file that you want to convert to UNIX-style, or vice-versa.
*Author: nint22*
# Formal Inputs & Outputs
## Input Description
On standard input, you will be given two strings in quotes: the first will be the text file location, with the second
being which format you want it output to. Note that this second string will always either be "Windows" or "Unix".
Windows line endings will always be CR+LF (carriage-return and then newline), while Unix endings will always be just
the LF (newline character).
## Output Description
Simply echo the text file read back off onto standard output, with all line endings corrected.
# Sample Inputs & Outputs
## Sample Input
The following runs your program with the two arguments in the required quoted-strings.
    ./your_program.exe "/Users/nint22/WindowsFile.txt" "Unix"
## Sample Output
The example output should be the contents of the WindowsFile.txt file, sans CR+LF characters, but just LF.
# Challenge Input
None required.
## Challenge Input Solution
None required.
# Note
None
				
"""


def main():
    pass


if __name__ == "__main__":
    main()
