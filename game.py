import pygame
import os
import random
import hollow
WIDTH = 800
HEIGHT = 600
BACKGROUND = (255, 0, 0)
#paths

gum_img = os.path.join("assets","game","sprites","gum.png")
bin_img = os.path.join("assets","game","sprites","bin-to-scale.png")
bg = pygame.image.load(os.path.join("assets","game","bg","bg.png"))
icon = pygame.image.load(os.path.join("assets","game","sprites","bin.png"))






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
    def __init__(self, startx, starty):
        super().__init__(bin_img, startx, starty)
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
    def __init__(self, startx, starty):
        super().__init__(gum_img, startx, starty)
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

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    score = 0


    player = Player(800/2-150/2,600-128)
    player_group = pygame.sprite.Group()
    gum = Gum(800/2-100/2,-57)
    gum_group = pygame.sprite.Group()
    gum_group.add(gum)
    player_group.add(gum)


    font = pygame.font.Font(None,36)
    

    pygame.display.set_caption("Bin Your Gum")
    pygame.display.set_icon(icon)
    pygame.mouse.set_visible(False)
    
    while True:
        pygame.event.pump()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        
        if pygame.sprite.spritecollide(player,gum_group,False,pygame.sprite.collide_mask):
        #if self.rect.colliderect(self.player.rect):
        #if self.mask.overlap(self.player.mask,(self.rect.x -self.player.rect.x,self.rect.y-self.player.rect.y)):
            score += 1
            print(f"score: {score}")
            print("collided")
            gum.respawn()
        elif gum.rect.y > 600:
            gum.respawn()
        
        
        player.update()
        gum.update()

        screen.blit(bg,(0,0))
        player.draw(screen)
        gum.draw(screen)
        score_text = hollow.textOutline(font,f"Score: {score}",(255, 234, 0),(255,255,255))
        screen.blit(score_text,(10,10))


        
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()