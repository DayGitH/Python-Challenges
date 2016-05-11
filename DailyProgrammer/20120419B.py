"""
Write a program that will use the FOIL method [http://www.algebrahelp.com/lessons/simplifying/foilmethod/pg2.htm] to
solve multiplying binomials. Your program will accept a binomial algebraic formula as input and you will parse the
data, use the FOIL method to reduce the formula, and print out the solution. You decide how you want to represent
exponents (could use caret, or just write out the value after the variable).

Sample Run:
Enter Binomials:  (2x + 6)(7x + 3)
Result:  14x^2 + 48x + 18
Enter Binomials: (2x2 + 3x)(5x2 + 9x)
Result:  10x4 + 33x3 + 27x2

Bonus: Support trinomials

"""


def findItem(theList, item):
    return [[ind, theList[ind].index(item)] for ind in range(len(theList)) if item in theList[ind]]

OPERATORS = ['+', '-']

inp = '(2x - 6)(7x - 3)'

# remove one side parens and use other to split the binomial into separate strings in a list.
# the filter is used to remove the empty string in the list
bin = list(filter(None, inp.replace('(', '').split(')')))

print(bin)

poly = [[0 for a in range(2)] for b in range(2)]
negative = False

for m,i in enumerate(bin):
    eq = i.split()

    if eq[1] == "-":
        negative = True
    else:
        negative = False

    eq = [item for item in eq if item not in OPERATORS]
    for n, c in enumerate(eq):
        x = c.find('x')
        if x > 0:
            num = int(c[:x])
            power = c[x+1:]
            if not power:
                power = 1
            else:
                power = int(power)
        else:
            num = int(c)
            power = 0

        if negative and n == 1:
            num *= -1

        poly[m][n] = [num, power]

res = []
for m, first in enumerate(poly[0]):
    for n, second in enumerate(poly[1]):
        res.append([first[0]*second[0], first[1]+second[1]])

print(res)
xy = zip(*res)
rng = list(map(max,xy))[1]

res2 = [0 for i in range(rng+1)]
for i in range(rng+1):
    index = findItem(res,i)
    for j in index:
        res2[i] += res[j[0]][0]

print(res2)
for a in range(len(res2)):
    if a > 1:
        res2[a] = str(res2[a]) + 'x' + str(a)
    elif a > 0:
        res2[a] = str(res2[a]) + 'x'
    else:
        res2[a] = str(res2[a])
    print(a, res2[a])

printer = ""

for a in res2:
    if not printer:
        printer = a
    else:
        if a[0] == "-":
            printer += " - {}".format(a.replace("-",""))
        else:
            printer += " + {}".format(a)

print(printer)
