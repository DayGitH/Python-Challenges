"""
Draw a line... except it must be your implementation of a line using only the ability to draw a point. Think
implementing a line is too easy? Try it :). You can output the result in ASCII text if you'd like instead of using a
graphics library. A successful implementation will be able to draw this[https://i.imgur.com/a8LuR.jpg] . Only being
able to draw horizontal, vertical, and diagonal lines is not enough, and the lines can't contain any holes. Also, if
you're drawing a line (I'll use drawLine(x1, y1, x2, y2) as an example) using the following call: drawLine(100, 10,
200, 300), then the following call must draw the same line: drawLine(200, 300, 100, 10).
"""

import pygame
import pygame.gfxdraw
from math import sin, cos

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
width = 400
height = 300

def nova_line(screen, x0, y0, x1, y1):
    if x1 >= x0 and y1 >= y0:
        x, x_end = [x0], x1
        y, y_end = [y0], y1
    elif x1 <= x0 and y1 >= y0:
        x, x_end = [x1], x0
        y, y_end = [y1], y0
    elif x1 >= x0 and y1 <= y0:
        x, x_end = [x0], x1
        y, y_end = [y0], y1
    elif x1 <= x0 and y1 <= y0:
        x, x_end = [x1], x0
        y, y_end = [y1], y0

    # x = x1 if x0 > x1 else x0
    # y = y1 if y0 > y1 else y0
    m = (y1 - y0) / (x1 - x0)
    c = y[0] - (m * x[0])

    while True:
        x.append(x[-1] + 0.1)
        y.append((m * x[-1]) + c)

        if x[-1] > x_end or y[-1] > y_end:
            return x, y


        # pygame.gfxdraw.pixel(screen, int(x), int(y), BLACK)


if __name__ == '__main__':
    done = False

    pygame.init()

    screen = pygame.display.set_mode([width, height])
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(WHITE)

        pygame.gfxdraw.pixel(screen, 230, 230, BLACK)
        x_list, y_list = nova_line(screen, 50, 50, 300, 250)

        for n in range(len(x_list)):
            pygame.gfxdraw.pixel(screen, int(x_list[n]), int(y_list[n]), BLACK)

        pygame.display.flip()
        clock.tick(60)