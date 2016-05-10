'''
An "upside up" number is a number that reads the same when it is rotated 180 degrees. For instance, 689 and 1961 are upside up
numbers.

Your task is to find the next upside up number greater than 1961, and to count the number of upside up numbers less
than ten thousand.

edit: since there is a confusion about 2 and 5, please consider them as "upside up" numbers for this problem. If you
have already done without it, its ok. Sorry for the late reply.
source: programmingpraxis.com
'''

u_list = ['0', '1', '2', '5', '6', '8', '9']
u_dict = {'0': '0', '1': '1', '2': '5', '5': '2', '6': '9', '8': '8', '9': '6'}

for i in range(19, 100):
    num_str = str(i)
    if set(num_str) - set(u_list):
        continue
    for n in reversed(num_str):
        num_str += u_dict[n]

    print(num_str)