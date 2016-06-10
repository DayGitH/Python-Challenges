"""
Your task is to write functions that encrypt and decrypt using the solitaire cipher
[http://www.schneier.com/solitaire.html]
"""

import numpy.random as nprnd
import copy
import itertools


def divider(l, div):
    l = l.replace(' ', '')
    res = []
    tmp = ''
    for n, i in enumerate(l):
        if n % div == 0:
            res.append(tmp)
            tmp = i
        else:
            tmp += i
    res.append(tmp)
    res = list(filter(None, res))
    res[-1] = res[-1].ljust(div, 'X')
    return res


def gen_keystream(length, deck, div):
    state = 1
    res = ''
    for n in range(length):
        while state != 10:
            if state == 1:
                # move joker A
                index = deck.index('JA')
                if index == len(deck)-1:
                    deck.insert(1, deck.pop(index))
                else:
                    deck.insert(index+1, deck.pop(index))
                state = 2
            elif state == 2:
                # move joker B
                index = deck.index('JB')
                if index == len(deck) - 1:
                    deck.insert(2, deck.pop(index))
                elif index == len(deck) - 2:
                    deck.insert(1, deck.pop(index))
                else:
                    deck.insert(index + 2, deck.pop(index))
                state = 3
            elif state == 3:
                # triple cut
                index1 = deck.index('JA')
                index2 = deck.index('JB')
                if index1 > index2:
                    index1, index2 = index2, index1

                deck = deck[index2+1:] + deck[index1:index2+1] + deck[:index1]
                state = 4
            elif state == 4:
                # count cut
                value = card_value(deck[-1])-1
                deck = deck[value:-1] + deck[:value] + [deck[-1]]
                state = 5
            elif state == 5:
                # get output card
                value = card_value(deck[0])
                output = deck[value-1+1] # -1 for 0 indexing of list and +1 because we need to pick the card after this1
                if output[0] == 'J':
                    state = 1
                else:
                    state = 6
            elif state == 6:
                # get letter from output card
                letter = card_value(output)%26 + 65
                res += chr(letter)
                state = 10
        state = 1
    return divider(res, div)


def card_value(card):
    suite_dict = {'C': 0, 'D': 13, 'H': 26, 'S': 39}
    card_dict = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
    if card[0] == 'J':
        return 53
    res = suite_dict[card[0]]
    try:
        res += card_dict[card[1]]
    except KeyError:
        res += int(card[1])
    return res


def letter2num(word):
    return [ord(w)-64 for w in ''.join(word)]


def main():
    inp = 'DO NOT USE PC'
    div = 5
    deck = ['CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK',
            'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK',
            'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK',
            'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK',
            'JA', 'JB']

    nprnd.shuffle(deck)
    print(deck)

    # encryption
    print('encoding')
    split_list = divider(inp, div)
    keystream = gen_keystream(len(''.join(split_list)), copy.deepcopy(deck), div)
    print(split_list, keystream)
    inp_num = letter2num(split_list)
    key_num = letter2num(keystream)
    encode_num = [(x+y)%26 for x,y in zip(inp_num, key_num)]
    encode_num = [26 if x==0 else x for x in encode_num]
    encoded = divider(''.join([chr(x+64) for x in encode_num]), div)
    print(encoded)

    print('')
    # decryption
    print('decoding')
    keystream = gen_keystream(len(''.join(encoded)), copy.deepcopy(deck), div)
    print(encoded, keystream)
    inp_num = letter2num(encoded)
    key_num = letter2num(keystream)
    decode_num = [(x-y)%26 for x,y in zip(inp_num, key_num)]
    decode_num = [26 if x==0 else x for x in decode_num]
    decoded = divider(''.join([chr(x+64) for x in decode_num]), div)
    print(decoded)

if __name__ == "__main__":
    main()
