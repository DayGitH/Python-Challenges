"""
Find the longest palindrome in the following 1169-character string:

Fourscoreandsevenyearsagoourfaathersbroughtforthonthisconta
inentanewnationconceivedinzLibertyanddedicatedtotheproposit
ionthatallmenarecreatedequalNowweareengagedinagreahtcivilwa
rtestingwhetherthatnaptionoranynartionsoconceivedandsodedic
atedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWeh
avecometodedicpateaportionofthatfieldasafinalrestingplacefo
rthosewhoheregavetheirlivesthatthatnationmightliveItisaltog
etherfangandproperthatweshoulddothisButinalargersensewecann
otdedicatewecannotconsecratewecannothallowthisgroundThebrav
elmenlivinganddeadwhostruggledherehaveconsecrateditfarabove
ourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorl
ongrememberwhatwesayherebutitcanneverforgetwhattheydidhereI
tisforusthelivingrathertobededicatedheretotheulnfinishedwor
kwhichtheywhofoughtherehavethusfarsonoblyadvancedItisrather
forustobeherededicatedtothegreattdafskremainingbeforeusthat
fromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwh
ichtheygavethelastpfullmeasureofdevotionthatweherehighlyres
olvethatthesedeadshallnothavediedinvainthatthisnationunsder
Godshallhaveanewbirthoffreedomandthatgovernmentofthepeopleb
ythepeopleforthepeopleshallnotperishfromtheearth

Your task is to write a function that finds the longest palindrome in a string and apply it to the string given above.

    taken from http://challenge.greplin.com/ :)

It seems the number of users giving challenges have been reduced. Since my final exams are going on and its kinda
difficult to think of all the challenges, I kindly request you all to suggest us interesting challenges at
/r/dailyprogrammer_ideas .. Thank you!
"""

import numpy as np


def longest_common_substring(str1, str2):
    """ from 20120602C """
    l1 = len(str1)
    l2 = len(str2)

    if l2 < l1:
        l1, l2 = l2, l1
        str1, str2 = str2, str1

    L = np.zeros((l1, l2))
    z = 0
    ret = []
    """ based on pseudocode from wikipedia """
    for i in range(l1):
        for j in range(l2):
            if str1[i] == str2[j]:
                if i == 0 or j == 0:
                    L[i, j] = 1
                else:
                    L[i, j] = L[i-1, j-1] + 1
                if L[i, j] > z:
                    z = int(L[i, j])
                    ret = [str1[i-z+1:i+1]]
                elif L[i, j] == z:
                    ret.append(str1[i-z+1:i+1])
            else:
                L[i, j] = 0

    if len(ret) == 1:
        return ret[0]
    else:
        return ret


def enforce_palindrom(answer):
    if type(answer) == list:
        answer = list(map(lambda x: x == x[::-1], answer))
    return answer


def main():
    string = 'Fourscoreandsevenyearsagoourfaathersbroughtforthonthisconta' \
             'inentanewnationconceivedinzLibertyanddedicatedtotheproposit' \
             'ionthatallmenarecreatedequalNowweareengagedinagreahtcivilwa' \
             'rtestingwhetherthatnaptionoranynartionsoconceivedandsodedic' \
             'atedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWeh' \
             'avecometodedicpateaportionofthatfieldasafinalrestingplacefo' \
             'rthosewhoheregavetheirlivesthatthatnationmightliveItisaltog' \
             'etherfangandproperthatweshoulddothisButinalargersensewecann' \
             'otdedicatewecannotconsecratewecannothallowthisgroundThebrav' \
             'elmenlivinganddeadwhostruggledherehaveconsecrateditfarabove' \
             'ourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorl' \
             'ongrememberwhatwesayherebutitcanneverforgetwhattheydidhereI' \
             'tisforusthelivingrathertobededicatedheretotheulnfinishedwor' \
             'kwhichtheywhofoughtherehavethusfarsonoblyadvancedItisrather' \
             'forustobeherededicatedtothegreattdafskremainingbeforeusthat' \
             'fromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwh' \
             'ichtheygavethelastpfullmeasureofdevotionthatweherehighlyres' \
             'olvethatthesedeadshallnothavediedinvainthatthisnationunsder' \
             'Godshallhaveanewbirthoffreedomandthatgovernmentofthepeopleb' \
             'ythepeopleforthepeopleshallnotperishfromtheearth'

    string = string.lower()

    answer = longest_common_substring(string, string[::-1])
    print(answer)


if __name__ == "__main__":
    main()
