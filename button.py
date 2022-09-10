# button.py
from graphics import *

class Button:

    def __init__(self, win, center, width, height, label):
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill(color_rgb(250,203,221))
        self.rect.setOutline(color_rgb(237,73,151))
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)

    def clicked(self, p):
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill(color_rgb(237,73,151))
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        self.rect.setFill(color_rgb(236,189,207))
        self.rect.setWidth(1)
        self.active = False
      
