import pygame
import subprocess
import sys

def img(path):
    return pygame.image.load(path)

def size(val, s):
    return pygame.transform.scale(val, s)

class Animation:
    def __init__(self, ralph_l, ralph_r, win, bg):
        self.ralph_l = ralph_l
        self.ralph_r = ralph_r
        self.win = win
        self.bg = bg
        self.stump = img("stump.png")
        self.stump.set_colorkey((0, 0, 128))
        self.stump = size(self.stump, (290, 80))

        self.ralph_left_hand = img("ralph_left_h.png")
        self.ralph_left_hand.set_colorkey((0, 0, 128))
        self.ralph_left_hand = size(self.ralph_left_hand, (230, 120))

        self.ralph_right_hand = img("ralph_right_h.png")
        self.ralph_right_hand.set_colorkey((0, 0, 128))
        self.ralph_right_hand = size(self.ralph_right_hand, (230, 120))

        self.ralph_yawn = img("ralph_yawn.png")
        self.ralph_yawn.set_colorkey((0, 0, 128))
        self.ralph_yawn = size(self.ralph_yawn, (270, 180))

        self.ralph_relax = img("ralph_relax.png")
        self.ralph_relax.set_colorkey((0, 0, 128))
        self.ralph_relax = size(self.ralph_relax, (180, 160))

        self.excavator_up = img("excavator_up.png")
        self.excavator_up.set_colorkey((0, 0, 0))
        self.excavator_up = size(self.excavator_up, (500, 400))

        self.excavator_down = img("excavator_down.png")
        self.excavator_down.set_colorkey((0, 0, 0))
        self.excavator_down = size(self.excavator_down, (530, 390)) #+ 30 -10

        self.ralph_out1 = img("ralph_out1.png")
        self.ralph_out1.set_colorkey((0, 0, 128))
        self.ralph_out1 = size(self.ralph_out1, (200, 70))

        self.ralph_out2 = img("ralph_out2.png")
        self.ralph_out2.set_colorkey((0, 0, 128))
        self.ralph_out2 = size(self.ralph_out2, (200, 70))

        self.ralph_out3 = img("ralph_out3.png")
        self.ralph_out3.set_colorkey((0, 0, 128))
        self.ralph_out3 = size(self.ralph_out3, (200, 70))

        self.ralph_out4 = img("ralph_out4.png")
        self.ralph_out4.set_colorkey((0, 0, 128))
        self.ralph_out4 = size(self.ralph_out4, (200, 70))

        self.speech1 = img("speech1.png")
        self.speech1.set_colorkey((0, 0, 128))
        self.speech1 = size(self.speech1, (500, 70))

        self.ralph_x = 1000
        self.ralph_y = 750
        self.ralph_speed = 3

        self.excavator_x = 1000
        self.excavator_speed = 2

        self.frame, self.count, self.angry_count = 0, 0, 0
        self.done, self.change, self.come_back, self.angry = False, False, False, False

        self.clock = pygame.time.Clock()

    def walk(self):
        if self.ralph_x > 530:
            self.ralph_x -= self.ralph_speed
           
        if (self.frame // 15) % 2 == 0:
            self.win.blit(self.ralph_l, (self.ralph_x, 789))
        else:
            self.win.blit(self.ralph_r, (self.ralph_x, 789)) 

        self.win.blit(self.stump, (470, 900)) 

        self.clock.tick(60)
        self.frame += 1
    
    def on_stump(self):

        if self.count < 5:
            if (self.frame // 15) % 2 == 0:
                self.win.blit(self.ralph_left_hand, (self.ralph_x - 25, 789))
            else:
                self.win.blit(self.ralph_right_hand, (self.ralph_x - 25, 789)) 
        elif self.count < 7:
            self.win.blit(self.ralph_yawn, (self.ralph_x - 50, 730))        
        elif self.count < 10:            
            self.win.blit(self.ralph_relax, (self.ralph_x - 10, 750))  
        elif self.count < 13:
            if self.ralph_y < 1000: 
                self.ralph_y += self.ralph_speed
                
            self.win.blit(self.ralph_relax, (self.ralph_x - 10, self.ralph_y))
        else:
            self.excavator()
        
        if self.count < 13 or self.excavator_x > 720:
            self.win.blit(self.stump, (470, 900)) 
        self.clock.tick(60)
        self.frame += 1
        self.count += 1 / 30

    def excavator(self):

        if self.excavator_x > 710:
            self.excavator_x -= self.excavator_speed
        else:
            self.excavator_x -= self.excavator_speed
            self.win.blit(self.stump, (self.excavator_x -250, 890))
           
        if (self.frame // 15) % 2 == 0:
            self.win.blit(self.excavator_up, (self.excavator_x, 600))
        else:
            self.win.blit(self.excavator_down, (self.excavator_x, 600 + 10))

        if self.excavator_x < -400:  
            info = pygame.display.Info()
            self.bg = img("dump_bg.png")
            self.bg = size(self.bg, (1240, info.current_h))
            self.excavator_x = 1000
            self.change = True
    
    def dump(self):
        
        if not self.come_back:

            self.excavator_x -= self.excavator_speed            

            self.win.blit(self.stump, (self.excavator_x -210, 890))
            if (self.frame // 15) % 2 == 0:
                self.win.blit(self.excavator_up, (self.excavator_x, 600))
            else:
                self.win.blit(self.excavator_down, (self.excavator_x, 600 + 10)) 

            if self.excavator_x < 650:
                self.come_back = True

        if self.come_back:            
            self.win.blit(self.stump, (430, 870))
            self.excavator_x += self.excavator_speed

            if (self.frame // 15) % 2 == 0:
                self.win.blit(self.excavator_up, (self.excavator_x, 600))
            else:
                self.win.blit(self.excavator_down, (self.excavator_x, 600 + 10))

            if self.excavator_x >= 1500:
                self.angry = True

        self.clock.tick(60)
        self.frame += 1

    def angry_ralph(self):
        self.win.blit(self.stump, (430, 870))

        if self.angry_count < 3:        
            self.win.blit(self.ralph_out1, (475, 800))
        elif self.angry_count < 6:
            self.win.blit(self.ralph_out2, (475, 800))
        elif self.angry_count < 12:   
            self.win.blit(self.speech1, (505, 750))     
            if (self.frame // 15) % 2 == 0:
                self.win.blit(self.ralph_out3, (475, 800))
            else:
                self.win.blit(self.ralph_out4, (475, 800))
            
        self.clock.tick(60)
        self.frame += 1
        self.angry_count += 1 / 30
def avvia_programma():
    pygame.quit()
    subprocess.run(["python3", "test.py"])
    sys.exit()
def main():

    pygame.init()
    clock = pygame.time.Clock()
    frame = 0
    
    info = pygame.display.Info()
    win = pygame.display.set_mode((1250, 980))
    pygame.display.set_caption("fix it felix")
    title = img("title.png")
    title = size(title, (800, 370))
    title.set_colorkey((0, 0, 0))
    win.blit(title, (250, 100))

    start_img = img("start.png")
    start_img = size(start_img, (800, 60))
    start_img.set_colorkey((0, 0, 0))
    win.blit(start_img, (250, 500))
    
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = False
        pygame.display.flip()
        
    bg = img("bg.png")
    bg = size(bg, (1250, info.current_h-200))

    ralph_left_foot = img("ralph_left_f.png")
    ralph_left_foot.set_colorkey((0, 0, 128))
    ralph_left_foot = size(ralph_left_foot, (170,200))

    ralph_right_foot = img("ralph_right_f.png")
    ralph_right_foot.set_colorkey((0, 0, 128))
    ralph_right_foot = size(ralph_right_foot, (170, 200))

    ralph_animation = Animation(ralph_left_foot, ralph_right_foot, win, bg)

    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        win.fill((0, 0, 0))  
        win.blit(ralph_animation.bg, (0, 100))
        if ralph_animation.ralph_x > 530:
            ralph_animation.walk()
        elif ralph_animation.angry:
            ralph_animation.angry_ralph()
            if ralph_animation.angry_count >= 12:
                avvia_programma()
        elif ralph_animation.change:
            ralph_animation.dump()
        else:              
            ralph_animation.on_stump()
        pygame.display.flip()

main()