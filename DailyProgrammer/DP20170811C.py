"""
[2017-08-11] Challenge #326 [Hard] Multifaceted alphabet blocks

https://www.reddit.com/r/dailyprogrammer/comments/6t0zua/20170811_challenge_326_hard_multifaceted_alphabet/

# Description
You are constructing a set of N alphabet blocks. The first block has 1 face. The second block has 2 faces, and so on up
to the Nth block, which has N faces. Each face contains a letter.
Given a word list, return a set of blocks that can spell every word on the word list, making N as small as possible. A
word can be spelled with the blocks if you can take some subset of the blocks, take one face from each block you chose,
put them in some order, and spell the word.
# Example input
    zero
    one
    two
    three
    four
    five
    six
    seven
# Example output
The smallest possible N in this case is N = 5:
    e
    eo
    fhs
    rvwx
    intuz
This output represents five blocks. Block #1 has one face that contains `e`, block #2 has two faces, `e` and `o`, and
so on up to block #5, which has the faces `i`, `n`, `t`, `u`, and `z`.
For example, `four` can be formed by using blocks #3, #2, #5, and #4 in order. Note that `ten` could not be formed from
these blocks even though all the letters are there, because the only `t` and the only `n` both appear on block #5, and
you can only use at most one face from each block.
# Challenge input
[This list of 10,000 12-letter words](https://pastebin.com/trMz6nWQ).
I'll award +1 gold medal flair for the best (lowest number of blocks) solution to the challenge input after 7 days. I
will break ties by concatenating the blocks in order of number of faces (`eeofhsrvwxintuz` for the example), and take
the lexicographically first solution.
"""


def main():
    pass


if __name__ == "__main__":
    main()
