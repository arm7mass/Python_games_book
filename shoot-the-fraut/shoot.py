from random import randint
from pgzero.builtins import Actor, animate, keyboard

import pygame as pg
    
    
screen = pg.display.set_mode((640, 480))


apple = Actor("apple")

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("good shot")
        place_apple()
    else:
        print("You missed it ")
        quit()

place_apple()