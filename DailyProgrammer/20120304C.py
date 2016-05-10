"""
build a tic tac toe game with opponent AI
bonus points for cooler AI implementations (depth/breadth first search, neural network, etc)
"""

import random

class perfectPlayer():
    def __init__(self, AI_turn, h_turn):
        self.arr = [[' ' for a in range(3)] for b in range(3)]
        self.AI_turn = AI_turn
        self.h_turn = h_turn

    def score(self, array, depth):
        if complete_win(array) == AI_turn:
            return 10 - depth
        elif complete_win(array) == h_turn:
            return depth - 10
        else:
            return 0

    def minimax(self, array, depth):
        over_score = -100
        move = 0
        # win or lose
        test = complete_win(array)
        if complete_win(array) == self.AI_turn:
            return [10 - depth, move]
        elif complete_win(array) == self.h_turn:
            return [depth - 10, move]
        # elif complete_win(array) == '':
        #     return [0, move]

        empty_list = []
        for a in range(len(array)):
            for b in range(len(array[a])):
                if array[a][b] == ' ':
                    empty_list.append((a * 3) + b + 1)

        #draw
        if not empty_list:
            return [0, move]

        for cell in empty_list:
            working_arr = unshared_copy(array)
            # working_arr = original_arr[:]
            # working_arr = player(array, cell)
            inp_turn = self.AI_turn if depth % 2 == 0 else self.h_turn
            working_arr = enter_play(working_arr, cell, inp_turn)
            score = self.minimax(working_arr, depth + 1)[0]

            if over_score == -100:
                over_score = score
                move = cell
            elif (depth % 2 == 0) and score > over_score:
                over_score = score
                move = cell
            elif (depth % 2 == 1) and score < over_score:
                over_score = score
                move = cell

        return [over_score, move]
        #
        # score = self.score(working_arr, depth)
        # if score != 0:
        #     return score
        # elif empty_list:
        #     return minimax(working_arr, depth + 1)

        # if not empty_list and self.score(array, depth) == 0:
        #     return 0
        #
        #
        #


def unshared_copy(inList):
    if isinstance(inList, list):
        return list( map(unshared_copy, inList) )
    return inList

def ai_easy(inp_arr, inp_turn):
    work_arr = inp_arr
    while True:
        ai_play = int(random.choice(range(9))) + 1
        try:
            work_arr = enter_play(inp_arr, ai_play, inp_turn)
            break
        except:
            # silently try again
            pass

    return work_arr


def player(inp_arr, inp_turn):
    work_arr = inp_arr
    while True:
        try:
            player = int(input('Enter player choice: '))
            work_arr = enter_play(inp_arr, player, inp_turn)
            break
        except:
            print('Already occupied. Please try again')

    return work_arr


def enter_play(inp_arr, number, symbol):
    work_arr = inp_arr
    if inp_arr[(number - 1) // 3][(number - 1) % 3] == ' ':
        work_arr[(number - 1) // 3][(number - 1) % 3] = symbol
    else:
        raise NameError('Occupied')
    return work_arr


def complete_win(inp_arr):
    for a in inp_arr:
        if all(x == a[0] for x in a):
            return a[0]

    # transposed inp_arr
    for a in zip(*inp_arr):
        if all(x == a[0] for x in a):
            return a[0]

    # checking diagonals
    if inp_arr[1][1] == inp_arr[0][0] and inp_arr[1][1] == inp_arr[2][2]:
        return inp_arr[1][1]
    if inp_arr[1][1] == inp_arr[0][2] and inp_arr[1][1] == inp_arr[2][0]:
        return inp_arr[1][1]

    check_num = 0
    for row in inp_arr:
        for x in row:
            if x == ' ':
                check_num += 1

    if check_num == 0:
        return 'q'

    return ''

arr = [[' ' for a in range(3)] for b in range(3)]
# arr = [[' ', 'x', ' '], [' ', ' ', 'x'], ['o', 'o', 'x']]


# print(p.minimax(arr, 0))

turn = ['o', 'x']
random.shuffle(turn)
print('Player is \'{}\''.format(turn[0]))

while True:
    difficulty = input('Difficulty? (e)asy or (h)ard').lower()
    if difficulty in ['e', 'h']:
        break
    else:
        print('try again')

if turn[0] == 'o':
    arr = ai_easy(arr, 'x')

for row in arr:
    print(row)

if difficulty == 'h':
    p = perfectPlayer('x', 'o')

while True:
    arr = player(arr, turn[0])
    if difficulty == 'e':
        arr = ai_easy(arr, turn[1])
    elif difficulty == 'h':
        move = p.minimax(arr, 0)[1]
        if move != 0:
            work_arr = enter_play(arr, move, turn[1])

    check = complete_win(arr)

    for row in arr:
        print(row)

    if check == turn[0]:
        print('Player wins!')
        break
    elif check == turn[1]:
        print('AI wins!')
        break
    elif check == 'q':
        print('Draw')
        break