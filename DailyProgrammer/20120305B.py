"""
Screen scraping involves interacting with the terminal display of a currently running program. There are commercial
screen scraping applications available for mainframe programs that provide a web interface on top of a dumb terminal
program.

Write a program that will read the following from a text file to simulate the dumb terminal program. Each line
represents a prompt to the user (always ends with a colon). Input constraints may be available for prompts. If they
are, then they will always be surrounded in parentheses. The accepted input values will always be separated by a comma,
and the value that is actually counted will be surrounded in square brackets.

Once you've parsed the text file, convert the data into an HTML form output file. If the prompt did not have any input
constraints, then the input type is just a text. If the prompt contained input constraints and there are less than 5
options, then the input type are radio buttons. If there are 5 or more possible input values, then the input type is a
dropdown.

Example:
Input File

Name:
Gender ([M]ale, [F]emale):
Position ([C]ashier, [D]eli Clerk, [M]anager, [P]roduce Clerk, [S]tock Person):

Output File (HTML)

<html>
<body>
<form>
Name:
<input type="text" name="name"/>
<br/>
Gender:
<input type="radio" name="gender" value="m"/> Male
<input type="radio" name="gender" value="f"/> Female
<br/>
Position:
<select name="position">
<option value="c">Cashier</option>
<option value="d">Deli Clerk</option>
<option value="m">Manager</option>
<option value="p">Produce Clerk</option>
<option value="s">Stock Person</option>
</select>
<br/>
<input type="submit" value="Submit"/>
</form>
</body>
</html>
"""

import re


with open('20120305B.txt') as f:
    read_data = f.read().split('\n')

# print(read_data)
data_list = []

for element in read_data:
    # print(element)
    working_list = []
    name, thing = element[:element.find(' ')], element[element.find('(') + 1: element.find(')')]
    working_list.append(name)

    if '[' in thing:
        thing = thing.split(', ')
        for t in thing:
            working_list.append([t[t.find('[')+1], "".join(re.findall("[a-zA-Z ]+", t))])
    data_list.append(working_list)

print(data_list)

with open('20120305B.html', 'w') as g:
    g.write('<html>\n')
    g.write('<body>\n')
    g.write('<form>\n')

    for data in data_list:
        if len(data) == 1:
            g.write(data[0] + ': ')
            g.write('<input type ="text" name="{}"/>\n'.format(data[0]))
            g.write('<br/>\n')
        elif len(data) < 5:
            name = data[0]
            for d in data:
                if type(d) is list:
                    g.write('<input type="radio" name="{}" value="{}"/> {}\n'.format(name, d[0], d[1]))
                else:
                    g.write(d + ':' + '\n')
            g.write('<br/>\n')
        else:
            name = data[0]
            for d in data:
                print(d)
                if type(d) is list:
                    g.write('<option value="{}">{}</option>\n'.format(d[0], d[1]))
                else:
                    g.write(d + ':' + '\n')
                    g.write('<select name="{}">\n'.format(d.lower()))
            g.write('</select>\n')
            g.write('<br/>\n')

    g.write('<input type="submit" value="submit"/>\n')
    g.write('</form>\n')
    g.write('</body>\n')
    g.write('</html>\n')