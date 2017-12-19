"""
Anyone who've tried to get through the A Song of Ice and Fire books written by George R.R. Martin (the basis for the HBO
show Game of Thrones) knows that while the books are generally excellent, there are a lot of characters. A staggering
number, in fact, and it can be very hard to remember who's who and who is related to who and who had an incestual
relationship with what sister or brother.

So, today, we make that a little bit easier! What follows at the end here is a list of 50+ characters from the books and
a list detailing how their related. Each character is given a two-letter code (for instance "AA" or "BQ") and a
specification of their gender ("M" or "F"), and then what follows is a list detailing how they're related to the other
characters.

To make things simple, there's only one "basic" relationship, which is "A is parent to B", written as "->". So, for
instance, if Arya Stark has the code "AI" and Eddard Stark has the code "AB", then "AB->AI" means "Eddard Stark is
parent to Arya Stark". Each person may have 0, 1 or 2 parents specified somewhere in the list, but no more.

(I should point out here that this family tree contains no spoilers. This is the family tree as it stands in the
beginning of Book 1, though some of the characters you wont meet until much later. For those of you who've read the
books or seen the show, please don't put any spoilers in the comments, even in hidden spoiler text.)

Write a program that parses this list, and can then answer questions about the relationships between people. Here are a
list of functions you should write:

    ancestors(person) which gives the direct ancestors of that person (parents, grand-parents, great-grand-parents,
    etc.). For instance, ancestors("Asha Greyjoy") should return ["Balon Greyjoy", "Alannys Harlaw", "Quellon Greyjoy"].
    What is the result to ancestors("Daenerys Targaryen")?

    descendants(person) which gives you the direct descendants of that person (children, grand-children,
    great-grand-children, etc.). What is the result of descendants("Jaehaerys Targaryen")?

    brothers(person) and sisters(person) which gives the brothers and sisters of the specified person (including
    half-brothers and half-sisters, though you could write special functions for full siblings and half siblings if you
    want).

    aunts(person) and uncles(person) which gives you the aunts and uncles of the specified person.

    cousins(person), which gives you the 1st cousins of the specified person.

    Bonus: As a bonus, write a function called relationship(person1, person2) which returns person1's relationshipt to
    person2 as a string (i.e. "Grandfather", "1st cousin", "Brother", "Great uncle", "Not related" etc.). As with all
    bonuses on /r/dailyprogrammer, this is entirely optional. EDIT: Since this chart gives no indication about who is
    married to whom, you can safely exclude all familial relationships that somehow involves marriage. That means that
    relationship("Eddard Stark", "Catelyn Tully") should return "Not related", and you can also skip all
    brother/sister/mother/father in-laws. Only relationships "by blood", so to speak.

And now, here is the family tree of some of the major characters in A Song of Ice and Fire:

AA = Rickard Stark (M)        AB = Eddard Stark (M)         AC = Catelyn Tully (F)
AD = Brandon Stark (M)        AE = Benjen Stark (M)         AF = Jon Snow (M)
AG = Robb Stark (M)           AH = Sansa Stark (F)          AI = Arya Stark (F)
AJ = Bran Stark (M)           AK = Rickon Stark (M)         AL = Hoster Tully (M)
AM = Minisa Whent (F)         AN = Edmure Tully (M)         AO = Lysa Tully (F)
AP = Jon Arryn (M)            AQ = Robert Arryn (M)         AR = Tytos Lannister (M)
AS = Tywin Lannister (M)      AT = Joanna Lannister (F)     AU = Kevan Lannister (M)
AV = Cersei Lannister (F)     AW = Jamie Lannister (M)      AX = Tyrion Lannister (M)
AY = Robert Baratheon (M)     AZ = Joffrey Baratheon (M)    BA = Myrcella Baratheon (F)
BB = Tommen Baratheon (M)     BC = Lancel Lannister (M)     BD = Steffon Baratheon (M)
BE = Stannis Baratheon (M)    BF = Selyse Florent (F)       BG = Shireen Baratheon (F)
BH = Renly Baratheon (M)      BI = Jaehaerys Targaryen (M)  BJ = Aerys Targaryen (M)
BK = Rhaella Targaryen (F)    BL = Rhaegar Targaryen (M)    BM = Elia Martell (F)
BN = Rhaenys Targaryen (F)    BO = Aegon Targaryen (M)      BP = Viserys Targaryen (M)
BQ = Daenerys Targaryen (F)   BR = Quellon Greyjoy (M)      BS = Balon Greyjoy (M)
BT = Euron Greyjoy (M)        BU = Victarion Greyjoy (M)    BV = Urrigon Greyjoy (M)
BW = Aeron Greyjoy (M)        BX = Rodrik Greyjoy (M)       BY = Maron Greyjoy (M)
BZ = Asha Greyjoy (F)         CA = Theon Greyjoy (M)        CB = Alannys Harlaw (F)
---------------------------------------------------------------------------------------
AA->AB, AA->AD, AA->AE, AB->AF, AB->AG, AB->AH, AB->AI, AB->AJ, AB->AK, AC->AG,
AC->AH, AC->AI, AC->AJ, AC->AK, AL->AC, AL->AN, AL->AO, AM->AC, AM->AN, AM->AO,
AO->AQ, AP->AQ, AR->AS, AR->AU, AS->AV, AS->AW, AS->AX, AT->AV, AT->AW, AT->AX,
AU->BC, AV->AZ, AV->BA, AV->BB, AY->AZ, AY->BA, AY->BB, BD->AY, BD->BE, BD->BH,
BE->BG, BF->BG, BI->BJ, BI->BK, BJ->BL, BJ->BP, BJ->BQ, BK->BL, BK->BP, BK->BQ,
BL->BN, BL->BO, BM->BN, BM->BO, BR->BS, BR->BT, BR->BU, BR->BV, BR->BW, BS->BX,
BS->BY, BS->BZ, BS->CA, CB->BX, CB->BY, CB->BZ, CB->CA
"""

