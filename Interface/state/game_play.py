import pygame

from object.move import move
from object.cat import Cat


class GamePlay():
    def __init__(self,amountplayer):
        self.bg_image = pygame.image.load('Art/Ladders_Finish.png')
        self.bg_size = pygame.transform.scale(self.bg_image, (700,700))

        self.cat = []
        self.cat.append(Cat(1))
        self.cat.append(Cat(2))
        self.cat.append(Cat(3))
        self.cat.append(Cat(4))

        self.amount = amountplayer
        self.haswon = False
        self.win = 0

    def main_GamePlay(self,screen):
        for i in range(4):
            if self.cat[i].column == 10 and self.cat[i].row == 10:
                self.haswon = True
                if self.haswon == True:
                    self.win = i + 1
        #draw
        screen.blit(self.bg_size, (0,0))
        move(self.cat,self.amount,screen)
        pygame.display.update()