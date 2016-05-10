'''
The U.S government has commissioned you to catch the terrorists!
There is a mathematical pyramid with the following pattern:
1
11
21
1211
111221
312211
you must write a program to calculate up to the 40th line of this pyramid. If you don't, the terrorists win!
'''

COUNT = 40

def count_digits(num_string):
    res = ''
    c = 0
    s = '.'
    for i in num_string:
        if i == s:
            c += 1
        else:
            res += str(c) + s
            s = i
            c = 1
    res += str(c) + s
    return res[2:]

string = '1'

print(string)

# minus one for offset by initial string
for i in range(COUNT - 1):
    string = count_digits(string)
    print(string)