"""
This one is inspired by an actual problem my friend had to deal with recently. Unfortunately, its a little bit
keyboard-locale specific, so if you don't happen to use a us-EN layout keyboard you might want to get a picture of one.

The en-us keyboard layout pictured here [http://en.wikipedia.org/wiki/File:KB_United_States-NoAltGr.svg] is one common
layout for keys. There are character-generating keys such as '1' and 'q', as well as modifier keys like 'ctrl' and
'shift', and 'caps-lock'

If one were to press every one of the character-generating keys in order from top to bottom left-to-right, you would get
the following string:

`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./

plus the whitespace characters TAB,RETURN,SPACE.

Your job is to write a function that takes in a character representing a keypress, as well as a boolean for each
'modifier' key like ctrl,alt,shift,and caps lock, and converts it properly into the ascii character for which the key
gets output.

For example, my python implementation keytochar(key='a',caps=True) returns 'A'. However,
keytochar(key='a',caps=True,shift=True) returns 'a'.

BONUS: Read in a string containing a record of keypresses and output them to the correct string. A status key change is
indicated by a ^ character..if a ^ character is detected, then the next character is either an 's' or 'S' for shift
pressed or shift released, respectively, a 'c' or 'C' for caps on or caps off respectively, and a 't' 'T' for control
down or up, and 'a' 'A' for alt down or up.

For example on the bonus, given the input

^sm^Sy e-mail address ^s9^Sto send the ^s444^S to^s0^S is ^cfake^s2^Sgmail.com^C

you should output

My e-mail address (to send the $$$ to) is FAKE@GMAIL.COM
"""


def key_to_char(key, caps=False, shift=False):
    key_dict = {'`': '~',  '1': '!', '2': '@', '3': '#', '4': '$', '5': '%', '6': '^',
                '7': '&',  '8': '*', '9': '(', '0': ')', '-': '_', '=': '+', '[': '{',
                ']': '}', '\\': '|', ';': ':', "'": '"', ',': '<', '.': '>', '/': '?'}
    if shift and key in key_dict:
        return key_dict[key]
    if shift ^ caps:
        return key.capitalize()
    else:
        return key


def keyboard_printer(string):
    caps = False
    shift = False
    mod = False
    for s in string:
        if s == '^':
            mod = True
            continue

        if mod:
            if s.lower() == 's':
                shift = not shift
            elif s.lower() == 'c':
                caps = not caps
            mod = False
            continue

        print(key_to_char(s, caps=caps, shift=shift), end='')


def main():
    keyboard_printer("^sm^Sy e-mail address ^s9^Sto send the ^s444^S to^s0^S is ^cfake^s2^Sgmail.com^C")


if __name__ == "__main__":
    main()
