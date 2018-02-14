"""
[2017-08-25] Challenge #328 [Hard] Subset Sum Automata

https://www.reddit.com/r/dailyprogrammer/comments/6vyihu/20170825_challenge_328_hard_subset_sum_automata/

# Description
Earlier this year we did the [subset
sum](https://www.reddit.com/r/dailyprogrammer/comments/68oda5/20170501_challenge_313_easy_subset_sum/) problem wherein
given a sequence of integers, can you find any subset that sums to 0. Today, inspired by [this
post](https://thquinn.github.io/projects/automaton.html) let's play subset sum automata. It marries the subset sum
problem with [Conway's Game of
Life](https://www.reddit.com/r/dailyprogrammer/comments/271xyp/622014_challenge_165_easy_ascii_game_of_life/). 
You begin with a board full of random integers in each cell. Cells will increment or decrement based on a simple
application of the subset sum problem: if any subset of the 8 neighboring cells can sum to the target value, you
increment the cell's sum by some value; if not, you decrement the cell by that value. Automata are defined with three
integers `x/y/z`, where `x` is the target value, `y` is the reward value, and `z` is the penalty value. 
Your challenge today is to implement the subset automata:
- Create a 2 dimensional board starting with random numbers
- Color the board based on the value of the cell (I suggest some sort of rainbow effect if you can)
- Parse the definition as described above
- Increment or decrement the cell according to the rules described above
- Redraw the board at each iteration
You'll probably want to explore various definitions and see what sorts of interesting patterns emerge. 
"""


def main():
    pass


if __name__ == "__main__":
    main()
