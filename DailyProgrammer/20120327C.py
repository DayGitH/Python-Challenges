"""
In this challenge, given an array of integers, the goal is to efficiently find the subarray that has the greatest value
when all of its elements are summed together. Note that because some elements of the array may be negative, the problem
is not solved by simply picking the start and end elements of the array to be the subarrray, and summing the entire
array. For example, given the array

{1, 2, -5, 4, -3, 2}

The maximum sum of a subarray is 4. It is possible for the subarray to be zero elements in length (if every element of
the array were negative).

Try to come up with an efficient algorithm!

taken from cprogramming.com
"""

def subarray(l):
    max = 0
    start = 0
    end = 0
    for a in range(1, len(l)+1):
        for b in range(6-a+1):
            if sum(l[b:b+a]) > max:
                max = sum(l[b:b+a])
                start = b
                end = b+a
    if max:
        return l[start:end]
    else:
        return False

if __name__ == '__main__':
    print(subarray([1, 2, -5, 4, -3, 2]))
