import pygame
import os
from object.dice import Dice
from object.ladder import LadderSnake

dice = Dice()
laddersnake = LadderSnake()

cat_path = 'fern_game/assets/nyan.png'
cat_path_flip = 'fern_game/assets/nyanflip.png'

class Cat(object):
    def __init__(self):
        CAT_WIDTH, CAT_HEIGHT = 63, 38
        self.image = pygame.image.load(cat_path)
        self.imageflip = pygame.image.load(cat_path_flip)
        self.size = pygame.transform.scale(self.image, (CAT_WIDTH, CAT_HEIGHT))
        self.sizeflip = pygame.transform.scale(self.imageflip, (CAT_WIDTH, CAT_HEIGHT))
        self.x = 4
        self.y = 645
        self.row = 1
        self.column = 1
        self.jumpCount = 12
        self.randomnum = 0
        self.checkmove = False

    def move(self):
        key = pygame.key.get_pressed()
        if dice.isrolling:
            self.randomnum = dice.randonnum + 1
        else:
            if self.randomnum > 0:
                self.checkmove = True
                dice.randonnum = 0
                if self.column > 9:
                    if self.jumpCount >= -12:
                        self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.1
                        self.y -= 2.8
                        self.jumpCount -= 1
                    else:
                        self.column = 1
                        self.jumpCount = 12
                        self.row += 1
                        self.randomnum -= 1
                else:
                    if self.jumpCount >= -12:
                        self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.1
                        self.jumpCount -= 1
                        if self.row % 2 == 0:
                            self.x -= 2.8
                        else:
                            self.x += 2.8
                    else:
                        self.jumpCount = 12
                        self.randomnum -= 1
                        self.column += 1
            else:
                laddersnake.move(self.row,self.column)
                self.row = laddersnake.row_lad
                self.column = laddersnake.column_lad
                self.checkmove = False
                self.y = 645 - ((self.row - 1) * 70)
                if self.row % 2 == 0:
                    self.x = 704 - ((self.column) * 70)
                else:
                    self.x = 4 + ((self.column - 1) * 70)

    def draw(self, screen):
        if self.row % 2 == 0:
            screen.blit(self.sizeflip, (self.x, self.y))
        else:
            screen.blit(self.size, (self.x, self.y))
        if not self.checkmove:
            dice.dicing(screen)