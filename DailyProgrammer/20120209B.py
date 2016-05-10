'''
create a program that will allow you to enter events organizable by hour. There must be menu options of some form, and
you must be able to easily edit, add, and delete events without directly changing the source code.
(note that by menu i dont necessarily mean gui. as long as you can easily access the different options and receive
prompts and instructions telling you how to use the program, it will probably be fine)
'''

live = True

class event():
    event_name = 'GEN_NAME'
    date = '19900101'
    hour = '00'

    def __init__(self, event_name, date, hour):
        self.event_name = event_name
        self.date = date
        self.hour = hour

    def update(self, parameter, value):
        if parameter == 'name':
            self.event_name = value
        elif parameter == 'date':
            self.date = value
        elif parameter == 'hour':
            self.hour = value

    def get_hour(self):
        return self.hour

    def get_date(self):
        return self.date

    def get_eventname(self):
        return self.event_name

eList = {1 : event('Generic Event', '20150128', '15'),
         2 : event('Generic Event 2', '20140305', '13'),
         3 : event('Generic Event 3', '20081212', '04'),
         4 : event('Generic Event 4', '19910527', '01'),
         5 : event('Generic Event 5', '19210527', '11')}
while live:
    for i in eList:
        print(i, '\t', eList[i].get_hour(), '\t', eList[i].get_date(), '\t', eList[i].get_eventname())

    print('1. Add Event')
    print('2. Edit Event')
    print('3. Delete Event')
    print('4. Exit program')

    mode = int(input('> '))

    if mode == 1:
        print('Enter event name:')
        name = input('> ')
        print('Enter event date:')
        date = input('> ')
        print('Enter event hour:')
        hour = input('> ')

        eList[len(eList) + 1] = event(name,date,hour)

    elif mode == 2:
        print('Choose the event you wish to update from the list above:')
        event_number = int(input('> '))

        print('Update name (leave empty for current value):')
        name = input('> ')
        print('Update date (leave empty for current value):')
        date = input('> ')
        print('Update hour (leave empty for current value):')
        hour = input('> ')

        if name != '':
            eList[event_number].update('name', name)
        if date != '':
            eList[event_number].update('date', date)
        if hour != '':
            eList[event_number].update('hour', hour)

    elif mode == 3:
        print('Choose the event you wish to update from the list above:')
        event_number = int(input('> '))

        del eList[event_number]

        if len(eList) >= event_number:
            for i in range(event_number, len(eList)+1):
                eList[i] = eList.pop(i+1)

    elif mode == 4:
        live = False