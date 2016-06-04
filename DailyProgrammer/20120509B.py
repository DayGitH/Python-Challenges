"""
Given an absolute path, write a program that outputs an ASCII tree of that directory.
Example output here: HERE [http://www.acooke.org/cute/UnixComman0.html]

Note: 'tree' utility is not allowed.

Extra credit: Limit the depth of the tree by variable n.
Thanks to jnaranjo for the challenge at /r/dailyprogrammer_ideas
"""

import os
import sys

PATH = "C:\Active\Python"


def change_path(p):
    try:
        os.chdir(p)
    except WindowsError:
        print('bad path')
        sys.exit()


def tree(p, lim, n=0):
    for i in os.listdir(p):
        if i.startswith('.'):
            continue

        print(' '*n + '+ ' + i)
        if os.path.isdir(p+'\\'+i) and n < lim:
            tree(p+'\\'+i, lim, n+1)


def main():
    change_path(PATH)
    tree(PATH, 1)

if __name__ == "__main__":
    main()
