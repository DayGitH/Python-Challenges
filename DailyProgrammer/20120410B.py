"""
Reverse Polish Notation(RPN) is a mathematical notation where every operator follows all of its operands. For instance,
to add three and four, one would write "3 4 +" rather than "3 + 4". If there are multiple operations, the operator is
given immediately after its second operand; so the expression written "3 ? 4 + 5" would be written "3 4 ? 5 +" first
subtract 4 from 3, then add 5 to that.

Transform the algebraic expression with brackets into RPN form.

You can assume that for the test cases below only single letters will be used, brackets [ ] will not be used and each
expression has only one RPN form (no expressions like abc)

Test Input:
(a+(b*c))
((a+b)*(z+x))
((a+t)*((b+(a+c))^(c+d)))
Test Output:
abc*+
ab+zx+*
at+bac++cd+ ^ *
"""

import re

inp = '((a+t)*((b+(a+c))^(c+d)))'

print(inp)

parenth = re.compile(r"(?<=\()[^()]*(?=\))", re.DOTALL)
symbol = re.compile(r"[+\-*/^](?=\w)", re.DOTALL)
while True:
    # Find expression between two parens without parens inbetween. End loop if not found
    txt = parenth.search(inp)
    if txt is None:
        break

    # find operator and its location in found expression
    sym = symbol.search(txt.group())

    # rearrange expression
    new = txt.group()[:sym.span()[0]] + txt.group()[sym.span()[1]:] + sym.group()

    # update rearranged expression
    inp = inp[:txt.span()[0]-1] + new + inp[txt.span()[1]+1:]
    print(inp)
