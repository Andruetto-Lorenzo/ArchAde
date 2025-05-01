import pygame as pg

# Inizializzazione di Pygame
pg.init()

# Costanti
WINDOW_WIDTH, WINDOW_HEIGHT = 512, 480
TITLE = "Tapper"
BARISTA_PERCORSO_SHEET = './sprites/Bartender.png'


screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption(TITLE)

color_key = (0, 48, 80)

def get_sprite(x, y, width, height, image):
    sprite_sheet = pg.image.load(image).convert_alpha()
    sprite_sheet.set_colorkey(color_key)

    rect = pg.Rect(x, y, width, height)
    sprite = pg.Surface((width, height), pg.SRCALPHA)
    sprite.blit(sprite_sheet, (0, 0), rect)

    return sprite

def get_row_sprites(start_x, start_y, frame_width, frame_height, frame_count, image):
    try:
        sheet = pg.image.load(image).convert()
        sheet.set_colorkey(color_key)
        sprites = []

        for i in range(frame_count):
            rect = pg.Rect(start_x + i * frame_width, start_y, frame_width, frame_height)
            frame = pg.Surface((frame_width, frame_height), pg.SRCALPHA)
            frame.blit(sheet, (0, 0), rect)
            sprites.append(frame)

        return sprites
    except Exception as e:
        print(f"Errore {e} nel caricare l'immagine")

class Bartender:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.sprite_sheet = BARISTA_PERCORSO_SHEET

        self.idle_sprites = get_row_sprites(0, 0, 33, 66, 2, BARISTA_PERCORSO_SHEET)
        self.serving_sprites = get_row_sprites(0, 66, 33, 66, 8, BARISTA_PERCORSO_SHEET)

        self.current_sprites = self.idle_sprites
        self.current_frame = 0
        self.animation_speed = 1
        self.animation_timer = 0

    def update(self, dt):
        self.animation_timer += dt

        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.current_sprites)

    # def draw(self, surface):
    #     current_sprite = self.current_sprites[self.current_frame]
    #     surface.blit(current_sprite, (self.x, self.y))

    def draw(self, surface):
        current_sprite = self.current_sprites[self.current_frame]
        scaled_sprite = pg.transform.scale(current_sprite, (66, 102)) 
        surface.blit(scaled_sprite, (self.x, self.y))

    def serve(self):
        self.current_sprites = self.serving_sprites
        self.current_frame = 0
    
    def idle(self):
        self.current_sprites = self.idle_sprites
        self.current_frame = 0


class Bancone:
    def __init__(self):
        # self.clienti = 
        pass

def main():
    clock = pg.time.Clock()
    
    bartender = Bartender(500, 400)

    running = True
    while running:
        # Riconoscimento di chiusura del gioco.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        welcoming_menu = pg.image.load("./sprites/tapper_menu.png")

        screen.blit(welcoming_menu, (0, 0))

        for event in pg.event.get():
            if event.type == pg.K_RETURN:
                screen.fill((0, 0, 0))
                bartender.draw(screen)

        keys = pg.key.get_pressed()

        # if keys[pg.K_RETURN]:
        #     print("Tasto invio premuto")
        #     screen.fill((0, 0, 0))
        #     bartender.draw(screen)


        dt = clock.tick(60) / 1000.0
        bartender.update(dt)
        pg.display.update()
    pg.quit()
main()