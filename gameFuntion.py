import pygame as pg
import random as rd


def draw_all_the_sprites(sprites_group, screen):
    # draw all the sprites in the group onto the screen
    for i in sprites_group:
        screen.blit(i.surf, i.rect)

def update_bullet(bullets, Bricksgroup, screen):
    for i in bullets:
        i.update(5, Bricksgroup, screen)

def update_brick(bricks, screen):
    for i in bricks:
        i.update(1, screen)


#def update_tank(tank, Bricksgroup):
    #if tank.collision(Bricksgroup):


def countBullet(sprites_group):
    a = 0
    for i in sprites_group:
        a += 1
    return a

def get_a_pos_for_bricks(a):
    # a is the number of bricks you want to generate
    def check_distance(new, tuple):
        for i in tuple:
            if abs(new - i) < 70:
                return False
        return True

    xset = set()
    poslist = []
    while len(xset) != a:
        newX = rd.randint(100, 800)
        if check_distance(newX, xset):
            xset.add(newX)

    for i in xset:
        poslist.append((i, 20))
    return poslist
    



def get_random_amount_of_bricks():
    return rd.randint(1, 3)

#This function returns boolean
# input 'degree' can be 1...5
def setMagicBrick_chance(degree):
    return rd.randint(0, 10) in range(degree)

def setBoomBrick_chance(degree):
    return rd.randint(0, 15) in range(degree)

def crash(screen):
    while True:

        surf = pg.image.load('gameover.png')
        screen.blit(surf, (50, 150))
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        
        