import pygame

def img(path):
    return pygame.image.load(path)

def size(val, s):
    return pygame.transform.scale(val, s)

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
        
        self.felix_x = 200
        self.felix_y = 789
        self.felix_speed = 2

        self.step = 200

        self.direction = 'right'
        self.move, self.felix_fix, self.moving = False, False, False

        self.min_x = 200
        self.max_x = 800
        self.min_y = 100
        self.max_y = 800

        self.clock = pygame.time.Clock()

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

    def left(self):
        if self.moving:
            return
        self.direction = 'left'
        if self.felix_x - self.step >= self.min_x:
            self.felix_x -= self.step        
            self.move = True
            self.moving = True
        else:
            self.move = False

    def right(self):
        if self.moving:
            return
        if self.felix_x + self.step <= self.max_x:
            self.felix_x += self.step
            self.direction = 'right'
            self.move = True
            self.moving = True
        else:
            self.move = False

    def up(self):
        if self.moving:
            return
        if self.felix_y -self.step >= self.min_y:
            self.felix_y -= self.step
            self.move = True
            self.moving = True
        else:
            self.move = False
    
    def down(self):
        if self.moving:
            return
        if self.felix_y + self.step <= self.max_y:
            self.felix_y += self.step
            self.move = True
            self.moving = True
        else:
            self.move = False

    def fix(self):
        self.felix_fix = True


def main(): 

    pygame.init()
    info = pygame.display.Info()
    win = pygame.display.set_mode((1250, info.current_h-100))
    pygame.display.set_caption("fix it felix")

    felix = Felix(win)
    clock = pygame.time.Clock()
    loop = True
    while loop:
        win.fill((0, 0, 0))
        for event in pygame.event.get():                
            if event.type == pygame.QUIT:
                loop = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    felix.left()
                elif event.key == pygame.K_RIGHT:
                    felix.right()
                elif event.key == pygame.K_UP:
                    felix.up()
                elif event.key == pygame.K_DOWN:
                    felix.down()
                elif event.key == pygame.K_f:
                    felix.fix()

        felix.draw_felix()
        pygame.display.flip()

        if felix.move or felix.felix_fix:
            pygame.time.delay(250)
            felix.moving = False

        felix.move = False
        felix.felix_fix = False
        clock.tick(60)

main()