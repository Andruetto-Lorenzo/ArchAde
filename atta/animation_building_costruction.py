import pygame as pg

# dimensioni della finestra
WIDTH, HEIGHT = 1800, 930
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Building Animation")

def load_image(path):
     return pg.image.load(path)

def flip_image(img):
     return pg.transform.flip(img, True, False)

def retail_images():
    gru = load_image('../assets/miscellanous.png')

    crop_rect = pg.Rect(800, 300, 150, 200)

    cropped_image = pg.Surface((150, 200))
    cropped_image.blit(gru, (0, 0), crop_rect)
    cropped_image.set_colorkey('black')

    return [
        pg.transform.scale(cropped_image, (650, 850)),
        pg.transform.scale(cropped_image, (650, 850)),
        pg.transform.scale(flip_image(cropped_image), (650, 850)),
        pg.transform.scale(flip_image(cropped_image), (650, 850)),
    ]

x_positions = [-1300, -650, 1800, 2450]

speed = 5
target_x = [WIDTH // 2 - 1000, WIDTH // 2 - 550, WIDTH // 2 - 100, WIDTH // 2 + 350]

def stamp(images):
    y = 80
    for i in range(4):
        screen.blit(images[i], (x_positions[i], y))

def update_positions():
    for i in range(4): 
        if x_positions[i] < target_x[i]:
            x_positions[i] += speed
            if x_positions[i] > target_x[i]:
                x_positions[i] = target_x
        elif x_positions[i] > target_x[i]:
            x_positions[i] -= speed
            if x_positions[i] < target_x[i]:
                x_positions[i] = target_x

def get_out():
    target_x_out = [-1300, -650, 1800, 2450]

    for i in range(4): 
        if x_positions[i] < target_x_out[i]:
            x_positions[i] += speed
            if x_positions[i] > target_x_out[i]:
                x_positions[i] = target_x_out
        elif x_positions[i] > target_x_out[i]:
            x_positions[i] -= speed
            if x_positions[i] < target_x_out[i]:
                x_positions[i] = target_x_out


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

def main():
    clock = pg.time.Clock()
    BUILD_EVENT = pg.USEREVENT
    images = retail_images()
    building = Building()

    fase = "entrata"
    timer_started = False  
    running = True
    while running:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == BUILD_EVENT and fase == "costruzione":
                fase = "uscita"

        screen.fill('black')

        if fase == "entrata":
            update_positions()
            stamp(images)
            if all(x_positions[i] == target_x[i] for i in range(4)):
                fase = "costruzione"
        elif fase == "costruzione":
            # building.draw(screen)
            stamp(images)
            if not timer_started:
                pg.time.set_timer(BUILD_EVENT, 4000)
                timer_started = True
        elif fase == "uscita":
            building.draw(screen)
            get_out()
            stamp(images)

        pg.display.flip()

    pg.quit()

main()