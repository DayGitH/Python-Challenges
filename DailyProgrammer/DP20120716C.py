"""
Write a program that is able to find all words in a Boggle [http://en.wikipedia.org/wiki/Boggle] board. For a word list,
you can use this file [http://code.google.com/p/dotnetperls-controls/downloads/detail?name=enable1.txt].

How many words can you find in the following 10x10 Boggle board?

T N L E P I A C N M
T R E H O C F E I W
S C E R E D A M E A
A O M O G O O F I E
G A C M H N L E R X
T D E R J T F O A S
I T A R T I N H N T
R N L Y I V S C R T
A X E P S S H A C F
I U I I I A I W T T

    Thanks to Medicalizawhat for suggesting this problem (and to Cosmologicon for providing a word list and some
    commentary) at /r/dailyprogrammer_ideas! If you have a problem that you think would be good for us, why not head
    over there and suggest it?

"""


class Node:
    """ from https://en.wikipedia.org/wiki/Trie#Algorithms """
    def __init__(self):
        self.children = {}  # mapping from character ==> Node
        self.value = None


def find(node, key):
    """ from https://en.wikipedia.org/wiki/Trie#Algorithms """
    for char in key:
        if char in node.children:
            node = node.children[char]
        else:
            return None
    return node.value


def insert(root, string, value):
    """ from https://en.wikipedia.org/wiki/Trie#Algorithms """
    node = root
    i = 0
    while i < len(string):
        if string[i] in node.children:
            node = node.children[string[i]]
            i += 1
        else:
            break

    # append new nodes for the remaining characters, if any
    while i < len(string):
        node.children[string[i]] = Node()
        node = node.children[string[i]]
        i += 1

    # store value in the terminal node
    node.value = value


def create_trie():
    with open('enable1.txt', 'r') as f:
        data = f.read().split()

    node = Node()
    for d in data:
        insert(node, d, d)
    return node


def main():
    node = create_trie()
    print(find(node, 'decipherer'))


if __name__ == "__main__":
    main()
