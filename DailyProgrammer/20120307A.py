"""
Challenge #19 will use The Adventures of Sherlock Holmes [https://www.gutenberg.org/cache/epub/1661/pg1661.txt] from
Project Gutenberg [https://www.gutenberg.org/].

Write a program that counts the number of alphanumeric characters there are in The Adventures of Sherlock Holmes.
Exclude the Project Gutenberg header and footer, book title, story titles, and chapters. Post your code and the
alphanumeric character count.
"""

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
chapter_strip = re.compile("([IVX]+\. THE ADVENTURE.*?\n)|(ADVENTURE [IVX]+\..*?\n)|(\n[IVX]+\.\n)", re.DOTALL)
txt = chapter_strip.sub('', txt.group())

# Strip every non-alphanumeric character
alphanum_strip = re.compile("[\W]+", re.DOTALL)
txt = alphanum_strip.sub('', txt)

print(len(txt))
