'''
Welcome to cipher day!
For this challenge, you need to write a program that will take the scrambled words from this post, and compare them
against THIS WORD LIST [http://pastebin.com/jSD873gL] to unscramble them. For bonus points, sort the words by length
when you are finished. Post your programs and/or subroutines!

Here are your words to de-scramble:
mkeart
sleewa
edcudls
iragoge
usrlsle
nalraoci
nsdeuto
amrhat
inknsy
iferkna
'''

# def strip_nonalpha(wordlist):
# ''' Removes newline from words and words with non-alpha characters '''
#     ''' Goes through list backwards, so that pop() doesn't unsync index
#     for i in range(len(wordlist)-1,-1,-1):
#         wordlist[i] = wordlist[i].replace('\n','')
#         if not wordlist[i].isalpha():
#             # print(wordlist[i])
#             wordlist.pop(i)
#     return wordlist

scrambled = ['mkeart', 'sleewa', 'edcudls', 'iragoge', 'usrlsle', 'nalraoci', 'nsdeuto', 'amrhat', 'inknsy', 'iferkna']

with open('wordlist.txt', 'r') as f:
    wordlist = list(f)

# wordlist = strip_nonalpha(wordlist)

for s in scrambled:
    for i in wordlist:
        ''' Original code, commented out '''
        # ''' compare length of sets and common letters '''
        # if (len(set(s).intersection(i)) == len(list(set(s)))) and (len(s) == len(i)):
        #     ''' holding variables to allow manipulation of characters '''
        #     hold_s, hold_i = s, i
        #     for l_s in range(len(hold_s)):
        #         for l_i in range(len(hold_i)):
        #             if hold_s[l_s] == hold_i[l_i]:
        #                 ''' replace common letters with zero '''
        #                 hold_s = hold_s.replace(hold_s[l_s],'0',1)
        #                 hold_i = hold_i.replace(hold_i[l_i],'0',1)
        #     ''' filter out zeros, if nothing left, that means they are anagrams '''
        #     if len((list(filter(('0').__ne__, hold_i)))) == 0:
        #         print(s, i)

        ''' Genius idea from another user. Sort the characters before comparing '''
        if sorted(s) == sorted(i.replace('\n', '')):
            print(s, i.replace('\n', ''))