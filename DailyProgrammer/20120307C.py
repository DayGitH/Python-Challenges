# -*- coding: utf-8 -*-
'''
Challenge #19 will use The Adventures of Sherlock Holmes [https://www.gutenberg.org/cache/epub/1661/pg1661.txt] from
Project Gutenberg [https://www.gutenberg.org/].

Write a program that will build and output a word index for The Adventures of Sherlock Holmes. Assume one page contains
40 lines of text as formatted from Project Gutenberg's site. There are common words like "the", "a", "it" that will
probably appear on almost every page, so do not display words that occur more than 100 times.

Example Output: the word "abhorrent" appears once on page 1, and the word "medical" appears on multiple pages, so the
output for this word would look like:
abhorrent: 1
medical: 34, 97, 98, 130, 160
Exclude the Project Gutenberg header and footer, book title, story titles, and chapters.
'''
import re

with open('20120307.txt', 'r') as f:
    text = f.read()

# Remove header and footer
window_strip = re.compile(r"(?<=[\n]{10}).*(?=[\n]{10})", re.DOTALL)
txt = window_strip.search(text)

# Remove glossary
content_strip = re.compile(r"(?<=[\n]{5}).*", re.DOTALL)
txt = content_strip.search(txt.group())

# Remove story and chapter titles
chapter_strip = re.compile(r"([IVX]+\. THE ADVENTURE.*?\n)|(ADVENTURE [IVX]+\..*?\n)|(\n[IVX]+\.\n)", re.DOTALL)
txt = chapter_strip.sub('', txt.group())

# split into 40 line strings
txt = txt.split('\n')
span = 40
txt = ["\n".join(txt[i:i+span]) for i in range(0, len(txt), span)]

#remove everything except letters and spaces
alpha_strip = re.compile(r"[^a-zA-Z\s]+", re.DOTALL)
for p in range(len(txt)):
    txt[p] = txt[p].replace('\n', ' ')
    txt[p] = alpha_strip.sub('', txt[p])

# blacklist holds words that occur more than 100 times and need not be counted
# whitelist is a dictionary that holds the word as the key and a list of page numbers as values
blacklist = []
whitelist = {}
for n, p in enumerate(txt, start=1):
    # split pages into words
    working_string = p.split(' ')
    for w in working_string:
        # check if word is in blacklist
        if w.lower() in blacklist:
            continue
        #check if word is in whitelist; if yes add to it, if too many added remove and add to blacklist
        elif w.lower() in whitelist:
            # print(w.lower(), n)
            whitelist[w.lower()].append(n)
            if len(whitelist[w.lower()]) > 100:
                blacklist.append(w.lower())
                del whitelist[w.lower()]
        # if not in whitelist, add to whitelist
        else:
            whitelist[w.lower()] = [n]

# print result
for i in sorted(whitelist):
    print(i, whitelist[i])