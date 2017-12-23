"""
During World War I, the German army used a very clever pen and paper cipher called the ADFGVX cipher
[http://en.wikipedia.org/wiki/ADFGVX_cipher], and your task today is to implement functions to both encrypt and decrypt
messages using this cipher. What follows is a rather lengthy description of how it works (you can also find a
description in that wikipedia link), but in essence it is actually quite simple.

Here is how it works:
The cleartext (the message that is to be encrypted) could consist of characters selected from an alphabet of
36 characters. For the purposes of today's problem, that alphabet will be:

"ABCDEFGHIKLMNOPQRSTUVWXYZ0123456789 "

That is, it will be the regular uppercase alphabet except for the letter J (if there's a J in the cleartext, replace it
with an I), ten numbers, and a space character. That makes 25 + 10 + 1 = 36 different characters.

The ciphertext will consist of only 6 different characters, namely the characters "ADFGVX". Supposedly these were
selected because they are quite unlike each other in morse code, lessening the risk for errors in transmission.

The key for the encryption and decryption consists of two parts: first one scrambled version of the cleartext alphabet
(i.e. some permutation of "ABCDEFGHIKLMNOPQRSTUVWXYZ0123456789 "), called the substitution key. Second we need a
transposition key which is a just a codeword of some sort.

Lets illustrate the encryption of the cleartext "Brake me out of jail on the 21st." using the substitution key
"R3FLMX7KWQ69D4Y5NOZ STV2EH8AP1ICBGU0" and the transposition key "PROGRAMMER"

Encryption proceeds as follows: we begin by putting the cleartext in A suitable format, so that it only contains
characters from the alphabet. Our cleartext then becomes "BRAKE ME OUT OF IAIL ON THE 21ST". As you can see, all
characters have been put into uppercase, the "J" have been replaced by an "I", and all characters not in the alphabet
(in this example, only the period ".") have been removed.

Next we put the substitution key into a 6x6 table with the cipher chars "ADFGVX" as row and column headers, like this:

   A D F G V X
  +------------
A | R 3 F L M X
D | 7 K W Q 6 9
F | D 4 Y 5 N O
G | Z   S T V 2
V | E H 8 A P 1
X | I C B G U 0

Each letter of the cleartext now gets replaced by two letters representing the row and column of the character in this
square. So for instance, 'A' becomes 'VG' (because it's in the V row and the G column), 'B' becomes 'XF', 'C' becomes
'XD', etc. This is called "fractioning" the text. If we convert our cleartext using this method it becomes:

B  R  A  K  E     M  E     O  U  T     O  F
XF AA VG DD VA GD AV VA GD FX XV GG GD FX AF GD

I  A  I  L     O  N     T  H  E     2  1  S  T
XA VG XA AG GD FX FV GD GG VD VA GD GX VX GF GG

Note that the space character is encoded as GD.

Next, this fractioned text is put into a table with the transposition key as headers, as follows:

P R O G R A M M E R
-------------------
X F A A V G D D V A
G D A V V A G D F X
X V G G G D F X A F
G D X A V G X A A G
G D F X F V G D G G
V D V A G D G X V X
G F G G F G F A D F

The last row didn't quite fit (it was six letters short), so we add in some random characters, in this case "FGFADF", to
fill it out. Now the columns are sorted in alphabetical order of the header characters:

A E G M M O P R R R
-------------------
G V A D D A X F V A
A F V G D A G D V X
D A G F X G X V G F
G A A X A X G D V G
V G X G D F G D F G
D V A G X V V D G X
G D G F A G G F F F

As you can see, the sorting is "stable", i.e. when there are two or more characters are identical in the transposition
key, they keep the original order they had. So in this example, there are three R's and two M's, and they are in the
same order relative to each other both before and after the transposition.

Now, finally, we simply read off the table column by column to get our ciphertext. This is the final result:

GADGVDGVFAAGVDAVGAXAGDGFXGGFDDXADXAAAGXFVGXGXGGVGFDVDDDFVVGVFGFAXFGGXF

To decrypt, reverse the operations described here.

EDIT: so, I just realized that I misspelled "Break out of jail" as "Brake out of jail", but it would be too much work to
fix it now :) I apologize for the silly mistake. Then again, hardened criminals aren't known for being great spellers!
"""

import numpy as np
from collections import defaultdict


def encrypt_adfgvx(cleartext, subs_key, trans_key):
    text = adfgvx_formatter(cleartext, subs_key)

    subs_arr = subs_array(subs_key)

    code = adfgvx_encode(text, subs_arr)
    code = reshape_encode(code, trans_key)
    code = reorder_encode(code, trans_key)
    return code


def subs_array(subs_key):
    subs_arr = np.array(list(subs_key))
    subs_arr.resize(6, 6)
    return subs_arr


def adfgvx_formatter(cleartext, subs_key):
    cleartext = cleartext.upper().replace('J', 'I')
    key_set = set(subs_key)
    return ''.join([t for t in cleartext if t in key_set])


def adfgvx_encode(text, subs_arr):
    code_dict = 'ADFGVX'
    enc = []
    for t in text:
        index = np.asarray(np.where(subs_arr == t)).T[0]
        enc.append(code_dict[index[0]])
        enc.append(code_dict[index[1]])
    return enc


def reshape_encode(enc, trans_key):
    code_dict = list('ADFGVX')
    length = len(trans_key)
    diff = length - (len(enc) % length)
    enc.extend(np.random.choice(code_dict, diff))
    return np.array(enc).reshape(-1, length)


def reorder_encode(enc, trans_key):
    trans_list = [(k, n) for n, k in enumerate(trans_key)]
    sorted_list = sorted(trans_list, key=lambda x: x[0])
    res = enc[:, [s[1] for s in sorted_list]]
    return ''.join(res.T.reshape(1, -1)[0])


def decrypt_adfgvx(code, subs_key, trans_key):
    subs_arr = subs_array(subs_key)

    answer = reorder_decode(code, trans_key)
    answer = ''.join(answer.reshape(1, -1)[0])
    answer = adfgvx_decode(answer, subs_arr)
    return answer


def reorder_decode(code, trans_key):
    code = np.array(list(code))
    code = code.reshape(len(trans_key), -1)
    code = code.T

    trans_list = [(k, n) for n, k in enumerate(trans_key)]
    sorted_list = sorted(trans_list, key=lambda x: x[0])
    sorter = [s[1] for s in sorted_list]
    sorter = [n for n, s in sorted(enumerate(sorter), key=lambda x: x[1])]
    return code[:, sorter]


def adfgvx_decode(code, subs_arr):
    code_dict = 'ADFGVX'
    res = ''
    for s in range(0, len(code), 2):
        res += subs_arr[code_dict.index(code[s]), code_dict.index(code[s+1])]
    return res


def generate_substitution_key():
    # TODO fix this
    subs_key = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")
    np.random.shuffle(subs_key)
    return ''.join(subs_key)


def main():
    cleartext = "Brake me out of jail on the 21st."
    # subs_key = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")
    # np.random.shuffle(subs_key)
    # subs_key = ''.join(subs_key)
    subs_key = generate_substitution_key()
    print(subs_key)
    trans_key = "PROGRAMMER"

    code = encrypt_adfgvx(cleartext, subs_key, trans_key)
    answer = decrypt_adfgvx(code, subs_key, trans_key)

    print(cleartext)
    print(code)
    print(answer)


if __name__ == "__main__":
    main()
