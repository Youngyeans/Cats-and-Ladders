import pygame , sys
from object.buttton import Button
from state.game_play import GamePlay

pygame.init()

SCREEN = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Cats and Ladders")
pygame.display.set_icon(pygame.image.load("Art/Cat_1_Player.png"))

BG = pygame.image.load("Art/Interface.png")
BG_End = pygame.image.load("Art/Interface.png")

LOGO = pygame.image.load("Art/Logo.png")

def howto():
    while True:
        HOW_MOUSE_POS = pygame.mouse.get_pos()
        HOW_BG = pygame.image.load("Art/How_To_BG.png")
        HOW_PREBG = pygame.image.load("Art/Many_Player.png")
        SCREEN.blit(HOW_PREBG, (0, 0))
        SCREEN.blit(HOW_BG, (0, 0))

        OK_BUTTON = Button(image = pygame.image.load("Art/OK.png"), pos = (350, 415),
                                hovering_image = pygame.image.load("Art/OK_Click.png"))
        X_BUTTON = Button(image=pygame.image.load("Art/X.png"), pos=(507, 270), 
                            hovering_image=pygame.image.load("Art/X_Click.png"))

        for button in [OK_BUTTON, X_BUTTON]:
            button.changeColor(HOW_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OK_BUTTON.checkForInput(HOW_MOUSE_POS):
                    play()
                elif X_BUTTON.checkForInput(HOW_MOUSE_POS):
                    main_menu()
        pygame.display.update()

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        P_BG = pygame.image.load("Art/Many_Player_BG.png")
        SCREEN.blit(P_BG, (0, 0))

        player1 = Button(image = pygame.image.load("Art/P1.png"), pos=((350/2), (350/2)),
                            hovering_image = pygame.image.load("Art/P1_Click.png"))
        player1.changeColor(PLAY_MOUSE_POS)
        player1.update(SCREEN)

        player2 = Button(image = pygame.image.load("Art/P2.png"), pos=((350 * 1.5), (350/2)),
                            hovering_image = pygame.image.load("Art/P2_Click.png"))
        player2.changeColor(PLAY_MOUSE_POS)
        player2.update(SCREEN)

        player3 = Button(image = pygame.image.load("Art/P3.png"), pos=((350/2), (350 * 1.5)),
                            hovering_image = pygame.image.load("Art/P3_Click.png"))
        player3.changeColor(PLAY_MOUSE_POS)
        player3.update(SCREEN)

        player4 = Button(image = pygame.image.load("Art/P4.png"), pos=((350 * 1.5), (350 * 1.5)),
                            hovering_image = pygame.image.load("Art/P4_Click.png"))
        player4.changeColor(PLAY_MOUSE_POS)
        player4.update(SCREEN)

        PLAYER = pygame.image.load("Art/Player.png")
        PLAY_RECT = PLAYER.get_rect(center=(350, 50))
        SCREEN.blit(PLAYER, PLAY_RECT)

        PLAY_BACK = Button(image = pygame.image.load("Art/Back.png"), pos=(70, 25), 
                            hovering_image = pygame.image.load("Art/Back_Click.png"))
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        PLAY_QUIT = Button(image = pygame.image.load("Art/Quit_2.png"), pos=(700 - 70, 25), 
                            hovering_image = pygame.image.load("Art/Quit_2_Click.png"))
        PLAY_QUIT.changeColor(PLAY_MOUSE_POS)
        PLAY_QUIT.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PLAY_QUIT.checkForInput(PLAY_MOUSE_POS):
                    quit_check_play()
                elif player1.checkForInput(PLAY_MOUSE_POS):
                    game_play(1)
                elif player2.checkForInput(PLAY_MOUSE_POS):
                    game_play(2)
                elif player3.checkForInput(PLAY_MOUSE_POS):
                    game_play(3)
                elif player4.checkForInput(PLAY_MOUSE_POS):
                    game_play(4)
        pygame.display.update()

def quit_check_play():
    while True:
        QUIT_CHECK_BG = pygame.image.load("Art/Quit_Check.png")
        QUIT_CHECK_PREBG = pygame.image.load("Art/Many_Player_Page.png")
        QUIT_CHECK_PREBG_SIZE = pygame.transform.scale(QUIT_CHECK_PREBG, (700, 700))

        X_BUTTON = Button(image=pygame.image.load("Art/X.png"), pos=(507, 270), 
                            hovering_image=pygame.image.load("Art/X_Click.png"))
        SURE_BUTTON = Button(image=pygame.image.load("Art/Sure.png"), pos=(270, 405), 
                            hovering_image=pygame.image.load("Art/Sure_Click.png"))
        CANCEL_BUTTON = Button(image=pygame.image.load("Art/Cancel.png"), pos=(430, 405), 
                            hovering_image=pygame.image.load("Art/Cancel_Click.png"))

        QUIT_CHECK_MOUSE_POS = pygame.mouse.get_pos()
        pygame.display.update()

        SCREEN.blit(QUIT_CHECK_PREBG_SIZE, (0, 0))
        SCREEN.blit(QUIT_CHECK_BG, (0, 0))

        for button in [SURE_BUTTON, CANCEL_BUTTON, X_BUTTON]:
            button.changeColor(QUIT_CHECK_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if X_BUTTON.checkForInput(QUIT_CHECK_MOUSE_POS):
                    play()
                if CANCEL_BUTTON.checkForInput(QUIT_CHECK_MOUSE_POS):
                    play()
                if SURE_BUTTON.checkForInput(QUIT_CHECK_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

def quit_check_menu():
    while True:
        QUIT_CHECK_BG = pygame.image.load("Art/Quit_Check.png")
        QUIT_CHECK_PREBG = pygame.image.load("Art/Menu Page.png")
        QUIT_CHECK_PREBG_SIZE = pygame.transform.scale(QUIT_CHECK_PREBG, (700, 700))

        X_BUTTON = Button(image=pygame.image.load("Art/X.png"), pos=(507, 270), 
                            hovering_image=pygame.image.load("Art/X_Click.png"))
        SURE_BUTTON = Button(image=pygame.image.load("Art/Sure.png"), pos=(270, 405), 
                            hovering_image=pygame.image.load("Art/Sure_Click.png"))
        CANCEL_BUTTON = Button(image=pygame.image.load("Art/Cancel.png"), pos=(430, 405), 
                            hovering_image=pygame.image.load("Art/Cancel_Click.png"))

        QUIT_CHECK_MOUSE_POS = pygame.mouse.get_pos()
        pygame.display.update()

        SCREEN.blit(QUIT_CHECK_PREBG_SIZE, (0, 0))
        SCREEN.blit(QUIT_CHECK_BG, (0, 0))

        for button in [SURE_BUTTON, CANCEL_BUTTON, X_BUTTON]:
            button.changeColor(QUIT_CHECK_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if X_BUTTON.checkForInput(QUIT_CHECK_MOUSE_POS):
                    main_menu()
                if CANCEL_BUTTON.checkForInput(QUIT_CHECK_MOUSE_POS):
                    main_menu()
                if SURE_BUTTON.checkForInput(QUIT_CHECK_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(LOGO, ((700 - 488)/2, 115))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("Art/Play.png"), pos=(350, 450), 
                            hovering_image=pygame.image.load("Art/Play_Click.png"))
        QUIT_BUTTON = Button(image=pygame.image.load("Art/Quit.png"), pos=(350, 570), 
                            hovering_image=pygame.image.load("Art/Quit_Click.png"))

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    howto()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    quit_check_menu()
        pygame.display.update()

def game_play(amountplayer):
    gameplay = GamePlay(amountplayer)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        gameplay.main_GamePlay(SCREEN)
        if gameplay.haswon:
            end_game(gameplay.win)
        pygame.display.update()

def end_game(whowin):
    while True:
        SCREEN.blit(BG_End, (0, 0))

        END_MOUSE_POS = pygame.mouse.get_pos()

        CAT_WIN = pygame.image.load('Art\Cat_' + str(whowin) + "_Win.png")

        QUIT_BUTTON = Button(image=pygame.image.load("Art/Quit.png"), pos=(580, 550), 
                            hovering_image=pygame.image.load("Art/Quit_Click.png"))

        RESTART_BUTTON = Button(image=pygame.image.load("Art/Retry.png"), pos=(150, 550), 
                            hovering_image=pygame.image.load("Art/Retry_Click.png"))

        SCREEN.blit(CAT_WIN, (0,0))

        for button in [QUIT_BUTTON, RESTART_BUTTON]:
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
                if RESTART_BUTTON.checkForInput(END_MOUSE_POS):
                    play()
        pygame.display.update()
        print("player "  + str(whowin) + " win")
main_menu()
