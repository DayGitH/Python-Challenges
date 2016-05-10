"""
Input: list of elements and a block size k or some other variable of your choice
Output: return the list of elements with every block of k elements reversed, starting from the beginning of the list.
For instance, given the list 12, 24, 32, 44, 55, 66 and the block size 2, the result is 24, 12, 44, 32, 66, 55.
"""


def main():
    block_size = 7
    working_list = [12, 24, 32, 44, 55, 66, 76, 42, 23, 11, 6, 59, 43, 88, 99, 1, 13, 47, 43, 56]
    result_list = []

    num = 0
    while True:
        if num > len(working_list):
            break

        result_list += list(reversed(working_list[num:num+block_size]))
        num += block_size

    print(working_list, '\n', result_list)

if __name__ == '__main__':
    main()
