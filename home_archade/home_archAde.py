import pygame

def img(path):
    return pygame.image.load(path)

def size(val, s):
    return pygame.transform.scale(val, s)

def main():

    pygame.init()
    clock = pygame.time.Clock()
    frame = 0

    pygame.display.set_caption("ArchAde")
    screen = pygame.display.set_mode((1920, 1080)) 

    bg = img("assets/bg.png")
    bg.set_colorkey((221, 255, 255))
    bg = size(bg, (1920, 1080))
    screen.blit(bg, (0, 0))

    pianta = img("assets/pianta.png")
    pianta.set_colorkey((221, 255, 255))
    pianta = size(pianta, (415, 537))
    screen.blit(pianta, (20, 400))

    arcade_felix = img("assets/arcade_felix2.png")
    arcade_felix.set_colorkey((221, 255, 255))
    arcade_felix = size(arcade_felix, (342, 600))
    screen.blit(arcade_felix, (420, 330))

    sedia = img("assets/sedia.png")
    sedia.set_colorkey((221, 255, 255))
    sedia = size(sedia, (261, 297))
    screen.blit(sedia, (720, 610))
    
    arcade_tapper = img("assets/arcade_tapper2.png")
    arcade_tapper.set_colorkey((221, 255, 255))
    arcade_tapper = size(arcade_tapper, (342, 650))
    screen.blit(arcade_tapper, (1000, 300))

    exit_text = img("assets/exit.png")
    exit_text.set_colorkey((221, 255, 255))
    exit_text = size(exit_text, (300, 120))
    screen.blit(exit_text, (1595, 170))

    door = img("assets/door.png")
    door.set_colorkey((221, 255, 255))
    door = size(door, (438, 581))
    screen.blit(door, (1530, 310))

    cat = img("assets/cat.png")
    cat.set_colorkey((221, 255, 255))
    cat = size(cat, (212, 197))
    screen.blit(cat, (1450, 750))

    text = img("assets/open.png")
    text.set_colorkey((221, 255, 255))
    text = size(text, (481, 240))
    screen.blit(text, (20, 70))

    img_rect = door.get_rect(topleft=(1530, 310))
    felix_rect = door.get_rect(topleft=(1530, 310))

    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    
    start = True
    while start:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if img_rect.collidepoint(event.pos):
                    start = False

            if img_rect.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        pygame.display.flip()

main()