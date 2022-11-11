import pygame as pg
from gameloop import loop
pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('BjarneFN')
loop(pg, screen)