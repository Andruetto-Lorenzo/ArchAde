import pygame as pg
# from time import sleep

# Inizializzazione di Pygame
pg.init()

# Costanti
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 800
TITLE = "Tapper"
BARISTA_PERCORSO_SHEET = './sprites/Bartender.png'

# Colori
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 27, 74)

screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption(TITLE)

color_key = (0, 48, 80)

# Classe barista
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

# Classe bancone
class Bancone:
    def __init__(self):
        # self.clienti = 
        pass


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

def main():
    clock = pg.time.Clock()
    
    bartender = Bartender(500, 400)

    font = pg.font.Font("freesansbold.ttf", 16)
    press_enter = font.render("Press [ENTER] to play", True, white, black)
    textRect = press_enter.get_rect()
    textRect.center = (WINDOW_WIDTH // 2, 470)

    welcoming_menu = pg.image.load("./sprites/tapper_menu.png")
    points = pg.image.load("./sprites/points.png")

    in_game = False

    running = True
    while running:
        # Riconoscimento di chiusura del gioco.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    in_game = True
        if in_game:
            screen.fill(blue)
            screen.blit(points, (WINDOW_WIDTH // 2, 0))
            # sleep(50)
            # screen.fill(black)
            # bartender.draw(screen)

        if not in_game:
            screen.fill(black)
            screen.blit(welcoming_menu, (0, 0))
            screen.blit(press_enter, textRect)

        dt = clock.tick(60) / 1000.0
        bartender.update(dt)
        pg.display.update()
    pg.quit()
main()
