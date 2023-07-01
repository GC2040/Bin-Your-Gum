import pygame, sys, os
import game
from button import Button


pygame.init()

SCREEN = pygame.display.set_mode((game.WIDTH, game.HEIGHT))
pygame.display.set_caption("Bin Your Gum - Menu")

BG = pygame.image.load(os.path.join("assets","game","bg","bg.png"))

cursor_img = pygame.image.load(os.path.join("assets","gum_cursor.png"))
cursor_img_rect = cursor_img.get_rect()

def get_font(size):
    return pygame.font.Font(os.path.join("assets","fonts","Belanosima","Belanosima-Regular.ttf"), size)

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    pygame.mouse.set_visible(False)
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Bin Your Gum", True, "#0096FF")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))

        PLAY_BUTTON = Button(image=pygame.image.load(os.path.join("assets","menus","button.png")), pos=(100, 100), 
                            text_input="PLAY", font=get_font(45), base_color="#000000", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load(os.path.join("assets","menus","button.png")), pos=(100, 175), 
                            text_input="OPTIONS", font=get_font(45), base_color="#000000", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load(os.path.join("assets","menus","button.png")), pos=(100, 250), 
                            text_input="QUIT", font=get_font(45), base_color="#000000", hovering_color="White")
        

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game.main()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
            cursor_img_rect.center = pygame.mouse.get_pos()  # update position 
        SCREEN.blit(cursor_img, cursor_img_rect)

        pygame.display.update()

main_menu()