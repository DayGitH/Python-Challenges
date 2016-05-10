import pickle
from string import *

file = pickle.load(open('ch5.p','rb'))

for line in file:
    for set in line:
        for x in range(set[1]):
            print(set[0],end='')
    print()