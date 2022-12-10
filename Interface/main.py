import pygame, sys
from buttton import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")
BG_End = pygame.image.load("assets/endpic.jpg")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/Valorant Font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("PLAYER", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 120))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        player1 = Button(image=None, pos=(400, 250),
                            text_input="PLAYER 1", font=get_font(20), base_color="white", hovering_color="Red")
        player1.changeColor(PLAY_MOUSE_POS)
        player1.update(SCREEN)

        player2 = Button(image=None, pos=(880, 250),
                            text_input="PLAYER 2", font=get_font(20), base_color="white", hovering_color="Red")
        player2.changeColor(PLAY_MOUSE_POS)
        player2.update(SCREEN)

        player3 = Button(image=None, pos=(400, 550),
                            text_input="PLAYER 3", font=get_font(20), base_color="white", hovering_color="Red")
        player3.changeColor(PLAY_MOUSE_POS)
        player3.update(SCREEN)

        player4 = Button(image=None, pos=(880, 550),
                            text_input="PLAYER 4", font=get_font(20), base_color="white", hovering_color="Red")
        player4.changeColor(PLAY_MOUSE_POS)
        player4.update(SCREEN)


        PLAY_BACK = Button(image=None, pos=(70, 25), 
                            text_input="BACK", font=get_font(30), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                elif player1.checkForInput(PLAY_MOUSE_POS):
                    end_game()
                elif player2.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                elif player3.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                elif player4.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("pink")

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
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

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
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def end_game():
    while True:
        SCREEN.blit(BG_End, (0, 0))

        END_MOUSE_POS = pygame.mouse.get_pos()

        End_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        End_RECT = End_TEXT.get_rect(center=(640, 100))

        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(End_TEXT, End_RECT)

        for button in [QUIT_BUTTON]:
            button.changeColor(END_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_BUTTON.checkForInput(END_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
main_menu()