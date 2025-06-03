import pygame as pg
from random import randint

# dimensioni della finestra
WIDTH, HEIGHT = 1250, 930
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Building Animation")


def load_image(path):
     return pg.image.load(path)

def flip_image(img):
     return pg.transform.flip(img, True, False)
    
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


        self.ralph_sad = load_image('ralph/ralph_spacca_alza_dx.png')
        self.ralph_sad = size(self.ralph_sad, ((190, 200)))
        self.ralph_sad.set_colorkey((0, 33, 87))

        self.ralph_sdx = load_image('ralph/ralph_spacca_dx.png')
        self.ralph_sdx = size(self.ralph_sdx, ((190, 200)))
        self.ralph_sdx.set_colorkey((0, 33, 87))

        self.ralph_sas = load_image('ralph/ralph_spacca_alza_sx.png')
        self.ralph_sas = size(self.ralph_sas, ((205, 215)))
        self.ralph_sas.set_colorkey((0, 33, 87))

        self.ralph_ssx = load_image('ralph/ralph_spacca_sx.png')
        self.ralph_ssx = size(self.ralph_ssx, ((205, 215)))
        self.ralph_ssx.set_colorkey((0, 33, 87))

        self.anim_timer = 0
        self.anim_interval = 20
        self.spacca = True
        self.count = 0

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

        if self.ralph_y == 60 and self.ralph_x == 572:
            if self.count < 5:
                if self.spacca: 
                    if (self.frame // 15) % 2 == 0:
                        surface.blit(self.ralph_sad, (self.ralph_x, self.ralph_y))
                    else:
                        surface.blit(self.ralph_sdx, (self.ralph_x, self.ralph_y))
                else:
                    if (self.frame // 15) % 2 == 0:
                        surface.blit(self.ralph_sas, (self.ralph_x, self.ralph_y-5))
                    else:
                        surface.blit(self.ralph_ssx, (self.ralph_x, self.ralph_y-5))
                
                self.anim_timer += 1
                if self.frame % 15 == 0:
                    self.spacca = not self.spacca
                    self.count += 1 / 2
                
        # #if (self.frame // 15) % 2 == 0 and self.ralph_x != 972 and self.ralph_y != 60:
        # if (self.frame // 15) % 2 == 0 and self.ralph_x < 52 and self.ralph_y != 60:
        #     surface.blit(self.ralph_lf, (self.ralph_x, 740))
        # #elif (self.frame // 15) % 2 != 0 and self.ralph_x != 972 and self.ralph_y != 60:
        # elif (self.frame // 15) % 2 != 0 and self.ralph_x < 52 and self.ralph_y != 60:
        #     surface.blit(self.ralph_rf, (self.ralph_x, 740))
            
        # self.clock.tick(60)
        self.frame += 1 # incremento counter dei frame


def create_windows(i, floor_x, floor_y, window_image, shutter_image, surface, broken=False):
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
                if col != 2 and not broken:
                    surface.blit(window_image, (x, y))
                    surface.blit(papa, (x + 23, y + 48))
                    surface.blit(pbpa,(x + 23, y + 47))
                    surface.blit(papb,(x + 23, y + 105))
                    surface.blit(pbpb,(x + 21, y + 105))
                else:
                    surface.blit(window_image, (x, y))
                    surface.blit(pbpa,(x + 23, y + 47))
                    surface.blit(papb,(x + 23, y + 105))
            elif not broken:
                surface.blit(window_image, (x, y))
                surface.blit(papa, (x + 23, y + 48))
                surface.blit(pbpa,(x + 23, y + 47))  
                surface.blit(papb,(x + 23, y + 105))
                surface.blit(pbpb,(x + 21, y + 105))
            else:
                surface.blit(window_image, (x, y))
                surface.blit(pbpa,(x + 23, y + 47))
                surface.blit(papb,(x + 23, y + 105))      

class Building():
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

    def draw(self, surface, ralph_cont=0):
        #screen_devided = WIDTH/2 - 900/2
        screen_devided = WIDTH/2 - 900/2
        images = [self.build_bottom, self.build_top, self.brick ,self.build_ledge, self.brick]
        sizes = [(screen_devided, HEIGHT-220), (screen_devided, HEIGHT-445), (screen_devided, HEIGHT-670), (screen_devided, HEIGHT-700),(screen_devided, HEIGHT-920)]

        for i in range(self.current_stage):
            surface.blit(images[i], sizes[i])
            if i != 3:
                floor_x = screen_devided
                floor_y = sizes[i][1]
                create_windows(i, floor_x,floor_y, self.window, self.shutter, surface, True if ralph_cont >= 5 else False)            
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
        self.felix_up_r = load_image("../rigli/felix_up_r.png")
        self.felix_up_r.set_colorkey((0, 0, 0))
        self.felix_up_r = size(self.felix_up_r, (100, 150))

        self.felix_hammer_r = load_image("../rigli/felix_hammer_r.png")
        self.felix_hammer_r.set_colorkey((0, 0, 0))
        self.felix_hammer_r = size(self.felix_hammer_r, (100, 150))

        self.felix_up_l = load_image("../rigli/felix_up_l.png")
        self.felix_up_l.set_colorkey((0, 0, 0))
        self.felix_up_l = size(self.felix_up_l, (130, 160))         

        self.felix_hammer_l = load_image("../rigli/felix_hammer_l.png")
        self.felix_hammer_l.set_colorkey((0, 0, 0))
        self.felix_hammer_l = size(self.felix_hammer_l, (100, 150))  

        self.felix_fix_r = load_image("../rigli/felix_fix_r.png") 
        self.felix_fix_r.set_colorkey((0, 0, 0))
        self.felix_fix_r = size(self.felix_fix_r, (140, 140))

        self.felix_fix_l = load_image("../rigli/felix_fix_l.png") 
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
    
    def update(self):
        # Gestisce gli stati di animazione
        if self.move or self.felix_fix:
            # Simula un delay senza bloccare il game loop
            if not hasattr(self, 'animation_timer'):
                self.animation_timer = pg.time.get_ticks()
            
            if pg.time.get_ticks() - self.animation_timer > 250:
                self.moving = False
                self.move = False
                self.felix_fix = False
                delattr(self, 'animation_timer')
    
    def get_rect(self):
        return pg.Rect(self.felix_x, self.felix_y, 100, 150)

class Bricks:
    def __init__(self, x, y):
        self.img = pg.transform.scale(pg.image.load("brick.png"), (50, 50))
        self.img.set_colorkey((0, 0, 0))
        self.x = x
        self.y = y
        self.speed = 5

    def update(self):
        self.y += self.speed

    def draw(self, surface):
        surface.blit(self.img, (self.x, self.y))

    def get_rect(self):
        return pg.Rect(self.x, self.y, 50, 50)

def check_collision(felix, bricks):
    felix_rect = felix.get_rect()
    collision_bricks = []

    for brick in bricks:
        brick_rect = brick.get_rect()
        if felix_rect.colliderect(brick_rect):
            collision_bricks.append(brick)
    
    return collision_bricks


def draw_lives(surface, lives_count):
    life = load_image("life.png")
    life.set_colorkey((0, 0, 0))
    life = pg.transform.scale(life, (50, 50))

    life_x = 1050
    for i in range(lives_count):
        surface.blit(life, (life_x, 50))
        life_x += 55


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
    felix = Felix(screen)
    play = False
        
    bricks = []
    last_spawn_time = pg.time.get_ticks()

    lives = 3
    coold = False
    cooldown = 0

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
            ralph.walk(screen)
            if ralph.count >= 5:
                fase = "felix"
                play = True
        
        elif fase == "felix":
                building.draw(screen, ralph.count)
                felix.update()
                felix.draw_felix()

                if coold:
                    if now - cooldown > 2000:
                        coold = False
                    
                    if (now // 200) % 2 == 0:
                        felix.draw_felix()
                else:
                    felix.draw_felix

                current_time = pg.time.get_ticks()

                if current_time - last_spawn_time > 6000:
                    col = randint(0, 4)
                    col_pos = [295, 450, 590, 750, 905]
                    x_pos = col_pos[col]

                    for _ in range(3):
                        y_pos = 200 - (_ * 53)
                        bricks.append(Bricks(x_pos, y_pos))

                    last_spawn_time = current_time

                # bricks = [brick1, brick2, brick3]
                # in brick
                for brick in bricks[:]:
                    brick.update()
                    brick.draw(screen)
                    if brick.y > HEIGHT:
                        bricks.remove(brick)
                
                if not coold:
                    collided_bricks = check_collision(felix, bricks)

                    if collided_bricks:
                        lives -= 1
                        coold = True
                        cooldown = now

                        if lives <= 0:                    
                            print('game over')

                    for brick in collided_bricks:
                        if brick in bricks:
                            bricks.remove(brick)

                draw_lives(screen, lives)

        pg.display.flip()

    pg.quit()

main()
