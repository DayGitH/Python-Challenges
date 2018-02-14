"""
[Weekly #23] Computational Complexity and Algorithm Design

https://www.reddit.com/r/dailyprogrammer/comments/36iufn/weekly_23_computational_complexity_and_algorithm/

# [](#WeeklyIcon) Dynamic Programming and Algorithm Design
Programming is fundamentally tied to computer science, which involves the design and optimization of algorithms to
solve certain problems. In the world of "big data", tweaking and streamlining algorithms to work as quickly as possible
is an important process in designing an algorithm, especially over large, inter-connected data sets.
A set of notations usually referred to as [**big-O notation**](http://en.wikipedia.org/wiki/Big_O_notation), so named
for the big letter O which is a core component of the notation (believe it or not). This notation describes how the
processing time and working space grows, as the size of the input data set grows. For example, if an algorithm runs in
O(*f*(n)) time, then the running time of the algorithm with respect to input size n grows no quicker than *f*(n),
ignoring any constant multiples.
An example of this is sorting data (there's a [pre-existing Weekly thread just on sorting
here](http://www.reddit.com/r/dailyprogrammer/comments/2emixb/)). The simple naïve algorithms for sorting typically run
in O(n^(2)) time in the worst-case scenario. This includes algorithms such as insertion sort. However, a bit of clever
thinking allowed algorithms such as quick-sort to be developed, which uses a [divide and
conquer](http://en.wikibooks.org/wiki/Algorithms/Divide_and_Conquer) approach to make the process simpler, thereby
reducing the time complexity to O(n log n) - which runs much faster when your data to be sorted is large.
We've recently had a spate of challenges which require a bit of algorithm design, so unbeknownst to you, you've already
done some of this work. The specific challenges are these five; check them out if you've not already:
* [[Hard] Unpacking a Sentence in a
Box](http://www.reddit.com/r/dailyprogrammer/comments/322hh0/20150410_challenge_209_hard_unpacking_a_sentence/)
* [[Intermediate] The Lazy Typist](http://www.reddit.com/r/dailyprogrammer/comments/351b0o/)
* [[Hard] Stepstring discrepancy](http://www.reddit.com/r/dailyprogrammer/comments/358pfk/)
* [[Intermediate] Pile of Paper](http://www.reddit.com/r/dailyprogrammer/comments/35s2ds/)
* [[Hard] Chester, the greedy Pomeranian](http://www.reddit.com/r/dailyprogrammer/comments/3629st/)
If you write an inefficient algorithm to solve these challenges, it might take forever to complete!
Techniques such as dynamic programming study algorithms, and specifically those that break problems down into
easier-to-solve sub-problems which can be solved quicker individually than as a whole. There's also a certain class of
problems (NP) for which you physically can't solve efficiently using this approach; this includes problems such as the
infamous [travelling salesman problem](http://mathworld.wolfram.com/TravelingSalesmanProblem.html) and [boolean
3-SAT](http://math.stackexchange.com/questions/86210/what-is-the-3sat-problem), for which no exact efficient solution
has been found; and indeed [probably won't be found](http://www.claymath.org/millenium-problems/p-vs-np-problem).
In today's Weekly discussion, discuss anything that interests you, or that you know of, relating to algorithm design,
or any interesting algorithmic approaches you took to solving any particular DailyProgrammer challenge set to date!
### Challenge Solution Order
In yesterday's challenge, we trialled ordering the solution submissions by *new* rather than by *best*. What are your
opinions on this? How did you think it went? Should we make this the norm?
### IRC
We have an [IRC channel on Freenode](http://www.reddit.com/r/dailyprogrammer/comments/2dtqr7/), at
**#reddit-dailyprogrammer**. Join the channel and lurk with us!
### Previously...
The previous weekly thread was [**Machine Learning**](http://www.reddit.com/r/dailyprogrammer/comments/3206mk/).
"""


def main():
    pass


if __name__ == "__main__":
    main()
