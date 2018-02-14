"""
[2016-07-06] Challenge #274 [Intermediate] Calculating De Bruijn sequences

https://www.reddit.com/r/dailyprogrammer/comments/4riubi/20160706_challenge_274_intermediate_calculating/

# Description
In combinatorial mathematics, a *k-ary* De Bruijn sequence *B(k, n)* of order *n*, named after the Dutch mathematician
Nicolaas Govert de Bruijn, is a cyclic sequence of a given alphabet *A* with size *k* for which every possible
subsequence of length *n* in *A* appears as a sequence of consecutive characters exactly once. At the terminus, you
"wrap" the end of the sequence around to the beginning to get any remaining subsequences. 
Each *B(k, n)* has length *k^n*.
A De Bruijn sequence *B(2, 3)* (with alphabet *0* and *1*) is therefore:
    00010111
Similarly, *B("abcd", 2)* (with alphabet "a", "b", "c", and "d") is therefore:
    aabacadbbcbdccdd
For those sequences of length, every trigram (for the former case) or bigram (for the latter case) is represented in
the result. 
De Bruijn sequences have various applications, including in PIN pad testing and rotor angle calculation. 
# Input Description
You'll be given two inputs *k* and *n*, the first is an integer or a a string of unique characters, the second is the
length of the subsequences to ensure are encoded.
# Output Description
Your program should emit a string that encodes the De Bruijn sequence.
# Input
    5 3
    2 4
    abcde 4
# Output
The outputs expected for those (in order) are:
   
0001002003004011012013014021022023024031032033034041042043044111211311412212312413213313414214314422232242332342432443334344
    0000100110101111
   
aaaabaaacaaadaaaeaabbaabcaabdaabeaacbaaccaacdaaceaadbaadcaaddaadeaaebaaecaaedaaeeababacabadabaeabbbabbcabbdabbeabcbabccabcdabceabdbabdcabddabdeabebabecabedabeeacacadacaeacbbacbcacbdacbeaccbacccaccdacceacdbacdcacddacdeacebacecacedaceeadadaeadbbadbcadbdadbeadcbadccadcdadceaddbaddcadddaddeadebadecadedadeeaeaebbaebcaebdaebeaecbaeccaecdaeceaedbaedcaeddaedeaeebaeecaeedaeeebbbbcbbbdbbbebbccbbcdbbcebbdcbbddbbdebbecbbedbbeebcbcbdbcbebcccbccdbccebcdcbcddbcdebcecbcedbceebdbdbebdccbdcdbdcebddcbdddbddebdecbdedbdeebebeccbecdbecebedcbeddbedebeecbeedbeeeccccdccceccddccdeccedcceecdcdcecdddcddecdedcdeececeddcedeceedceeeddddeddeededeee
"""


def main():
    pass


if __name__ == "__main__":
    main()
