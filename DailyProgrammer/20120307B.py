"""
Challenge #19 will use The Adventures of Sherlock Holmes [https://www.gutenberg.org/cache/epub/1661/pg1661.txt] from
Project Gutenberg [https://www.gutenberg.org/].

The Adventures of Sherlock Holmes is composed of 12 stories. Write a program that counts the number of words in each
story. Then, print out the story titles ordered by its word count in descending order followed by how many words each
story contains. Exclude the Project Gutenberg header and footer, book title, story titles, and chapters.
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

# Remove chapter titles from first story
chapter_strip = re.compile(r"(\n[IVX]+\.\n)", re.DOTALL)
txt = chapter_strip.sub('', txt.group())

# Iterate over search for Story headers to find story start and end indexes and find difference to find the location
# of story. Then split on spaces and count to get result.
story_strip = re.compile("([IVX]+\. THE ADVENTURE.*?(?=\n))|(ADVENTURE [I|V|X]+\..*?(?=\n))", re.DOTALL)
end = 0

for m in story_strip.finditer(txt):
    print(len(txt[end:m.start()].split()))
    print(m.group(), end=': ')
    end = m.end()

print(len(txt[end:].split()))
