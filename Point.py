import pygame as pg
import pygame.gfxdraw

class Point:
    def __init__(self, x, y, color, screen):
        self.x = x
        self.y = y
        self.pos = (x,y)
        self.r = 12
        self.color = color
        self.drag = False
        self.screen = screen

    def draw(self):
        if self.drag:
            self.draging()
        pg.gfxdraw.aacircle(self.screen, self.pos[0], self.pos[1], self.r, self.color)
        pg.gfxdraw.filled_circle(self.screen, self.pos[0], self.pos[1], self.r, self.color)

    def draging(self):
        self.x = pg.mouse.get_pos()[0]
        self.y = pg.mouse.get_pos()[1]
        self.pos = pg.mouse.get_pos()
