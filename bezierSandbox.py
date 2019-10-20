from random import randint

import pygame as pg
import pygame.gfxdraw
from pygame.locals import *

from Button import Button
from Point import Point
from Curve import Curve

pg.init()
pg.display.set_caption('Bezier Sandbox')
clock = pg.time.Clock()

width = 1000
heigth = 700
screen = pg.display.set_mode((width, heigth))

BLUE = (58, 234, 193)
YELLOW = (244, 191, 66)
RED = (234, 87, 58)
GREY = (50, 50, 50)
GREEN = (125, 244, 66)

on = True


def conPoints(pnts, wid=4):
    for i in range(len(pnts)-1):
        pg.draw.aaline(screen, GREY, pnts[i].pos, pnts[i+1].pos, wid)

def addPoint():
    points.append(Point(randint(200, 800), randint(100, 600), BLUE, screen))
    curve.change = True
    curve.generate(points)
    curve.change = False
    
def remPoint():
    if len(points) > 3:
        points.pop()
        curve.change = True
        curve.generate(points)
        curve.change = False

def lessW():
    if curve.w > 2:
        curve.w-= 1

def moreW():
    curve.w+= 1

def changeStyle():
    curve.style = not curve.style

points = []
buttons = []
for i in range(3):
    points.append(Point(randint(200, 800), randint(100, 600), BLUE, screen))

buttons.append(Button(0, 0, 100, 40, addPoint, screen, GREEN))
buttons.append(Button(0, 40, 100, 40, remPoint, screen, RED))
buttons.append(Button(0, 80, 100, 40, changeStyle, screen, GREY))
buttons.append(Button(0, 120, 50, 40, moreW, screen, GREY))
buttons.append(Button(50, 120, 50, 40, lessW, screen, GREY))
    
curve = Curve(points, screen)

while(on):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            on = False
            quit()
            pg.quit()

        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            for point in points:
                if(((event.pos[0]-point.pos[0])**2 + (event.pos[1]-point.pos[1])**2)**(.5)<=point.r):
                    point.drag = True
                    curve.change = True

            for button in buttons:
                if(button.x < event.pos[0] < button.x + button.w and button.y < event.pos[1] < button.y +  button.h):
                    button.state = True
                    button.act()

        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            curve.change = False
            for point in points:
                point.drag = False
            for button in buttons:
                button.state = False

    screen.fill((5, 5, 5))
    conPoints(points, wid=4)
    curve.generate(points)
    
    if curve.style:
        curve.drawLine()
    else:
        curve.drawPoint()
    
    for point in points:
        point.draw()
    for button in buttons:
        button.draw()

    pg.display.flip()
    clock.tick(60)
