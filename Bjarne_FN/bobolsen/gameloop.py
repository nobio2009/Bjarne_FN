import pygame as pg
from random import randint
from movement import Movement
from colors import *
from save import *

def is_collided_with(self, sprite): return self.colliderect(sprite)

def spawn_trash():
    trashes=[]
    for i in range(10):
            trashes.append(
                (randint(200,590), 
            randint(50, 400))
        )
    return trashes

# Font
# Score
def loop(pygame : pg, screen : pg.Surface):
    background = pg.image.load('background.png')
    def save(a, b):
        f = open("save.py", "w")
        f.write(f"saved_point = {a}" + "\n")
        f.write(f"saved_upgrade = {b}" + "\n")
        f.close()

    font = pygame.font.Font('font.ttf', 32)

    point = saved_point

    trash_count = 0

    trash_max = 1

    def show_score(x, y):
        score = font.render(f'Score:{str(point)} Backpack:{str(trash_count)}/{str(trash_max)} - Made by: Noa, Bertil, Emil', True, (255, 255, 255))
        screen.blit(score, (x, y))

    textX = 10
    textY = 10

    player_file = ''

    player_image = pg.image.load('player.png')

    shp_image = pg.image.load('shp.png')

    bin_image = pg.image.load('bin.png')

    trash_image = pg.image.load('trash.png')
    trash_image = pygame.transform.scale(trash_image, (60,60))

    loop = True
    trash = False
    
    x = 8
    y = 278

    upgrade = saved_upgrade
        
    trashes = spawn_trash()


    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save(point, upgrade)
                loop = False
                exit()

        x,y,player_file = Movement(pygame, x,y)

        if trash == True:
            player_file = 'player_trash.png'
        if upgrade > 0:
            player_file = 'player_backpack_'+str(upgrade)+'.png'
        screen.blit(background, (0, 10))
        bin_sprite = screen.blit(bin_image, (10, 450))

        shp_sprite = screen.blit(shp_image, (600, 450))

        player_sprite = screen.blit(pygame.image.load(player_file), (x,y))

        for i in trashes:
            trash_sprite = screen.blit(trash_image, i)
            print(trash_count, trash_max)
            if is_collided_with(trash_sprite, player_sprite) and trash_count != trash_max:
                trashes.remove(i)
                trash = True
                trash_count += 1
                
        if trash == True and is_collided_with(player_sprite,bin_sprite):
            if len(trashes) == 0: trashes = spawn_trash()
            point += trash_count
            trash_count = 0
            trash=False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_e] and is_collided_with(player_sprite, shp_sprite):
            if upgrade == 0 and point >= 10:
                point = point -10
                upgrade += 1
                trash_max = 2
            elif upgrade == 1 and point >= 15:
                point = point -15
                upgrade += 1
                trash_max = 3
            elif upgrade == 2 and point >= 25:
                point = point -25
                upgrade += 1
                trash_max = 4

        show_score(textX, textY)
        pygame.display.flip()
        pygame.display.update()