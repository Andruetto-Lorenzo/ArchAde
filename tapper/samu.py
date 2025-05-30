import pygame as pg
import sys

# Inizializzazione di Pygame
pg.init()

# Costanti
WINDOW_WIDTH, WINDOW_HEIGHT = 512, 480
TITLE = "Tapper"
BARISTA_DIR_SHEET = './sprites/Bartender.png'

# Colori
COLORS = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "blue": (0, 27, 74),
    "color_key": (17, 88, 159)
}

LOADING_DURATION = 3000
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption(TITLE)

# Classe barista
class Bartender:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite_sheet = BARISTA_DIR_SHEET
        self.idle_sprites = self.get_idle_sprites(2, BARISTA_DIR_SHEET)
        # self.serving_sprites = get_row_sprites(0, 66, 33, 66, 8, BARISTA_DIR_SHEET)
        self.current_sprites = self.idle_sprites
        self.current_frame = 0
        self.animation_speed = 1
        self.animation_timer = 0

    def update(self, dt):
        self.animation_timer += dt

        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.current_sprites)

    def draw(self, surface):
        current_sprite = self.current_sprites[self.current_frame]
        surface.blit(current_sprite, (self.x, self.y))

    def serve(self):
        self.current_sprites = self.serving_sprites
        self.current_frame = 0
    
    def idle(self):
        self.current_sprites = self.idle_sprites
        self.current_frame = 0

    def get_idle_sprites(self, frame_count, image):
        try:
            self.sheet = pg.image.load(image).convert()
            self.sheet.set_colorkey(COLORS['color_key'])
            sprites = []

            first_image_startx = 0
            first_image_starty = 42
            first_image_width = 32
            first_image_height = 60

            second_image_startx  = 2
            second_image_starty = 41
            second_image_width = 32
            second_image_height = 62 

            count = 0
            for i in range(frame_count):
                if not count:
                    rect = pg.Rect(first_image_startx + i * first_image_width, 
                                   first_image_starty, first_image_width, first_image_height)
                    frame = pg.Surface((first_image_width, first_image_height), pg.SRCALPHA)
                    frame.blit(self.sheet, (0, 0), rect)
                if count:
                    rect = pg.Rect(second_image_startx + i * second_image_width, 
                                   second_image_starty, second_image_width, second_image_height)
                    frame = pg.Surface((second_image_width, second_image_height), pg.SRCALPHA)
                    frame.blit(self.sheet, (0, 0), rect)
                sprites.append(frame)
                count += 1

            return sprites
        except Exception as e:
            print(f"Errore {e} nel caricare l'immagine")

# Classe bancone
class Bancone:
    def __init__(self):
        # self.clienti = 
        pass

class Customer:
    def __init__(self, x, y,id):
        self.x = x
        self.id = id
        self.y = y
        self.width = 20
        self.height = 20
        self.animation_timer = 0
        self.cust_sprites = self.get_sprites(0, 4, "./sprites/customers_saloon.png")
        self.current_sprites = self.cust_sprites
        self.current_frame = 0
        self.animation_speed = 1
        self.speed = 30
        self.state = "normal"  # "normal" o "angry"
        self.normal_speed = 0.5  # Velocità normale (lenta)
        self.angry_speed = 2    # Velocità arrabbiato (veloce)
        self.current_speed = self.normal_speed
        
        # Timer per diventare arrabbiato
        self.patience_timer = 0
        self.patience_limit = 5000  # 5 secondi prima di arrabbiarsi



    def draw(self, surface):
        current_sprite = self.current_sprites[self.current_frame]
        surface.blit(current_sprite, (self.x, self.y))    
        self.draw_rect = pg.Rect(self.x,self.y,self.width,self.height)
    
    def get_sprites(self, start_frame_count, frame_count, image):
        self.sprites = []
        try:
            self.sheet = pg.image.load(image).convert()
            self.sheet.set_colorkey(COLORS['color_key'])
            startx = 0
            starty = 0
            for i in range(start_frame_count, frame_count):
                self.rect = pg.Rect(startx + i * 33.5, starty, 33.5, 33.5) # + i * 30
                self.frame = pg.Surface((33.5, 33.5), pg.SRCALPHA)
                self.frame.blit(self.sheet, (0, 0), self.rect)

                self.sprites.append(self.frame)

            return self.sprites
        except Exception as e:
            print("Errore nel caricare l'immagine")
            print(f"Errore: {e}")

    def update(self, dt):        
        self.animation_timer += dt

        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.current_sprites)
        
        if self.current_frame == 0:
            self.state = "advancing"
        self.move()
    
    def move(self):
        self.x += self.current_speed
        if self.id == 1:
            if self.y == 80 and self.x >= 295:
                self.x = 295
        if self.id == 2:
            if self.y == 175 and self.x >= 330:
                self.x = 330
        if self.id == 3:
            if self.y == 271 and self.x >= 360:
                self.x = 360
        if self.id == 4:
            if self.y == 367 and self.x >= 390:
                self.x = 390

    def become_angry(self):
        if self.state != "angry":
            self.state = "angry"
            self.current_sprites = self.angry_sprites
            self.current_speed = self.angry_speed
            self.current_frame = 0  # Riparti dal primo frame delle sprite arrabbiate

    def serve_drink(self):
        self.state = "normal"
        self.current_sprites = self.normal_sprites
        self.current_speed = self.normal_speed
        self.patience_timer = 0
        self.current_frame = 0

    def is_angry(self):
        return self.state == "angry"

    # def move(self):
    #     if self.state == "advancing":
    #         self.x += self.speed

