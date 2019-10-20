import pygame as pg
import pygame.gfxdraw

class Curve:
    def __init__(self, po, screen):
        self.res = 100
        self.points = po
        self.color = (244, 191, 66)
        self.style = False
        self.w = 4
        self.struct= []
        self.change = True
        self.generate(self.points)
        self.change = False
        self.screen = screen

    def generate(self, pnts):
        if not self.change:
            return
        self.struct = []
        self.points = pnts
        if len(self.points) < 4:
            x1, y1 = self.points[0].pos
            x2, y2 = self.points[1].pos
            x3, y3 = self.points[2].pos 
            for i in range(self.res):
                cx1 = x1*((1-i/100)**2)
                cx2 = 2*x2*(1-i/100)*(i/100)
                cx3 = x3*((i/100)**2)
                cy1 = y1*((1-i/100)**2)
                cy2 = 2*y2*(1-i/100)*(i/100)
                cy3 = y3*((i/100)**2)
                self.struct.append((int(cx1+cx2+cx3), int(cy1+cy2+cy3)))
            return

        x1, y1 = self.points[0].pos
        x2, y2 = self.points[1].pos
        x3 = self.points[1].x - (self.points[1].x - self.points[2].x)/2
        y3 = self.points[1].y - (self.points[1].y - self.points[2].y)/2
        for i in range(self.res):
            cx1 = x1*((1-i/100)**2)
            cx2 = 2*x2*(1-i/100)*(i/100)
            cx3 = x3*((i/100)**2)
            cy1 = y1*((1-i/100)**2)
            cy2 = 2*y2*(1-i/100)*(i/100)
            cy3 = y3*((i/100)**2)
            self.struct.append((int(cx1+cx2+cx3), int(cy1+cy2+cy3)))

        for i in range(2, len(self.points)-2):
            x1 = self.points[i-1].x - (self.points[i-1].x - self.points[i].x)/2
            y1 = self.points[i-1].y - (self.points[i-1].y - self.points[i].y)/2
            x2, y2 = self.points[i].pos
            x3 = self.points[i+1].x + (self.points[i].x - self.points[i+1].x)/2
            y3 = self.points[i+1].y + (self.points[i].y - self.points[i+1].y)/2
            for i in range(self.res):
                cx1 = x1*((1-i/100)**2)
                cx2 = 2*x2*(1-i/100)*(i/100)
                cx3 = x3*((i/100)**2)
                cy1 = y1*((1-i/100)**2)
                cy2 = 2*y2*(1-i/100)*(i/100)
                cy3 = y3*((i/100)**2)
                self.struct.append((int(cx1+cx2+cx3), int(cy1+cy2+cy3)))

        x1 = self.points[-3].x - (self.points[-3].x - self.points[-2].x)/2
        y1 = self.points[-3].y - (self.points[-3].y - self.points[-2].y)/2
        x2, y2 = self.points[-2].pos
        x3, y3 = self.points[-1].pos
        for i in range(self.res):
            cx1 = x1*((1-i/100)**2)
            cx2 = 2*x2*(1-i/100)*(i/100)
            cx3 = x3*((i/100)**2)
            cy1 = y1*((1-i/100)**2)
            cy2 = 2*y2*(1-i/100)*(i/100)
            cy3 = y3*((i/100)**2)
            self.struct.append((int(cx1+cx2+cx3), int(cy1+cy2+cy3)))

    def drawPoint(self):
        for point in self.struct:
            pg.gfxdraw.aacircle(self.screen, point[0], point[1], int(self.w/2), self.color)
            pg.gfxdraw.filled_circle(self.screen, point[0], point[1], int(self.w/2), self.color)

    def drawLine(self):
        for i in range(len(self.struct)-1):
            pg.draw.aaline(self.screen, self.color, self.struct[i], self.struct[i+1], self.w)
