"""
[2017-06-24] Challenge #320 [Hard] Path to Philosophy

https://www.reddit.com/r/dailyprogrammer/comments/6j7k3x/20170624_challenge_320_hard_path_to_philosophy/

#Description
Clicking on the first link in the main text of a Wikipedia article not in parentheses, and then repeating the process
for subsequent articles, usually eventually gets you to the Philosophy article. As of May 26, 2011, 94.52% of all
articles in Wikipedia lead eventually to the article Philosophy. The rest lead to an article with no wikilinks or with
links to pages that do not exist, or get stuck in loops. 
[Here's a youtube video demonstrating this phenomenon.](http://www.youtube.com/watch?v=vehDe2lSptU) 
Your goal is to write a program that will find the path from a given article to the Philosophy article by following the
first link (not in parentheses) in the main text of the given article.
#Formal Inputs & Outputs
##Input description
The program should take in a string containing a valid title of a Wikipedia article.
##Output description
Your program must print out each article in the path from the given article to
[Philosophy](http://en.wikipedia.org/wiki/Philosophy).
##Sample Inputs & Outputs
**Input**
    Molecule
**Output**
    Molecule 
    Atom 
    Matter 
    Invariant mass 
    Energy 
    Kinetic energy 
    Physics 
    Natural philosophy 
    Philosophy 
## Challenge Input
    Telephone
**Solution to challenge input**
    Telephone
    Telecommunication
    Transmission (telecommunications)
    Analog signal
    Continuous function
    Mathematics
    Quantity
    Property (philosophy)
    Logic
    Reason
    Consciousness
    Subjectivity
    Subject (philosophy)
    Philosophy
#Notes/Hints
To start you can go to the url `http://en.wikipedia.org/wiki/{subject}`.
The title of the page that you are on can be found in the element `firstHeading` and the content of the page can be
found in `bodyContent`.
#Bonus 1
Cycle detection: Detect when you visit an already visited page.
#Bonus 2
Shortest path detection: Visit, preferably in parallel, all the links in the content to find the shortest path to
Philosophy
#Finally
Have a good challenge idea, like /u/nagasgura did?
Consider submitting it to /r/dailyprogrammer_ideas.
Oh and please don't go trolling and changing the wiki pages just for this challenge 
"""


def main():
    pass


if __name__ == "__main__":
    main()
