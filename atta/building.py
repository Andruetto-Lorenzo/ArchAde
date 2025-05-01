import pygame as pg

pg.init()

#dimensioni della finestra
WIDTH, HEIGHT = 1800, 930
screen = pg.display.set_mode((WIDTH, HEIGHT))

#class per il building
class Building:
    def __init__(self):
        self.brick = pg.image.load('building/building_brick.png')
        self.build_bottom = pg.image.load('building/building_cement_bottom.png')
        self.build_top = pg.image.load('building/building_cement_top.png')
        self.build_ledge = pg.image.load('building/building_ledge.png')
        self.door_fixed = pg.image.load('door/door_fixed.png') 
        self.initialize_building()

    def initialize_building(self):
        self.brick = pg.transform.scale(self.brick, (900, 225))
        self.build_bottom = pg.transform.scale(self.build_bottom, (900, 225))
        self.build_top = pg.transform.scale(self.build_top, (900, 225))
        self.build_ledge = pg.transform.scale(self.build_ledge, (900, 30))
        self.door_fixed = pg.transform.scale(self.door_fixed, (100 ,350))

    def draw(self, surface):
        screen_devided = WIDTH/2 - 900/2
        surface.blit(self.brick, (screen_devided, HEIGHT- 925))
        surface.blit(self.brick, (screen_devided, HEIGHT-675))
        surface.blit(self.build_ledge, (screen_devided, HEIGHT-705))
        surface.blit(self.build_bottom, (screen_devided, HEIGHT-225))
        surface.blit(self.build_top, (screen_devided, HEIGHT-450))
        self.draw_door(surface)

    def draw_door(self,surface):
        screen_devided = WIDTH/2 - 100/2
        surface.blit(self.door_fixed, (screen_devided, HEIGHT-350))


building = Building()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill('black') 
    building.draw(screen)        
    pg.display.flip()            

pg.quit()