# def get_sprite(x, y, width, height, image):
#     sprite_sheet = pg.image.load(image).convert_alpha()
#     sprite_sheet.set_colorkey(COLORS['color_key'])

#     rect = pg.Rect(x, y, width, height)
#     sprite = pg.Surface((width, height), pg.SRCALPHA)
#     sprite.blit(sprite_sheet, (0, 0), rect)

#     return sprite

def avoid_loop_printing(message, count=0):
    count += 1
    if not count:
        pass
    print(str(message))

def main():
    clock = pg.time.Clock()

    tapper = Bartender(360, 200) # 320 100
    customer1 = Customer(100, 175,1)
    customer2 = Customer(125, 80,2)
    customer3 = Customer(100, 271,3)
    customer4 = Customer(100, 367,4)
    font = pg.font.SysFont("tapper", 16)
    press_enter = font.render("Press ENTER to play", True, COLORS['white'], COLORS['black'])
    textRect = press_enter.get_rect()
    textRect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 60)
    
    welcoming_menu = pg.image.load("./sprites/tapper_menu.png")
    points = pg.image.load("./sprites/points.png")

    scene = pg.image.load('../tapper/sprites/bar_scene.png')

    loading = True
    running = True
    in_menu = True
    game_started = False

    while running:
        # Riconoscimento di chiusura del gioco.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    avoid_loop_printing("Tasto invio premuto")
                    start_time = pg.time.get_ticks()
                    in_menu = False

        if in_menu:
            screen.fill(COLORS['black'])
            screen.blit(welcoming_menu, (0, 0))
            screen.blit(press_enter, textRect)

        elif loading:
            screen.fill(COLORS['blue'])
            screen.blit(points, (0, 0))            

            current_time = pg.time.get_ticks()
            if start_time and current_time - start_time >= LOADING_DURATION:
                loading = False
                game_started = True

        elif game_started:
            screen.fill(COLORS["black"])
            screen.blit(scene, (0, 0))
            bartender_dt = clock.tick(60) / 800.0
            tapper.update(bartender_dt)
            tapper.draw(screen)

            customers_dt = clock.tick(50) / 800.0
            customer1.draw(screen)
            customer1.update(customers_dt)
            customer2.draw(screen)
            customer2.update(customers_dt)
            customer3.draw(screen)
            customer3.update(customers_dt)
            customer4.draw(screen)
            customer4.update(customers_dt)
            

            for event in pg.event.get():
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP or event.key == pg.K_w:    
                        avoid_loop_printing("freccia in su premuta.")
                        print(tapper.x,tapper.y)
                        if tapper.y == 100:
                            tapper.x == 300
                            tapper.y = 0    
                        if tapper.y == 200:
                            tapper.x = 330
                            tapper.y = 100
                        elif tapper.y == 300:
                            tapper.x = 360
                            tapper.y = 200
                        elif tapper.y == 400:
                            tapper.x = 390
                            tapper.y = 300
                        if tapper.y == 0:
                            tapper.x = 420
                            tapper.y = 400    
                    elif event.key == pg.K_DOWN or event.key == pg.K_s:
                        avoid_loop_printing("Freccia giù premuta.")
                        if tapper.y == 100:
                            tapper.x = 360
                            tapper.y = 200
                        elif tapper.y == 200:
                            tapper.x = 390
                            tapper.y = 300
                        elif tapper.y == 300:
                            tapper.x = 420
                            tapper.y = 400
                        elif tapper.y == 400:
                            tapper.y = 500
                        print(tapper.x,tapper.y)
                        if tapper.y == 500:
                            tapper.x = 330
                            tapper.y = 100
                    if event.key == pg.K_LEFT:
                        tapper.x -= 30
                        print(tapper.x,tapper.y)
                    if event.key == pg.K_RIGHT:
                        if tapper.x == 330 and tapper.y == 100 or tapper.x == 360 and tapper.y == 200  or tapper.x == 390 and tapper.y == 300 or tapper.x == 420 and tapper.y == 400 :
                            tapper.x = tapper.x  
                            
                        else:
                            tapper.x += 30
        pg.display.update()
    pg.quit()
    sys.exit()
main()
