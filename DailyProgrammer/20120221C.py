"""
Create a rock-paper-scissors program, however, there should be no user input. the computer should play against itself.
Make the program keep score, and for extra credit, give the option to "weigh" the chances,
so one AI will one more often.
"""

import random

BEST_OF = 5


def main():
    moves = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    while True:
        p1_wins = 0
        p2_wins = 0
        i = 0
        while i < BEST_OF:
            p1 = random.choice(list(moves.keys()))
            p2 = random.choice(list(moves.keys()))
            print('P1 throws {}!'.format(p1))
            print('P2 throws {}!'.format(p2))

            if p1 == p2:
                print('draw')
            elif p1 == moves[p2]:
                print('point for P2')
                p2_wins += 1
                i += 1
            elif p2 == moves[p1]:
                print('point for P1')
                p1_wins += 1
                i += 1
            else:
                print('Rework your logic, bozo!')

            if (p1_wins > (BEST_OF / 2)) or (p2_wins > (BEST_OF / 2)):
                break

        print('P1: {}\t0P2: {}'.format(p1_wins, p2_wins))
        if p1_wins > p2_wins:
            print('P1 wins!!!')
        elif p2_wins > p1_wins:
            print('P2 wins!!!')

        if input('Another game (Y/N)?: ').lower() == 'y':
            pass
        else:
            break

if __name__ == '__main__':
    main()
