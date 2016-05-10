"""
Create a program that will take any string and write it out to a text file, reversed.
input: "hello!"
output: "!olleh"
"""

with open('20120221B.txt', 'w') as f:
    f.write(input('Enter string: ')[::-1])

print('DONE')

# found better version
# open('20120221B.txt', 'w').write(input('Enter string: ')[::-1])
