"""
Huffman coding [http://en.wikipedia.org/wiki/Huffman_coding] is a compression algorithm. Implementing it is a good
occasion to work with queues, trees and bits.

Say we have a string of characters, and we want to transmit it over a network. To that end, we're gonna compress it.

The idea of the Huffman encoding is to replace each character by a bit sequence whose length depends on the frequency of
occurrence of the character in the string: if a character occurs very often, we want to represent it by a very short bit
sequence to avoid wasting space, but if appears only once or twice, it doesn't really matter if the bit sequence is
long.

Exercise:

    Write a function that takes a string and returns a Huffman tree, as described in the Wikipedia article.

    Write an encoding function that takes a string and returns a sequence of bits that correspond to its Huffman
    encoding.

    Write a decoding function that takes a sequence of bits and a Huffman tree, and reconstructs the original string.

Notice that you need the tree to decode a message. Bonus points if you figure out a way to encode the tree along with
the bit sequence.

Also, don't let the gigantic introduction in the Wikipedia article discourage you, an algorithm is explained here
[http://en.wikipedia.org/wiki/Huffman_coding#Basic_technique]. There's even a cute animation!

(This challenge was posted to /r/dailyprogrammer_ideas by /u/wicked-canid -- thanks!)
"""


def huffman_tree(string):
    chars = set(string)
    hist = []
    tree = {}
    for c in chars:
        hist.append([c, string.count(c)])
        tree[c] = ''

    while len(hist) > 1:
        hist.sort(key=lambda x: x[1])

        zero = hist.pop(0)
        one = hist.pop(0)
        for char in zero[0]:
            tree[char] = '0' + tree[char]
        for char in one[0]:
            tree[char] = '1' + tree[char]
        hist.append([zero[0]+one[0], zero[1]+one[1]])

    print(tree)
    return tree


def huffman_encode(string, tree):
    string = string.upper()

    res = ''
    for char in string:
        res += tree[char]
    return res


def huffman_decode(string, tree):
    decoder = {tree[key]: key for key in tree}
    check = ''
    res = ''
    for bit in string:
        check += bit
        if check in decoder:
            res += decoder[check]
            check = ''
    return res


def main():
    inp = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"

    print(inp)
    tree = huffman_tree(inp)
    code = huffman_encode(inp, tree)
    print(code)
    original = huffman_decode(code, tree)
    print(original)


if __name__ == "__main__":
    main()
