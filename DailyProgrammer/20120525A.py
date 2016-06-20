"""
Your task is to implement Ackermann Function in the most efficient way possible.
Please refer the wiki page link given for its explanation.

-------------------------------------------------------------------------------------------------------

Since many did not like the previous challenge because it was quite unsatisfactory here is a new challenge ...
Input: A sequence of integers either +ve or -ve
Output : a part of the sequence in the list with the maximum sum.

UPDATE: I have given some more info on the [difficult] challenge since it seems to be very tough. you have upto monday
to finish all these challenges. pls note it :)
"""

import numpy.random as nprnd
import copy


def A(m, n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return A(m-1, 1)
    elif m > 0 and n > 0:
        return A(m-1, A(m, n-1))
    else:
        return None


def maxarray(sq):
    print(sq)

    max_end = 0
    end_list = []

    max_sofar = 0
    sofar_list = []

    for a in sq:
        if max_end+a > 0:
            max_end = max_end + a
            end_list.append(a)
        else:
            max_end = 0
            end_list = []

        if max_end > max_sofar:
            max_sofar = max_end
            sofar_list = copy.deepcopy(end_list)

    return max_sofar, sofar_list


def main():
    # print(A(1,2))

    seq = list(nprnd.randint(-25, 25, size=100))
    m = maxarray(seq)
    print('list: {}\nsum: {}'.format(m[1], m[0]))


if __name__ == "__main__":
    main()
