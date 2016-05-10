"""
Your mission is to create a stopwatch program. this program should have start, stop, and lap options, and it should
write out to a file to be viewed later.
"""

import time
import os
import pygame


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

screen_width = 300
screen_height = 400
text_posx = 0
text_posy = 40

'''
Possible states include:
     start
     active
     lap
     stop
     reset
'''
state = 'stop'

class textbox():
    x = 0
    y = 0
    waqt = '0'
    text = '0'
    text_size = 25
    font = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont('Calibri', self.text_size, True, False)

    def update(self, screen, waqt):
        self.waqt = waqt
        text =  self.font.render(self.waqt,True,BLACK)
        screen.blit(text, [self.x, self.y])

    def textsize(self, text_size):
        self.text_size = text_size

def time_format(sec):
    milliseconds = int((sec % 1) * 1000)

    sec = int(sec)
    seconds = sec % 60
    minutes = (sec % 3600) // 60  # 60
    hours = (sec % 86400) // 3600  # 60 * 60
    days = sec // 86400  # 24 * 60 * 60

    string = str(days).zfill(4) + ":" + str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2) + ":"  +str(milliseconds).zfill(3)
    return string

pygame.init()
laptext = {}

screen = pygame.display.set_mode([screen_width, screen_height])
textnum = textbox(0, 0)
clock = pygame.time.Clock()

go = False
exit = False
start_time = 0
lap_list = [0]
restart_flag = False

file = open('log.txt', 'a')
file.write('New log\n')

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                go = True
                if state == 'stop':
                    state = 'start'
                elif state == 'active':
                    state = 'lap'
                else:
                    pass
            elif event.key == pygame.K_RSHIFT and state == 'active':
                go = True
                state = 'stop'
            elif event.key == pygame.K_r and state == 'stop':
                go = True
                print('r')
                state = 'reset'
        elif event.type == pygame.QUIT:
            exit = True

    screen.fill(WHITE)

    if go:
        go = False
        if state == 'start':
            if not restart_flag:
                start_time = time.clock()
                restart_flag = True
            else:
                '''
                start_time added twice
                Once to compensate for non-zero start-time
                Second to uncompensate the lap-time to absolute time
                '''
                start_time += time.clock() - (lap_list[-1]+start_time)
            state = 'active'
        elif state == 'lap':
            lap_list.append(time.clock() - start_time)
            print('lap')
            laptext[len(lap_list)] = textbox(text_posx,text_posy)
            text_posy += 40
            state = 'active'
        elif state == 'stop':
            lap_list.append(time.clock() - start_time)
            laptext[len(lap_list)] = textbox(text_posx,text_posy)
            text_posy += 40
            print('stop')
        elif state == 'reset':
            for i in lap_list:
                file.write(time_format(i) + '\n')
            file.write('\n')
            start_time = 0
            lap_list = [0]
            laptext = {}
            state = 'stop'
            restart_flag = False
            text_posy = 40

    if state == 'active':
        textnum.update(screen, time_format(time.clock()-start_time))#-restart_offset
    elif len(lap_list) > 0:
        textnum.update(screen, time_format(lap_list[-1]))
    else:
        textnum.update(screen, time_format(0))

    for i in range(2,len(lap_list)+1):
        laptext[i].update(screen, time_format(lap_list[i-1]))

    pygame.display.flip()

    clock.tick(60)

for i in lap_list:
    file.write(time_format(i) + '\n')
file.write('\n')

file.close()
pygame.quit()