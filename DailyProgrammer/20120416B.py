"""
Write a program that computes the Kaprekar chain [http://mathworld.wolfram.com/KaprekarRoutine.html] for a given
starting number, and compute the longest possible Kaprekar chain [http://mathworld.wolfram.com/KaprekarRoutine.html]
"""

# inp = input('> ')

inp = "2801"

old_inp = ""
while inp != old_inp:
    print(inp)
    desc = ''.join(sorted(inp, reverse=True))
    asc = ''.join(sorted(inp))

    inp, old_inp = str(int(desc) - int(asc)), inp


print('Done')
