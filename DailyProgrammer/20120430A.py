"""
The population count of a bitstring is the number of set bits (1-bits) in the string. For instance, the population
count of the number 23, which is represented in binary as 10111 is 4.

Your task is to write a function that determines the population count of a number representing a bitstring
"""

def pop(n):
    return bin(n)[2:].count('1')

if __name__ == '__main__':
    print(pop(255))