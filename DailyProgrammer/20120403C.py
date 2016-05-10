"""
The objective of this exercise is to maintain a list of Strings in memory that support undo and redo. Write a program
that allows the user to add, edit, delete, undo, and redo entries in a list. You must be able to undo and redo
everything you've done during the execution of this program. After each command is run, always print out the list
(unless you're doing this in a UI). Before writing any code, first think about how to write add, edit, and remove with
undo and redo in mind. If there are no submissions to this post, I'll reply with some hints.

Sample Run:
Enter command ('A'dd, 'E'dit, 'D'elete, 'U'ndo, 'R'edo): A
Enter text to add: Venus
Venus
Enter command ('A'dd, 'E'dit, 'D'elete, 'U'ndo, 'R'edo): A
Enter text to add: Mars
Venus
Mars
Enter command ('A'dd, 'E'dit, 'D'elete, 'U'ndo, 'R'edo): U
Venus
Enter command ('A'dd, 'E'dit, 'D'elete, 'U'ndo, 'R'edo): U
Enter command ('A'dd, 'E'dit, 'D'elete, 'U'ndo, 'R'edo): R
Venus
Enter command ('A'dd, 'E'dit, 'D'elete, 'U'ndo, 'R'edo): R
Venus
Mars
Enter command ('A'dd, 'E'dit, 'D'elete, 'U'ndo, 'R'edo): A
Enter text to add: Saturn
Venus
Mars
Saturn
Enter command ('A'dd, 'E'dit, 'D'elete, 'U'ndo, 'R'edo): E
Enter index to edit: 1
Enter text to edit: Earth
Venus
Earth
Saturn
Enter command ('A'dd, 'E'dit, 'D'elete, 'U'ndo, 'R'edo): U
Venus
Mars
Saturn
Enter command ('A'dd, 'E'dit, 'D'elete, 'U'ndo, 'R'edo): R
Venus
Earth
Saturn
Enter command ('A'dd, 'E'dit, 'D'elete, 'U'ndo, 'R'edo): D
Enter index to delete: 2
Venus
Earth
Enter command ('A'dd, 'E'dit, 'D'elete, 'U'ndo, 'R'edo): U
Venus
Earth
Saturn
Enter command ('A'dd, 'E'dit, 'D'elete, 'U'ndo, 'R'edo): R
Venus
Earth
"""

mem = []
undo = []
redo = []

while True:
    cmd = input("Enter command ('A'dd, 'E'dit, 'D'elete, 'U'ndo, 'R'edo, e'X'it): ").upper()

    if cmd == 'A':
        txt = input('Enter text to add: ')
        mem.append(txt)
        undo.append('A_' + txt)

    elif cmd == 'E':
        index = int(input('Enter index to edit: '))
        txt = input('Enter text to edit: ')
        temp = mem[index]
        mem[index] = txt
        undo.append('E_' + str(index) + '_' + temp + '_' + txt)

    elif cmd == 'D':
        index = int(input('Enter index to delete: '))
        undo.append('D_' + str(index) + '_' + mem[index])
        del mem[index]

    elif cmd == 'U':
        u = undo.pop()
        redo.append(u)
        u = u.split('_')

        if u[0] == 'A':
            mem.remove(u[1])
        elif u[0] == 'E':
            mem[int(u[1])] = u[2]
        elif u[0] == 'D':
            mem.insert(int(u[1]), u[2])

    elif cmd == 'R':
        r = redo.pop()
        undo.append(r)
        r = r.split('_')

        if u[0] == 'A':
            mem.append(r[1])
        elif u[0] == 'E':
            mem[int(r[1])] = r[3]
        elif u[0] == 'D':
            del mem[int(r[1])]

    elif cmd == 'X':
        print('Ending')
        break

    else:
        print('Invalid command. Please try again.')

    for m in mem:
        print(m)

    print('\n')
