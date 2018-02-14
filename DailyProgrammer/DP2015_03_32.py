"""
[2015-03-32] Challenge 208 [Bonus] The Infinite Stallman Theorem

https://www.reddit.com/r/dailyprogrammer/comments/310525/20150332_challenge_208_bonus_the_infinite/

# [](#BonusIcon) _(Bonus)_: The Infinite Stallman Theorem
Loosely, the [*infinite monkey theorem*](http://en.wikipedia.org/wiki/Infinite_monkey_theorem) states that, given an
infinite number of monkeys randomly typing at typewriters for an unbounded amount of time, one will eventually produce
a work of Shakespeare from start to finish. After the Japanese government performed this thought experiment using an
infinitely-nested fractal pocket dimension with some success in 2007 (despite the incident with the micro black holes),
application of the theorem has had some practical value in the field of [software
optimization](http://en.wikipedia.org/wiki/Program_optimization).
Human-developed programs often suffer from performance issues, such as the during the compilation of large programs.
Even today's compilers, such as the GNU Compiler Collection or Clang, take a non-trivial amount of time to compile
complex systems. Partly, this boils down to limitations of human thought process when designing the architecture of
such systems. This problem can be alleviated by randomly-generating the program instead, using the theorem described
above. This is known as using an **evolutionary algorithm**, named by Charles Darwin who produced the first
artifically-generated Smalltalk compiler in 1866.
Today, your challenge is to randomly generate a C++ compiler, by simulating a monkey entering random characters on a
typewriter, and testing the resulting source code. The randomly-generated compiler can be implemented in a language of
your choice.
# Formal Inputs and Outputs
## Input Description
The input to this challenge consists of a single line, describing the C++ standard which the generated compiler should
accept. This can consist of any of the following strings:
* `c++98` for the C++98 standard.
* `c++03` for the 2003 revision of the C++98 standard.
* `c++11` for the C++11 standard (previously known as C++0x).
* `c++14` for the 2014 revision of the C++11 standard.
## Output Description
You are to output a tarball of the source of a randomly-generated C++ compiler, compliant to the standard provided as
input to the challenge.
# Sample Inputs and Outputs
## Sample Input
    c++14
# Notes
Got any cool challenge ideas? Submit them to /r/DailyProgrammer_Ideas!
"""


def main():
    pass


if __name__ == "__main__":
    main()
