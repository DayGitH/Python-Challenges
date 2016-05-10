"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def is_palindrom(pal):
    '''Assuming six digit number'''
    DIGITS = 6
    front = (pal // 10 ** (DIGITS / 2))
    back = (pal % 10 ** (DIGITS / 2))
    pal = 0
    for i in range(1,1 + int(DIGITS / 2)):
        pal += (back // 10 ** (int(DIGITS / 2) - i)) * (10 ** (i - 1))
        back -= (back // 10 ** (int(DIGITS / 2) - i)) * (10 **  (int(DIGITS / 2) - i))
        
    if front == pal:
        return True
    else:
        return False

def find_palindrom(pal):
    '''Finds the next lower palindrom'''
    p = pal
    while True:
        p -= 1
        if is_palindrom(p):
            return p

def main():
    '''Find the largest palindrome made from the product of two 3-digit numbers.'''
    x = 999999
    for i in range(100):
        for i in range(999,900,-1):
            for j in range(999,900,-1):
                if i * j == x:
                    print('{} * {} = {}'.format(i, j, x))
        x = find_palindrom(x)
        
main()