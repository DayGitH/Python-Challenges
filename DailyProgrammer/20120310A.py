"""
Write a program that will compare two lists, and append any elements in the second list that doesn't exist in the first.
input: ["a","b","c",1,4,], ["a", "x", 34, "4"]
output: ["a", "b", "c",1,4,"x",34, "4"]
"""

inp1 = ["a","b","c",1,4,]
inp2 = ["a", "x", 34, "4"]

final = inp1[:]

for a in inp2:
    if a not in final:
        final.append(a)

print(final)