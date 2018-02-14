"""
[2016-09-02] Challenge #281 [Hard] Minesweeper Solver

https://www.reddit.com/r/dailyprogrammer/comments/50s3ax/20160902_challenge_281_hard_minesweeper_solver/

#Description
In this challenge you will come up with an algorithm to solve the classic game of
[Minesweeper](http://minesweeperonline.com/).
The brute force approach is impractical since the search space size is anywhere around 10^20 to 10^100 depending on the
situation, you'll have to come up with something clever.
#Formal Inputs & Outputs
##Input description
The current field state where each character represents one field. Flags will not be used. 
Hidden/unknown fields are denoted with a '?'.   
'Zero-fields' with no mines around are denoted with a space.
Example for a 9x9 board:
        1????
        1????
        111??
          1??
    1211  1??
    ???21 1??
    ????211??
    ?????????
    ?????????
##Output description
A list of zero-based row and column coordinates for the fields that you have determined to be **SAFE**. For the above
input example this would be:
    0 5
    1 6
    1 7
    2 7
    3 7
    5 1
    5 7
    6 2
    6 7
The list does not need to be ordered.
##Challenge input
As suggested by /u/wutaki, this input is a greater challenge then the original input
    ??????
    ???2??
    ???4??
    ?2??2?
    ?2222?
    ?1  1?
#Notes/Hints
If you have no idea where to start I suggest you play the game for a while and try to formalize your strategy.
Minesweeper is a game of both logic and luck. [Sometimes it is impossible](http://i.imgur.com/yLhxzrl.jpg) to find free
fields through logic. The right output would then be an empty list. Your algorithm does not need to guess.
#Bonus
Extra hard mode: Make a closed-loop bot. It should take a screenshot, parse the board state from the pixels, run the
algorithm and manipulate the cursor to execute the clicks.
*Note: If this idea is selected for submission I'll be able to provide lots of input/output examples using my own
solution.*
#Finally
Have a good challenge idea like /u/janismac did?
Consider submitting it to /r/dailyprogrammer_ideas
"""


def main():
    pass


if __name__ == "__main__":
    main()
