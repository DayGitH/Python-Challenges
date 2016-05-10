"""
Write a program that will help you play poker by telling you what kind of hand you have.

Input:
The first line of input contains the number of test cases (no more than 20). Each test case consists of one line - five
space separated cards. Each card is represented by a two-letter (or digit) word. The first character is the rank
(A,K,Q,J,T,9,8,7,6,5,4,3 or 2), the second character is the suit (S,H,D,C standing for spades, hearts, diamonds and
clubs). The cards can be in any order (but they will not repeat).

Output:
For each test case output one line describing the type of a hand, exactly like in the list above.
"""


rank = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
suit = ['S', 'H', 'D', 'C']


def validate(val):
    if len(val) != 5:
        return False

    for v in val:
        if v[0] not in rank or v[1] not in suit:
            return False
    return True


def deck_sort(inp):
    d = {'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T': 4, '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12}
    return sorted(inp, key=lambda x: d[x[0]])


def same_suit(inp):
    for i in inp:
        if not i[1] == inp[0][1]:
            return False
    return True


def same_rank(inp):
    for i in inp:
        if i[0] != inp[0][0]:
            return False
    return True


def consecutive(inp):
    nxt = ''
    for i in inp:
        if not nxt:
            nxt = rank.index(i[0]) + 1
        elif rank[nxt] == i[0]:
            nxt = rank.index(i[0]) + 1
        else:
            return False
    return True


def test(inp):
    if royal_flush(inp):
        print('Royal Flush')
    elif straight_flush(inp):
        print('Straight Flush')
    elif four_of_a_kind(inp):
        print('Four of a Kind')
    elif full_house(inp):
        print('Full House')
    elif flush(inp):
        print('Flush')
    elif straight(inp):
        print('Straight')
    elif three_of_a_kind(inp):
        print('Three of a Kind')
    elif two_pair(inp):
        print('Two Pair')
    elif one_pair(inp):
        print('One Pair')
    else:
        print('"High" Card')


def straight_flush(inp):
    return same_suit(inp) and consecutive(inp)


def royal_flush(inp):
    return straight_flush(inp) and inp[0][0] == 'A'


def four_of_a_kind(inp):
    return (same_rank(inp[:4])) or \
           (same_rank(inp[1:]))


def full_house(inp):
    return (same_rank(inp[:3]) and same_rank(inp[3:])) or \
           (same_rank(inp[:2]) and same_rank(inp[2:]))


def flush(inp):
    return same_suit(inp)


def straight(inp):
    return consecutive(inp)


def three_of_a_kind(inp):
    return (same_rank(inp[0:3])) or \
           (same_rank(inp[1:4])) or \
           (same_rank(inp[2:5]))


def two_pair(inp):
    return (same_rank(inp[0:2]) and same_rank(inp[2:4])) or \
           (same_rank(inp[0:2]) and same_rank(inp[3:5])) or \
           (same_rank(inp[1:3]) and same_rank(inp[3:5]))


def one_pair(inp):
    return (same_rank(inp[0:2])) or \
           (same_rank(inp[1:3])) or \
           (same_rank(inp[2:4])) or \
           (same_rank(inp[3:5]))


if __name__ == '__main__':
    number = int(input('Number of inputs: '))

    print('Please enter combinations: ')
    for i in range(number):
        cards = input('> ').upper().split()
        if validate(cards):
            test(deck_sort(cards))
        else:
            print('invalid input')
