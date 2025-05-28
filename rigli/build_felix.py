import pygame as pg

# dimensioni della finestra
WIDTH, HEIGHT = 1250, 930
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Building Animation")


def load_image(path):
     return pg.image.load(path)

def flip_image(img):
     return pg.transform.flip(img, True, False)

def img(path):
    return pg.image.load(path)

def size(val, s):
    return pg.transform.scale(val, s)

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
    plant = load_image('../atta/building/bush.png')
    plant = pg.transform.scale(plant, (50, 50))
    k = 0
    for i in range(40):
        screen.blit(plant, (k, 890))
        k+=50

class Ralph:
    def __init__(self):
        self.ralph_rf = pg.transform.scale(load_image('../atta/ralph/ralph_right_foot.png'), (170, 200))
        self.ralph_lf = pg.transform.scale(load_image('../atta/ralph/ralph_left_foot.png'), (170, 200))
        self.ralph_rf_flipped = pg.transform.scale(load_image('../atta/ralph/ralph_right_f.png'), (170, 200))
        self.ralph_lf_flipped = pg.transform.scale(load_image('../atta/ralph/ralph_left_f.png'), (170, 200))
        self.ralph_scale = pg.transform.scale(load_image('../atta/ralph/ralph_scale.png'), (170,200))
        self.ralph_x = 0
        self.ralph_y = 740
        self.frame = 0
        self.ralph_speed = 4
        self.ralph_rf.set_colorkey((0, 0, 128))
        self.ralph_rf_flipped.set_colorkey((0, 0, 128))
        self.ralph_lf_flipped.set_colorkey((0, 0, 128))
        self.ralph_rf.set_colorkey((0, 0, 128))
        self.ralph_scale.set_colorkey((0, 0, 128))
        self.ralph_lf.set_colorkey((0, 0, 128))

    def walk(self, surface):
        if self.ralph_x < 972 and self.ralph_y != 60:
            self.ralph_x += self.ralph_speed
        elif self.ralph_x == 972 and self.ralph_y != 60:
            self.ralph_y -= self.ralph_speed
            surface.blit(self.ralph_scale,(self.ralph_x - 4, self.ralph_y))
        if self.ralph_y == 60 and self.ralph_x != 572:
            self.ralph_x -= self.ralph_speed
            if (self.frame // 15) % 2 == 0:
                surface.blit(self.ralph_lf_flipped, (self.ralph_x, self.ralph_y))
            elif (self.frame // 15) % 2 != 0:
                surface.blit(self.ralph_rf_flipped, (self.ralph_x, self.ralph_y))
        if (self.frame // 15) % 2 == 0 and self.ralph_x != 972 and self.ralph_y != 60:
            surface.blit(self.ralph_lf, (self.ralph_x, 740))
        elif (self.frame // 15) % 2 != 0 and self.ralph_x != 972 and self.ralph_y != 60:
            surface.blit(self.ralph_rf, (self.ralph_x, 740))
        # self.clock.tick(60)
        self.frame += 1


class Building:
    def __init__(self):
        self.brick = pg.image.load('../atta/building/building_brick.png')
        self.build_bottom = pg.image.load('../atta/building/building_cement_bottom.png')
        self.build_top = pg.image.load('../atta/building/building_cement_top.png')
        self.build_ledge = pg.image.load('../atta/building/building_ledge.png')
        self.door_fixed = pg.image.load('../atta/door/door_fixed.png')
        self.window = pg.image.load('../atta/windows/windowb.png')
        self.shutter = pg.image.load('../atta/windows/shutter.png')
        self.flower = pg.image.load('../atta/flower.png')
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
                for row in range(1):  
                    for col in range(5):
                        x = floor_x + 110 + col * 150
                        y = floor_y + 20 + row * (self.window.get_height() + 20)
                        surface.blit(self.window, (x, y))
                        if i >= 4:
                            surface.blit(self.shutter, (x, y))
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


class Felix:
    def __init__(self, win):
        self.win = win
        self.felix_up_r = img("felix_up_r.png")
        self.felix_up_r.set_colorkey((0, 0, 0))
        self.felix_up_r = size(self.felix_up_r, (100, 150))

        self.felix_hammer_r = img("felix_hammer_r.png")
        self.felix_hammer_r.set_colorkey((0, 0, 0))
        self.felix_hammer_r = size(self.felix_hammer_r, (100, 150))

        self.felix_up_l = img("felix_up_l.png")
        self.felix_up_l.set_colorkey((0, 0, 0))
        self.felix_up_l = size(self.felix_up_l, (130, 160))         

        self.felix_hammer_l = img("felix_hammer_l.png")
        self.felix_hammer_l.set_colorkey((0, 0, 0))
        self.felix_hammer_l = size(self.felix_hammer_l, (100, 150))  

        self.felix_fix_r = img("felix_fix_r.png") 
        self.felix_fix_r.set_colorkey((0, 0, 0))
        self.felix_fix_r = size(self.felix_fix_r, (140, 140))

        self.felix_fix_l = img("felix_fix_l.png") 
        self.felix_fix_l.set_colorkey((0, 0, 0))
        self.felix_fix_l = size(self.felix_fix_l, (140, 130))

        self.positions = [
            [(285, 310), (430, 310), (565, 310), (710, 310), (890, 310)],
            [(285, 535), (420, 535), (555, 535), (720, 535), (890, 535)],
            [(285, 800), (430, 800), (555, 800), (715, 800), (890, 800)]
        ]       

        self.row = 2
        self.col = 0 
        self.felix_x, self.felix_y = self.positions[self.row][self.col]
        self.felix_speed = 2

        self.direction = 'right'
        self.move, self.felix_fix, self.moving = False, False, False

        self.min_x = 200
        self.max_x = 800
        self.min_y = 100
        self.max_y = 800

        self.clock = pg.time.Clock()

    def draw_felix(self):
        
        if self.direction == 'right':
            if self.move:
                self.win.blit(self.felix_hammer_r, (self.felix_x, self.felix_y))
            elif self.felix_fix: 
                self.win.blit(self.felix_fix_r, (self.felix_x, self.felix_y))
            else:
                self.win.blit(self.felix_up_r, (self.felix_x, self.felix_y)) 

        elif self.direction == 'left':
            if self.move:
                self.win.blit(self.felix_hammer_l, (self.felix_x, self.felix_y))
            elif self.felix_fix: 
                self.win.blit(self.felix_fix_l, (self.felix_x -20, self.felix_y+20))
            else:
                self.win.blit(self.felix_up_l, (self.felix_x, self.felix_y)) 

    def change_position(self):
        self.felix_x, self.felix_y = self.positions[self.row][self.col]
        self.move = True
        self.moving = True

    def left(self):
        if self.moving or self.col == 0:
            return
        self.col -= 1
        self.direction = 'left'
        self.change_position()
    
    def right(self):
        if self.moving or self.col == len(self.positions[0]) - 1:
            return
        self.col += 1
        self.direction = 'right'
        self.change_position()

    def up(self):
        if self.moving or self.row == 0:
            return
        self.row -= 1
        self.change_position()

    def down(self):
        if self.moving or self.row == len(self.positions) - 1:
            return
        self.row += 1
        self.change_position()

    def fix(self):
        self.felix_fix = True

def main():
    pg.init()
    clock = pg.time.Clock() # clock

    images = retail_images_costruction() # immagini delle ruspe
    building = Building() # creazione dell'oggetto 'palazzo'
    ralph = Ralph()
    fase = "entrata"
    start_time = None
    last_update_time = 0
    count = 0
    running = True
    felix = Felix(screen)

    # ciclo di gioco
    while running:
        clock.tick(60)
        now = pg.time.get_ticks()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                
            elif event.type == pg.KEYDOWN:
                if fase == "felix":
                    if event.key == pg.K_LEFT:
                        felix.left()
                    elif event.key == pg.K_RIGHT:
                        felix.right()
                    elif event.key == pg.K_UP:
                        felix.up()
                    elif event.key == pg.K_DOWN:
                        felix.down()
                    elif event.key == pg.K_f:
                        felix.fix()

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
                if ralph.ralph_x <= 572 and ralph.ralph_y == 60:
                    fase = 'felix'
            
        elif fase == 'felix':
            building.draw(screen)
            felix.draw_felix()

        pg.display.flip()
        if fase == 'felix':
            if felix.move or felix.felix_fix:
                pg.time.delay(250)
                felix.moving = False
                felix.move = False
                felix.felix_fix = False
        

    pg.quit()

main()
