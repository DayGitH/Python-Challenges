"""
Write a program that will accept a sentence as input and then output that sentence surrounded by some type of an ASCII decoratoin banner.
Sample run:
Enter a sentence: So long and thanks for all the fish
Output
*****************************************
*                                       *
*  So long and thanks for all the fish  *
*                                       *
*****************************************
Bonus: If the sentence is too long, move words to the next line.
"""


def chunks(inp, n):
    i = 0
    chunks = []
    length = len(inp)

    while i < length:
        w = inp[i:i+n]
        if len(w) == n and inp[i+n] != ' ':
            ind = w.rfind(' ')
            s = inp[i:i+ind+1].strip().ljust(n)
            chunks.append(s)
            i += ind
        else:
            chunks.append(w.strip().ljust(n))
            i += n
    return chunks

inp = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

n = 96

l = chunks(inp, n)

if len(l) == 1:
    l[0] = l[0].strip()
    n = len(l[0].strip())

print('*' * (n+4))
print('* {} *'.format(' ' * n))

for a in l:
    print('* {} *'.format(a))

print('* {} *'.format(' ' * n))
print('*' * (n+4))
