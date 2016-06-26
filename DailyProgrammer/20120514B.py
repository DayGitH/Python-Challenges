"""
After years of study, scientists have discovered an alien language transmitted from a faraway planet. The alien
language is very unique in that every word consists of exactly L lowercase letters. Also, there are exactly D words in
this language.

Once the dictionary of all the words in the alien language was built, the next breakthrough was to discover that the
aliens have been transmitting messages to Earth for the past decade. Unfortunately, these signals are weakened due to
the distance between our two planets and some of the words may be misinterpreted. In order to help them decipher these
messages, the scientists have asked you to devise an algorithm that will determine the number of possible
interpretations for a given pattern.

A pattern consists of exactly L tokens. Each token is either a single lowercase letter (the scientists are very sure
that this is the letter) or a group of unique lowercase letters surrounded by parenthesis ( and ). For example:
(ab)d(dc) means the first letter is either a or b, the second letter is definitely d and the last letter is either d or
c. Therefore, the pattern (ab)d(dc) can stand for either one of these 4 possibilities: add, adc, bdd, bdc.

Please note that sample i/p and o/p is given in the link below
Link [https://code.google.com/codejam/contest/90101/dashboard#s=p0]
"""


def extract(d):
    L = int(d[0])
    D = int(d[1])
    N = int(d[2])
    d = d[3:]

    w_list = d[:D]
    inp = d[D:]

    return L, D, N, w_list, inp


def separate(l):
    """
    Sweeps through l from left to right and separates the format into a list of three.

    If parens found, goes into collection mode before adding to result list
    """
    tmp = ''
    res = []
    coll = False
    for i in l:
        # Collection mode enable/disable
        if i == '(':
            coll = True
            tmp = ''
            continue
        elif i == ')':
            coll = False
            res.append(tmp)
            continue

        # if collection mode, add to temp, else directly append to result list
        if coll:
            tmp += i
        else:
            res.append(i)
    return res


def compare(len, i_list, w_list):
    n = 0
    for w in w_list:
        for m in range(len):
            if w[m] not in i_list[m]:
                break
        else:
            n += 1
    return n


def main():
    with open('A-large-practice.in') as f:
        data = f.read().split()

    L, D, N, w_list, inp = extract(data)

    for n, i in enumerate(inp):
        inp[n] = separate(i)
        out = compare(L, inp[n], w_list)
        print('Case #{}: {}'.format(n+1, out))

if __name__ == "__main__":
    main()
