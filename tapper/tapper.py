import pygame as pg
from sys import exit

pg.init()

width, height = 1000, 800
TITLE = "Tapper"

screen = pg.display.set_mode((width, height))
pg.display.set_caption(TITLE)

def get_sprite(x, y):
    sprite_sheet = pg.image.load("./sprites/Bartender.png").convert_alpha()
    rect = pg.Rect(x, y, 33, 66)
    image = pg.Surface((66, 66), pg.SRCALPHA)
    image.blit(sprite_sheet, (0, 0), rect)
    
    return image

class Bancone:
    def __init__(self):
        # self.clienti = 
        pass

def main():
    color_key = (0, 48, 80)
    sprites = []
    
    sprite = get_sprite(0, 66)
    sprite.set_colorkey(color_key)
    sprites.append(sprite)

    running = True
    while running:
        screen.fill((0, 0, 0))
        for i, sprite in enumerate(sprites):
            screen.blit(sprite, (i * 40, 50))
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                exit()

main()