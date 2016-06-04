"""
T9 Spelling: The Latin alphabet contains 26 characters and telephones only have ten digits on the keypad. We would like
to make it easier to write a message to your friend using a sequence of keypresses to indicate the desired characters.
The letters are mapped onto the digits as 2=ABC, 3=DEF, 4=GHI, 5=JKL, 6=MNO, 7=PQRS, 8=TUV, 9=WXYZ. To insert the
character B for instance, the program would press 22. In order to insert two characters in sequence from the same key,
the user must pause before pressing the key a second time. The space character should be printed to indicate a pause.
For example "2 2? indicates AA whereas "22? indicates B. Each message will consist of only lowercase characters a-z and
space characters. Pressing zero emits a space. For instance, the message "hi" is encoded as "44 444?, "yes" is encoded
as "999337777?, "foo bar" (note two spaces) is encoded as "333666 6660022 2777?, and "hello world" is encoded as
"4433555 555666096667775553?.

This challenge has been taken from Google Code Jam Qualification Round Africa 2010
[http://code.google.com/codejam/contest/dashboard?c=351101#s=p2] ... Please use the link for clarifications. Thank You
"""

import re

T9_dict = {'2': 'a', '22': 'b', '222': 'c',
           '3': 'd', '33': 'e', '333': 'f',
           '4': 'g', '44': 'h', '444': 'i',
           '5': 'j', '55': 'k', '555': 'l',
           '6': 'm', '66': 'n', '666': 'o',
           '7': 'p', '77': 'q', '777': 'r', '7777': 's',
           '8': 't', '88': 'u', '888': 'v',
           '9': 'w', '99': 'x', '999': 'y', '9999': 'z'}

"""
Inverse dictionary creator from https://stackoverflow.com/questions/2568673/inverse-dictionary-lookup-python
"""
T9_dict2 = {v: k for k, v in T9_dict.items()}


def splitter(inp):
    res = []
    inp = inp.split(' ')
    for i in inp:
        res += [m.group(0) for m in re.finditer(r"(\d)\1*", i)]
    return res


def decoder(l):
    res = ''
    for i in l:
        if '0' in i:
            res += ' '
        else:
            res += T9_dict[i]
    return res


def encoder(str):
    res = ''
    hold = ''
    for i in str:
        if i == ' ':
            res += '0'
        else:
            if hold in T9_dict2[i]:
                res += ' '
            res += T9_dict2[i]
            hold = res[-1]
    return res.strip()


def main():
    # inp = input('T9 input: ')  #
    inp = '4433555 555666096667775553'
    s = splitter(inp)
    t = decoder(s)
    print(t)

    inp = 'hello world'
    w = encoder(inp)
    print(w)


if __name__ == "__main__":
    main()
