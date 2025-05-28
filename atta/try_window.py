import pygame as pg

# dimensioni della finestra
WIDTH, HEIGHT = 1250, 930
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Building Animation")


def load_image(path):
     return pg.image.load(path)

def flip_image(img):
     return pg.transform.flip(img, True, False)

def retail_cloud(count):
    miscellanous = load_image('../assets/miscellanous.png')
    crop_rect = pg.Rect(120,450,70,70)
    cropped_cloud = pg.Surface((400, 400))
    cropped_cloud.blit(miscellanous, (0, 0), crop_rect)
    cropped_cloud.set_colorkey('black')
    cloud_pos = [130, 380, 630, 880] #1130
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

#x_positions = [-1300, -650, 1800, 2450]
x_positions = [-1300, -650, 1250, 1900]
speed = 5
target_x = [WIDTH // 2 - 1000, WIDTH // 2 - 550, WIDTH // 2 - 100, WIDTH // 2 + 350]

#target_x = [WIDTH // 2 -1000, WIDTH // 2 - 550, WIDTH // 2 - 100, WIDTH // 2 + 350]

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
    #target_x_out = [-1300, -650, 1800, 2450]
    target_x_out = [-1300, -650, 1250, 1900]
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

class Ralph:
    def __init__(self):
        self.ralph_rf = pg.transform.scale(load_image('ralph/ralph_right_foot.png'), (170, 200))
        self.ralph_lf = pg.transform.scale(load_image('ralph/ralph_left_foot.png'), (170, 200))
        self.ralph_rf_flipped = pg.transform.scale(load_image('ralph/ralph_right_f.png'), (170, 200))
        self.ralph_bad = pg.transform.scale(load_image('ralph/ralph_bad.png'), (170, 200))
        self.ralph_bas = pg.transform.scale(load_image('ralph/ralph_bas.png'), (170, 200))
        self.ralph_lf_flipped = pg.transform.scale(load_image('ralph/ralph_left_f.png'), (170, 200))
        # self.ralph_spacca_piano_1 = pg.transform.scale(load_image())
        self.ralph_scale = pg.transform.scale(load_image('ralph/ralph_scale.png'), (170,200))
        self.ralph_x = 0
        self.ralph_y = 740
        self.frame = 0
        self.ralph_speed = 4
        self.ralph_bad.set_colorkey((0,33,87))
        self.ralph_bas.set_colorkey((0,33,87))
        self.ralph_rf.set_colorkey((0, 0, 128))
        self.ralph_rf_flipped.set_colorkey((0, 0, 128))
        self.ralph_lf_flipped.set_colorkey((0,0,128))
        self.ralph_rf.set_colorkey((0, 0, 128))
        self.ralph_scale.set_colorkey((0, 0, 128))
        self.ralph_lf.set_colorkey((0, 0, 128))

    def walk(self, surface):
        if self.ralph_x < 972 and self.ralph_y != 60: # condizione per ralph al piano terra incrementa la x (lo fa muovere verso destra)
            self.ralph_x += self.ralph_speed
            if self.ralph_x >= 52 and self.ralph_x <=970: # ralph spacca le finestre al piano terra
                if (self.frame // 15) % 2 == 0: # movimento dinamico con cambio di immagini
                    surface.blit(self.ralph_bad, (self.ralph_x, self.ralph_y))
                else:
                    surface.blit(self.ralph_bas, (self.ralph_x, self.ralph_y))
        elif self.ralph_x == 972 and self.ralph_y != 60: # ralph sale le scale 
            self.ralph_y -= self.ralph_speed
            surface.blit(self.ralph_scale,(self.ralph_x - 4, self.ralph_y))
        if self.ralph_y == 60 and self.ralph_x != 572: # ralph arriva al centro del palazzo
            self.ralph_x -= self.ralph_speed
            if (self.frame // 15) % 2 == 0:
                surface.blit(self.ralph_lf_flipped, (self.ralph_x, self.ralph_y))
            elif (self.frame // 15) % 2 != 0:
                surface.blit(self.ralph_rf_flipped, (self.ralph_x, self.ralph_y))
        #if (self.frame // 15) % 2 == 0 and self.ralph_x != 972 and self.ralph_y != 60:
        if (self.frame // 15) % 2 == 0 and self.ralph_x < 52 and self.ralph_y != 60:
            surface.blit(self.ralph_lf, (self.ralph_x, 740))
        #elif (self.frame // 15) % 2 != 0 and self.ralph_x != 972 and self.ralph_y != 60:
        elif (self.frame // 15) % 2 != 0 and self.ralph_x < 52 and self.ralph_y != 60:
            surface.blit(self.ralph_rf, (self.ralph_x, 740))
        # self.clock.tick(60)
        self.frame += 1 # incremento counter dei frame


def create_windows(i, floor_x, floor_y, window_image, shutter_image, surface):
    papa = pg.transform.scale(pg.image.load('windows/papa.png'), (45,51))
    pbpa = pg.transform.scale(pg.image.load('windows/pbpa.png'), (45,49))
    papb = pg.transform.scale(pg.image.load('windows/papb.png'), (46,46))
    pbpb = pg.transform.scale(pg.image.load('windows/pbpb.png'), (48,48))
    papa.set_colorkey('black')
    pbpa.set_colorkey('black')
    papb.set_colorkey('black')
    pbpb.set_colorkey('black')
    for row in range(1):  
        for col in range(5):
            x = floor_x + 110 + col * 150
            y = floor_y + 20 + row * (window_image.get_height() + 20)

            if i >= 4:
                surface.blit(shutter_image, (x, y))
            elif i == 1:
                if col != 2:
                    surface.blit(window_image, (x, y))
                    surface.blit(papa, (x + 23, y + 48))
                    surface.blit(pbpa,(x + 23, y + 47))
                    surface.blit(papb,(x + 23, y + 105))
                    surface.blit(pbpb,(x + 21, y + 105))
            else:
                surface.blit(window_image, (x, y))
                surface.blit(papa, (x + 23, y + 48))
                surface.blit(pbpa,(x + 23, y + 47))  
                surface.blit(papb,(x + 23, y + 105))
                surface.blit(pbpb,(x + 21, y + 105))      

class Building:
    def __init__(self):
        self.brick = pg.image.load('building/building_brick.png')
        self.build_bottom = pg.image.load('building/building_cement_bottom.png')
        self.build_top = pg.image.load('building/building_cement_top.png')
        self.build_ledge = pg.image.load('building/building_ledge.png')
        self.door_fixed = pg.image.load('door/door_fixed.png')
        self.window = pg.image.load('windows/window_black.png')
        self.shutter = pg.image.load('windows/window_closed.png')
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
        self.window.set_colorkey('white')
        self.shutter = pg.transform.scale(self.shutter, (90 , 190))
        self.flower = pg.transform.scale(self.flower, (200, 50))

    def draw(self, surface):
        #screen_devided = WIDTH/2 - 900/2
        screen_devided = WIDTH/2 - 900/2
        images = [self.build_bottom, self.build_top, self.brick ,self.build_ledge, self.brick]
        sizes = [(screen_devided, HEIGHT-220), (screen_devided, HEIGHT-445), (screen_devided, HEIGHT-670), (screen_devided, HEIGHT-700),(screen_devided, HEIGHT-920)]

        for i in range(self.current_stage):
            surface.blit(images[i], sizes[i])
            if i != 3:
                floor_x = screen_devided
                floor_y = sizes[i][1]
                create_windows(i, floor_x,floor_y, self.window, self.shutter, surface)            
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
    ralph = Ralph()
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
            fase = "ralph"
        elif fase == "ralph":
            building.draw(screen)
            if ralph.ralph_x <= 972:
                ralph.walk(screen)
                if (ralph.ralph_y == 60 and ralph.ralph_x == 572):
                    screen.blit(ralph.ralph_bad,(ralph.ralph_x,ralph.ralph_y))
                    screen.blit(ralph.ralph_bas,(ralph.ralph_x,ralph.ralph_y))
            
            
        pg.display.flip()

    pg.quit()

main()
