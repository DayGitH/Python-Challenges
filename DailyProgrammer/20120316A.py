"""
you have a string "ddaaiillyypprrooggrraammeerr". We want to remove all the consecutive duplicates and put them in a
separate string, which yields two separate instances of the string "dailyprogramer".
use this list for testing:

input: "balloons"
expected output: "balons" "lo"
input: "ddaaiillyypprrooggrraammeerr"
expected output: "dailyprogramer" "dailyprogramer"
input: "aabbccddeded"
expected output: "abcdeded" "abcd"
input: "flabby aapples"
expected output: "flaby aples" "bap"
"""

inp = "ddaaiillyypprrooggrraammeerr"
org = ""
extra = ""
hold = ""

for a in range(len(inp)):
    if hold == inp[a]:
        extra += inp[a]
    else:
        org += inp[a]
        hold = inp[a]

print("original:\t", inp)
print("first:\t\t", org)
print("repeats:\t", extra)