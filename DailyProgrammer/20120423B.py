"""
We have it easy nowadays when it comes to numbers. It's so simple to add them and subtract them that we don't even
consider that it wasn't always so. Even multiplication is not that tough! And you can represent very large numbers very
easily, if you want to write down a million, you just write "1000000". That's only seven digits!

It wasn't so easy for the Romans. They had to make due with their clumsy Roman numerals. Think how hard it is to add
Roman numerals together. If you wanted to add XXVIII with LXXXII, you would have to smush them together to form
LXXXXXVIIIII, then you would have to realize that XXXXX is equal to L and IIIII is equal to V, and turn it to LLVV, and
then you'd have to shorten that to CX. Look how much work to just add 28 and 82! And just imagine trying to write a
million with Roman numerals: you'd literally have to write down one thousand copies of M!

But Roman numerals aren't without advantages: they at least look very pretty. I think we can all agree that Rocky V
looks way cooler than Rocky 5.

So in this challenge, we honor the romans. Your task is to write a function that can add together two Roman numerals
supplied as strings. Example: roman_addition("XXVIII", "LXXXII") returns "CX".

The easiest way to do this would obviously be to just to convert the roman numerals to integers and then convert the
sum of those integers back to a Roman numeral. But since the Romans couldn't do that, you can't either! Write the
function so that it performs the task similarly to how it might have been done in ancient Rome, either with the
"smushing together" method I described above, or another method of your choosing (don't worry about efficiency). But
at no point shall you convert the numerals to decimal or binary integers! Imagine if you lived in ancient Rome and
decimal numbers hadn't been invented yet, how would you do it?

The output of this function should as "minimal" as possible. I.e. if the answer is XVII, it should output XVII, not
XIIIIIII or VVVII.

Real Roman numerals sometimes uses a trick to make the numbers shorter: you put a smaller numeral in front of a larger
numeral to represent the difference between the two. So for instance, 4 would be written as "IV", 9 as "IX" or 1949 as
"MCMIL". For the purposes of this problem, lets ignore that. 4 is "IIII", 9 is "VIIII" and 1949 is "MDCCCCXXXXVIIII".
The numbers become longer this way, but it makes much more sense if all the numerals are "in order". Also, the exact
rules for how this trick worked was never rigorous, and changed over time.

For reference, here's the different single numerals and their value:
I = 1
V = 5    = IIIII
X = 10   = VV
L = 50   = XXXXX
C = 100  = LL
D = 500  = CCCCC
M = 1000 = DD
Bonus 1: Write a function that does subtraction. Example: roman_subtraction("CX", "LXXXII") returns "XXVIII"
Bonus 2: Write a function that performs multiplication with Roman numerals, again without ever converting them to
regular integers. Example: roman_multiplication("XVI", "VII") returns "CXII".
"""

sort = {"M": 1,
        "D": 2,
        "C": 3,
        "L": 4,
        "X": 5,
        "V": 6,
        "I": 7
       }

ref1 = {"DD": "M",
        "CCCCC": "D",
        "LL": "C",
        "XXXXX": "L",
        "VV": "X",
        "IIIII": "V"
       }

ref2 = {"CM": "DCCCC",
        "CD": "CCCC",
        "XC": "LXXXX",
        "XL": "XXXX",
        "IX": "VIIII",
        "IV": "IIII"
       }

inp = "XC LXXXII"

inp = inp.split()

for i in range(len(inp)):
    while True:
        old = inp[i]
        for a in ref2:
            inp[i] = inp[i].replace(a, ref2[a])
        if inp[i] == old:
            break

work = sorted(''.join(inp), key=lambda x:sort[x[0]])
out = ''.join(work)

while True:
    old = out
    for a in ref1:
        out = out.replace(a, ref1[a])
    if out == old:
        break
print(out)
