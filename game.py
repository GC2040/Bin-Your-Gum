import pygame
import os, sys
import random
import hollow
WIDTH = 800
HEIGHT = 600
BACKGROUND = (255, 0, 0)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, startx, starty):
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.topleft = [startx, starty]

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect )



class Player(Sprite):
    def __init__(self, startx, starty,running_dir):
        self.bin_img = os.path.join(running_dir,"assets","game","sprites","bin-to-scale.png")
        super().__init__(self.bin_img, startx, starty)
        
        self.speed = 4
        
        #mask
        self.rect.width = 85
        self.rect.height = 25
        
        self.mask = pygame.mask.Mask((self.rect.width,self.rect.height),True)
        #self.mask = pygame.mask.from_surface(self.image)

    def draw(self,screen):
        screen.blit(self.image, (self.rect.x -65, self.rect.y))
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a] and self.rect.x >= 0:
            self.move(-self.speed,0)
        elif key[pygame.K_RIGHT] or key[pygame.K_d] and self.rect.x <=800-85:
            self.move(self.speed,0)

    def move(self, x, y):
        self.rect.move_ip([x,y])

class Gum(Sprite):
    def __init__(self, startx, starty,running_dir):
        self.gum_img = os.path.join(running_dir,"assets","game","sprites","gum.png")
        super().__init__(self.gum_img, startx, starty)
        
        self.speed = 6
        
        self.score = 0

        #masks
        self.mask = pygame.mask.from_surface(self.image)
        #self.mask = pygame.mask.from_surface(self.image)

        
        
        
    
    def update(self):
        self.move(0,self.speed)

    def respawn(self):
        range = random.randrange(700)
        print(f"Respawn X : {range}")
        self.rect.y = -57
        self.rect.x = range
            
            
    def move(self,x,y):
        self.rect.move_ip([x,y])
class Game():
    def __init__(self, running_dir) -> None:
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.score = 0
        self.running_dir = running_dir
        
        
    def main(self):
        
        
        self.bg = pygame.image.load(os.path.join(self.running_dir,"assets","game","bg","bg.png"))
        self.icon = pygame.image.load(os.path.join(self.running_dir,"assets","game","sprites","bin.png"))
        self.player = Player(800/2-150/2,600-128,self.running_dir)
        self.player_group = pygame.sprite.Group()
        self.gum = Gum(800/2-100/2,-57,self.running_dir)
        self.gum_group = pygame.sprite.Group()
        self.gum_group.add(self.gum)
        self.player_group.add(self.gum)


        font = pygame.font.Font(None,36)
        

        pygame.display.set_caption("Bin Your Gum")
        pygame.display.set_icon(self.icon)
        pygame.mouse.set_visible(False)
        
        while True:
            pygame.event.pump()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if pygame.sprite.spritecollide(self.player,self.gum_group,False,pygame.sprite.collide_mask):
            #if self.rect.colliderect(self.player.rect):
            #if self.mask.overlap(self.player.mask,(self.rect.x -self.player.rect.x,self.rect.y-self.player.rect.y)):
                self.score += 1
                print(f"score: {self.score}")
                print("collided")
                self.gum.respawn()
            elif self.gum.rect.y > 600:
                self.gum.respawn()
            
            
            self.player.update()
            self.gum.update()

            self.screen.blit(self.bg,(0,0))
            self.player.draw(self.screen)
            self.gum.draw(self.screen)
            score_text = hollow.textOutline(font,f"Score: {self.score}",(255, 234, 0),(255,255,255))
            self.screen.blit(score_text,(10,10))


            
            pygame.display.flip()

            self.clock.tick(60)