import re


class Character:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

        self.parents = []
        self.children = []


def extract_data(input_string):
    char_dict = {}
    code_dict = {}
    for char in re.findall('([A-Z]{2} = [A-Za-z ]* \([FM]\))', input_string):
        code = char[:2]
        name = char[5:-4]
        gender = char[-2]

        code_dict[code] = name
        char_dict[name] = Character(name, gender)

    for rel in re.findall('([A-Z]{2}->[A-Z]{2})', input_string):
        parent = code_dict[rel[:2]]
        child = code_dict[rel[-2:]]

        char_dict[parent].children.append(child)
        char_dict[child].parents.append(parent)

    return char_dict


def ancestors(char_dict, person):
    parents = char_dict[person].parents
    res = set(parents[:])
    for p in parents:
        res.update(ancestors(char_dict, p))
    return list(res)


def descendants(char_dict, person):
    children = char_dict[person].children
    res = set(children[:])
    for c in children:
        res.update(descendants(char_dict, c))
    return list(res)


def siblings(char_dict, person, gender=None, fullness=0):
    """fullness=0 all siblings
       fullness=1 full siblings only
       fullness=2 half siblings only
    """
    parents = char_dict[person].parents
    if gender:
        children = []
        for p in parents:
            res = []
            for c in char_dict[p].children:
                if char_dict[c].gender == gender:
                    res.append(c)
            children.append(res)
    else:
        children = [char_dict[p].children for p in parents]

    if len(children) == 1:
        children.append([])

    answer = []
    if fullness == 0:
        answer = list(set(children[0]) | set(children[1]))
    elif fullness == 1:
        answer = list(set(children[0]) & set(children[1]))
    elif fullness == 2:
        answer = list(set(children[0]) ^ set(children[1]))

    if person in answer:
        answer.remove(person)

    return answer


def parents_siblings(char_dict, person, gender=None):
    parents = set(char_dict[person].parents)
    grandparents = [char_dict[p].parents for p in parents]
    grandparents = {p for sublist in grandparents for p in sublist}

    # return list({char_dict[g].children for g in grandparents})
    res = {''}
    for g in grandparents:
        if gender:
            for c in char_dict[g].children:
                if char_dict[c].gender == gender:
                    res.update([c])
        else:
            res.update(char_dict[g].children)
    return list(res - parents)[1:]  # [1:] to remove empty name


