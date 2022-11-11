import pygame

bin_image = pygame.image.load('bin.png')

speed = 2

def Movement(pygame, x,y):
    keys = pygame.key.get_pressed()
    file='player.png'
    if keys[pygame.K_w]:
        y-=speed
    elif keys[pygame.K_s]:
        y+=speed
    elif keys[pygame.K_d]:
        x+=speed
    elif keys[pygame.K_a]:
        x-=speed
    x,y = borders(x, y)
    return x,y,file

def borders(x, y):
    if x >= 650:
        x = 650
    elif x <= -16:
        x = -16
    if y <= 10:
        y=10
    elif y >= 440:
        y=440
    return x,y