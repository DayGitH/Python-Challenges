'''
create a program that will remind you to stop procrastinating every two hours with a pop up message! :)

This program has the potential of helping many people :D
'''

import easygui, time

while True:
    time.sleep(2*60*60)
    easygui.msgbox("This is a message!", title="simple gui")