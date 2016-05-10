"""
Enter an integer for the number of iterations, and create a program that prints out a sierpinski triangle.
First 4 iterations as an example [http://i.imgur.com/fjlTg.png]

Thanks to Rinfiyks for the challenge at /r/dailyprogrammer_ideas
"""

"""
inspired by /u/Cosmologicon's solution
"""
def sierpinski(n):
    if n == 1:
        return ['x']
    l = sierpinski(n-1)
    s = ' ' * 2**(n-2)
    return [s + a + s for a in l] + [a + ' ' + a for a in l]

print('\n'.join(sierpinski(7)))