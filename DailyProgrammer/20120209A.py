'''
create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:

your name is (blank), you are (blank) years old, and your username is (blank)

for extra credit, have the program log this information in a file to be accessed later.
'''

if __name__ == '__main__':
    print('What is your name?')
    name = input('> ')

    print('How old are you?')
    age = 'x'
    while not isinstance(age, int):
        age = input('> ')
        try:
            age = int(age)
        except:
            print('Invalid age. Please try again')

    print('What is your username?')
    user = input('> ')

    print('\nYour name is {}, you are {} years old, and your username is {}'.format(name, age, user))

    file = open('userinfo.txt', 'w')

    file.write('Name:     {}\n'.format(name))
    file.write('Age:      {}\n'.format(age))
    file.write('UserName: {}\n\n'.format(user))

    file.close()