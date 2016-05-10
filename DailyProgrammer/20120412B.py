"""
Today's challenge is to determine if a number is a Kaprekar Number [http://mathworld.wolfram.com/KaprekarNumber.html]
Enjoy :)
"""

k = 297
sq = str(k**2)
s = int(sq[:int(len(sq)/2)]) + int(sq[int(len(sq)/2):])

print(k == s)
