"""
Give the Ullman's Puzzle

    This puzzle is due to Jeffrey Ullman:

    Given a list of n real numbers, a real number t, and an integer k, determine if there exists a k-element subset of
    the original list of n real numbers that is less than t.

    For instance, given the list of 25 real numbers 18.1, 55.1, 91.2, 74.6, 73.0, 85.9, 73.9, 81.4, 87.1, 49.3, 88.8,
    5.7, 26.3, 7.1, 58.2, 31.7, 5.8, 76.9, 16.5, 8.1, 48.3, 6.8, 92.4, 83.0, 19.6, t = 98.2 and k = 3, the 3-element
    subset 31.7, 16.5 and 19.6 sums to 67.8, which is less than 98.2, so the result is true.

    This is a puzzle, so you’re not allowed to look at the suggested solution until you have your own solution.

    Your task is to write a function that makes that determination. When you are finished, you are welcome to read or
    run a suggested solution, or to post your own solution or discuss the exercise in the comments below.

Write a function that makes that determination
"""


def ullman(n_list, t, k):
    return t > sum(sorted(n_list)[:k])


def main():
    n_list = [18.1, 55.1, 91.2, 74.6, 73.0,
              85.9, 73.9, 81.4, 87.1, 49.3,
              88.8, 05.7, 26.3, 07.1, 58.2,
              31.7, 05.8, 76.9, 16.5, 08.1,
              48.3, 06.8, 92.4, 83.0, 19.6]

    t = 98.2
    k = 3

    print('Ullman: {}'.format(ullman(n_list, t, k)))


if __name__ == "__main__":
    main()
