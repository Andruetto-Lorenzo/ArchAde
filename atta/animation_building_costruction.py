import pygame as pg

# dimensioni della finestra
WIDTH, HEIGHT = 1800, 930
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Building Animation")


def load_image(path):
     return pg.image.load(path)

def flip_image(img):
     return pg.transform.flip(img, True, False)

def retail_cloud(count):
    gru = load_image('../assets/miscellanous.png')
    crop_rect = pg.Rect(120,450,70,70)
    cropped_cloud = pg.Surface((400, 400))
    cropped_cloud.blit(gru, (0, 0), crop_rect)
    cropped_cloud.set_colorkey('black')
    cloud_pos = [380, 630, 880, 1130]
    cloud_y = [650, 450, 250, -20]
    clouds =  [
        pg.transform.scale(cropped_cloud, (1500,1500)),
        pg.transform.scale(cropped_cloud, (1500,1500)),
        pg.transform.scale(cropped_cloud, (1500,1500)),
        pg.transform.scale(cropped_cloud, (1500,1500))
    ]

    for i in range(4):
        screen.blit(clouds[i], (cloud_pos[i], cloud_y[3 if count > 3 else count]))

def retail_images_costruction():
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
                x_positions[i] = target_x[i]
        elif x_positions[i] > target_x[i]:
            x_positions[i] -= speed
            if x_positions[i] < target_x[i]:
                x_positions[i] = target_x[i]

def get_out():
    target_x_out = [-1300, -650, 1800, 2450]
    for i in range(4): 
        if x_positions[i] < target_x_out[i]:
            x_positions[i] += speed
            if x_positions[i] > target_x_out[i]:
                x_positions[i] = target_x_out[i]
        elif x_positions[i] > target_x_out[i]:
            x_positions[i] -= speed
            if x_positions[i] < target_x_out[i]:
                x_positions[i] = target_x_out[i]
        
def build_plants():
    plant = load_image('building/bush.png')
    plant = pg.transform.scale(plant, (50, 50))
    k = 0
    for i in range(40):
        screen.blit(plant, (k, 890))
        k+=50



class Building:
    def __init__(self):
        self.brick = pg.image.load('building/building_brick.png')
        self.build_bottom = pg.image.load('building/building_cement_bottom.png')
        self.build_top = pg.image.load('building/building_cement_top.png')
        self.build_ledge = pg.image.load('building/building_ledge.png')
        self.door_fixed = pg.image.load('door/door_fixed.png')
        self.window = pg.image.load('windows/windowb.png')
        self.flower = pg.image.load('flower.png')
        # self.cloud = retail_cloud()
        self.initialize_building()
        self.current_stage = 1  # inizia con la base

    def initialize_building(self):
        self.brick = pg.transform.scale(self.brick, (900, 225))
        self.build_bottom = pg.transform.scale(self.build_bottom, (900, 225))
        self.build_top = pg.transform.scale(self.build_top, (900, 225))
        self.build_ledge = pg.transform.scale(self.build_ledge, (900, 30))
        self.door_fixed = pg.transform.scale(self.door_fixed, (150 ,400))
        self.window = pg.transform.scale(self.window, (90 , 190))
        self.flower = pg.transform.scale(self.flower, (200, 50))

    def draw(self, surface):
        screen_devided = WIDTH/2 - 900/2
        images = [self.build_bottom, self.build_top, self.brick ,self.build_ledge, self.brick]
        sizes = [(screen_devided, HEIGHT-220), (screen_devided, HEIGHT-445), (screen_devided, HEIGHT-670), (screen_devided, HEIGHT-700),(screen_devided, HEIGHT-920)]

        for i in range(self.current_stage):
            surface.blit(images[i], sizes[i])
            if i != 3:
                floor_x = screen_devided
                floor_y = sizes[i][1]
                for row in range(1):  
                    for col in range(5):
                        x = floor_x + 110 + col * 150
                        y = floor_y + 20 + row * (self.window.get_height() + 20)
                        surface.blit(self.window, (x, y))
            if i == 0:
                surface.blit(self.flower, (screen_devided + 125,HEIGHT-50))
                surface.blit(self.flower, (screen_devided + 585,HEIGHT-50))

        self.draw_door(surface)

    def advance_stage(self):
        if self.current_stage < 5:
            self.current_stage += 1

    def is_complete(self):
        return self.current_stage == 5

    def draw_door(self, surface):
        screen_devided = WIDTH/2 - 100/2
        surface.blit(self.door_fixed, (screen_devided - 20, HEIGHT-400))

def main():
    clock = pg.time.Clock() # clock
    images = retail_images_costruction() # immagini delle ruspe
    building = Building() # creazione dell'oggetto 'palazzo'
    fase = "entrata"
    start_time = None
    last_update_time = 0
    count = 0
    running = True

    # ciclo di gioco
    while running:
        clock.tick(60)
        now = pg.time.get_ticks()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill('black')
        build_plants()
        if fase == "entrata":
            update_positions()
            stamp(images)
            if all(x_positions[i] == target_x[i] for i in range(4)):
                fase = "costruzione"
                start_time = now
                last_update_time = now

        elif fase == "costruzione":
            building.draw(screen)
            if now - last_update_time >= 1000:
                building.advance_stage()
                last_update_time = now
                count += 1
                if building.is_complete():
                    fase = "uscita"
            stamp(images)
            retail_cloud(count)
            
        elif fase == "uscita":
            building.draw(screen)
            get_out()
            stamp(images)

        pg.display.flip()

    pg.quit()

main()
