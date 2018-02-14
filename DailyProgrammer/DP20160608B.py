"""
[2016-06-08] Challenge #270 [Intermediate] Generating Text with Markov Processes

https://www.reddit.com/r/dailyprogrammer/comments/4n6hc2/20160608_challenge_270_intermediate_generating/

# Description
Text generation algorithms exist in a wide variety of formats, including "Mad Libs" and Markov processes. A Markov
chain algorithm generates text by creating a statistical model of potential textual suffixes for a given prefix. That's
a fancy way of saying "it basically determines the next most probable word given the training set." Markov chain
programs typically do this by breaking the input text into a series of words, then by sliding along them in some fixed
sized window, storing the first N-1 words as a prefix and then the Nth word as a member of a set to choose from
randomly for the suffix. Then, given a prefix, pick randomly from the suffixes to make the next piece of the chain. 
Take this example text:
    Now is not the time for desert, now is the time for dinner 
For a set of triples, yielding a bi-gram (2 word) prefix, we will generate the following prefixes and suffix:
    Prefixes        Suffixes
    --------        --------
    Now, is         not
    is, not         the
    not, the        time
    the, time       for
    time, for       desert
    for, desert     now
    desert, now     is
    now, is         not, the  
    is, the         time
    the, time       for
    time, for       desert, dinner
You'll see a couple of the prefixes have TWO suffixes, this is because they repeat but one with a different suffix and
one with the same suffix. Repeating this over piles and piles of text will start to enable you to build statistically
real but logically meaningless sentences. Take this example output from my program after running it over Star Trek plot
summaries:
    "attack." In fact, Yeoman Tamura's tricorder shows that Kirk has been killed after
    beaming down to the bridge, Kirk reminisces about having time to beam down. Kirk wants
    Spock to grab hold of him in a fist fight with Kirk and Spock try to escape, the collars
    are activated, subjecting them to an entrance, which then opens. Scotty saves the day by
    pretending to help Spock, and Mullhall voluntarily agree, and the others transported to
    the one which is not at all obvious what to make diplomatic advances. Meanwhile Kirk is
    able to get inside. McCoy and nerve pinches Chief at
# Challenge
Your challenge today is to implement a Markov generator supporting a bi-gram prefix. It should be capable of ingesting
a body of text for training and output a body of text generated from that. 
# Notes
[Markov Chain
Algorithm](http://www.rose-hulman.edu/Users/faculty/young/CS-Classes/csse220/200820/web/Programs/Markov/markov.html)
from rose-hulman.edu
If you want to reproduce my Star Trek fun, I extracted the summaries from [Eric Wasserman's
site](http://www.ericweisstein.com/fun/startrek/) and made them into a [flat text
file](https://drive.google.com/file/d/0B3rX15hRO_71NEt0cl8tcWMxNnM/view?usp=sharing). 
"""


def main():
    pass


if __name__ == "__main__":
    main()
