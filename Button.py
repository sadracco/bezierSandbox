import pygame as pg

class Button:
    def __init__(self, x, y, w, h, ac, screen, color=(255,255,255)):
        self.padding = 8
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.act = ac
        self.state = False
        self.screen = screen

    def action(self):
        if not self.state:
            self.act()

    def draw(self):
        p = self.padding
        pg.draw.rect(self.screen, self.color, (self.x+p,self.y+p,self.w-p,self.h-p))
