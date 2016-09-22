"""
Write a program that given two strings, finds out if the second string is contained in the first, and if it is, where
it is.

I.e. given the strings "Double, double, toil and trouble" and "il an" will return 18, because the second substring is
embedded in the first, starting on position 18.

NOTE: Pretty much every language have this functionality built in for their strings, sometimes called find() (as in
Python) or indexOf() (as in Java). But the point of this problem is to write the program yourself, so you are not
allowed to use functions like this!
"""

def substring(str1, str2):
    l1 = len(str1)
    l2 = len(str2)

    if l1 < l2:
        return -1

    for i in range(l1-l2):
        if str1[i:i+l2] == str2:
            return i
    return -1


def main():
    str1 = "Double, double, toil and trouble"
    str2 = "il an"

    print(str1.find(str2))

    print(substring(str1, str2))

if __name__ == "__main__":
    main()
