'''
Write a program that will take coordinates, and tell you the corresponding number in pascals triangle. For example:
Input: 1, 1
output:1
input: 4, 2
output: 3
input: 1, 19
output: error/nonexistent/whatever
the format should be "line number, integer number"
for extra credit, add a function to simply print the triangle, for the extra credit to count, it must print at least
15 lines.
'''

old_list = []
new_list = [1]

print('Line number?')
line_number = int(input('> '))

print('Integer number?')
int_number = int(input('> '))

# print(new_list)

#generates a pascal triangle tier in each loop
for i in range(line_number - 1):
    new_list, old_list = [], new_list

    new_list.append(1)

    if i > 0:
        for e in range(0,len(old_list)-1):
            new_list.append(old_list[e] + old_list[e + 1])

    new_list.append(1)
    # print(new_list)

try:
    print('The integer is: {}'.format(new_list[int_number - 1]))
except IndexError:
    print('Nonexistent!!!')