def cousins(char_dict, person):
    upper_list = parents_siblings(char_dict, person)
    return list({c for upper in upper_list for c in char_dict[upper].children})


def relationship(person1, person2):
    pass


def main():
    input_string = ("AA = Rickard Stark (M)        AB = Eddard Stark (M)         AC = Catelyn Tully (F) "
                    "AD = Brandon Stark (M)        AE = Benjen Stark (M)         AF = Jon Snow (M) "
                    "AG = Robb Stark (M)           AH = Sansa Stark (F)          AI = Arya Stark (F) "
                    "AJ = Bran Stark (M)           AK = Rickon Stark (M)         AL = Hoster Tully (M) "
                    "AM = Minisa Whent (F)         AN = Edmure Tully (M)         AO = Lysa Tully (F) "
                    "AP = Jon Arryn (M)            AQ = Robert Arryn (M)         AR = Tytos Lannister (M) "
                    "AS = Tywin Lannister (M)      AT = Joanna Lannister (F)     AU = Kevan Lannister (M) "
                    "AV = Cersei Lannister (F)     AW = Jamie Lannister (M)      AX = Tyrion Lannister (M) "
                    "AY = Robert Baratheon (M)     AZ = Joffrey Baratheon (M)    BA = Myrcella Baratheon (F) "
                    "BB = Tommen Baratheon (M)     BC = Lancel Lannister (M)     BD = Steffon Baratheon (M) "
                    "BE = Stannis Baratheon (M)    BF = Selyse Florent (F)       BG = Shireen Baratheon (F) "
                    "BH = Renly Baratheon (M)      BI = Jaehaerys Targaryen (M)  BJ = Aerys Targaryen (M) "
                    "BK = Rhaella Targaryen (F)    BL = Rhaegar Targaryen (M)    BM = Elia Martell (F) "
                    "BN = Rhaenys Targaryen (F)    BO = Aegon Targaryen (M)      BP = Viserys Targaryen (M) "
                    "BQ = Daenerys Targaryen (F)   BR = Quellon Greyjoy (M)      BS = Balon Greyjoy (M) "
                    "BT = Euron Greyjoy (M)        BU = Victarion Greyjoy (M)    BV = Urrigon Greyjoy (M) "
                    "BW = Aeron Greyjoy (M)        BX = Rodrik Greyjoy (M)       BY = Maron Greyjoy (M) "
                    "BZ = Asha Greyjoy (F)         CA = Theon Greyjoy (M)        CB = Alannys Harlaw (F) "
                    "--------------------------------------------------------------------------------------- "
                    "AA->AB, AA->AD, AA->AE, AB->AF, AB->AG, AB->AH, AB->AI, AB->AJ, AB->AK, AC->AG, "
                    "AC->AH, AC->AI, AC->AJ, AC->AK, AL->AC, AL->AN, AL->AO, AM->AC, AM->AN, AM->AO, "
                    "AO->AQ, AP->AQ, AR->AS, AR->AU, AS->AV, AS->AW, AS->AX, AT->AV, AT->AW, AT->AX, "
                    "AU->BC, AV->AZ, AV->BA, AV->BB, AY->AZ, AY->BA, AY->BB, BD->AY, BD->BE, BD->BH, "
                    "BE->BG, BF->BG, BI->BJ, BI->BK, BJ->BL, BJ->BP, BJ->BQ, BK->BL, BK->BP, BK->BQ, "
                    "BL->BN, BL->BO, BM->BN, BM->BO, BR->BS, BR->BT, BR->BU, BR->BV, BR->BW, BS->BX, "
                    "BS->BY, BS->BZ, BS->CA, CB->BX, CB->BY, CB->BZ, CB->CA")

    data = extract_data(input_string)
    print(ancestors(data, "Daenerys Targaryen"))
    print(descendants(data, "Jaehaerys Targaryen"))
    print(siblings(data, "Jon Snow", gender=None, fullness=0))
    print(parents_siblings(data, "Joffrey Baratheon", gender=None))
    print(cousins(data, "Jamie Lannister"))


if __name__ == "__main__":
    main()
