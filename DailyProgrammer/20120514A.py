"""
Imagine each letter and its position within the alphabet. Now assign each letter its corresponding value ie a=1,
b=2,... z=26. When given a list of words, order the words by the sum of the values of the letters in their names.

Example: Shoe and Hat
Hat: 8+1+20 = 29
Shoe: 19+8+15+5 = 47
So the order would be Hat, Shoe.

For extra points, divide by the sum by the number of letters in that word and then rank them.
thanks to SpontaneousHam for the challenge at /r/dailyprogrammer_ideas
"""

w_list = ['shoe', 'hat']


def main():
    ascii_list=lambda x: [i - 96 for i in list(map(ord, list(x)))]
    res = sorted(w_list, key=ascii_list)
    print(res)

if __name__ == "__main__":
    main()
