'''
today, your challenge is to create a program that will take a series of numbers (5, 3, 15), and find how those numbers
can add, subtract, multiply, or divide in various ways to relate to eachother. This string of numbers should result in
5 * 3 = 15, or 15 /3 = 5, or 15/5 = 3. When you are done, test your numbers with the following strings:
4, 2, 8
6, 2, 12
6, 2, 3
9, 12, 108
4, 16, 64
For extra credit, have the program list all possible combinations.
for even more extra credit, allow the program to deal with strings of greater than three numbers. For example, an input
of (3, 5, 5, 3) would be 3 * 5 = 15, 15/5 = 3. When you are finished, test them with the following strings.
2, 4, 6, 3
1, 1, 2, 3
4, 4, 3, 4
8, 4, 3, 6
9, 3, 1, 7
'''

numbers = [9, 3, 1, 6]

# if numbers[0] + numbers[1] == numbers[2]:
#     print("{} + {} = {}".format(numbers[0],numbers[1],numbers[2]))
#     print("{} - {} = {}".format(numbers[2],numbers[0],numbers[1]))
#     print("{} - {} = {}".format(numbers[2],numbers[1],numbers[0]))
# elif abs(numbers[0] - numbers[1]) == numbers[2]:
#     print("{} - {} = {}".format(max(numbers[0],numbers[1]),min(numbers[0],numbers[1]),numbers[2]))
#     print("{} + {} = {}".format(min(numbers[0],numbers[1]),numbers[2],max(numbers[0],numbers[1])))
#     print("{} - {} = {}".format(max(numbers[0],numbers[1]),numbers[2],min(numbers[0],numbers[1])))
# elif numbers[0] * numbers[1] == numbers[2]:
#     print("{} * {} = {}".format(numbers[0],numbers[1],numbers[2]))
#     print("{} / {} = {}".format(numbers[2],numbers[0],numbers[1]))
#     print("{} / {} = {}".format(numbers[2],numbers[1],numbers[0]))
# elif numbers[0] / numbers[1] == numbers[2]:
#     print("{} / {} = {}".format(numbers[0],numbers[1],numbers[2]))
#     print("{} * {} = {}".format(numbers[1],numbers[2],numbers[0]))
#     print("{} / {} = {}".format(numbers[0],numbers[2],numbers[1]))
# else:
#     print('broke')

ops = ['+', '-', '*', '/']

for i in range(1,len(numbers)):
    remaining = numbers[1:len(numbers)]
    remaining.remove(numbers[i])
    for a in ops:
        for b in ops:
            if eval(str(numbers[0])+a+str(numbers[i])) == eval(str(remaining[0])+b+str(remaining[1])):
                print(str(numbers[0])+a+str(numbers[i]),'=',str(remaining[0])+b+str(remaining[1]))