import pygame
import os
import random
from buttton import Button

back3_path = 'Art/Card_Back3.png'
back5_path = 'Art/Card_Back5.png'
forward3_path = 'Art/Card_Forward3.png'
forward5_path = 'Art/Card_Forward5.png'
start_path = 'Art/Card_Start.png'
stop_path = 'Art/Card_Stop.png'
card_path = 'Art/Card.png'
cardclick_path = 'Art/Card_Click.png'

pic = random.randrange(1,7,1)

class Card(object):
    def __init__(self):
        self.back3 = pygame.image.load(back3_path)
        self.back5 = pygame.image.load(back5_path)
        self.forward3 = pygame.image.load(forward5_path)
        self.forward5 = pygame.image.load(forward5_path)
        self.start = pygame.image.load(start_path)
        self.stop = pygame.image.load(stop_path)

    def before_rand(self):
        mouse = pygame.mouse.get_pos()
        self.card = pygame.image.load("Art/Card.png")
        self.card_click = pygame.image.load("Art/Card_Click.png")
        self.card_button = Button(image = self.card, pos=(350, 450), 
                            hovering_image = self.cardclick)
        for button in [self.card_button]:
            button.changeColor(mouse)

    def check_click(self, screen):
            if pic == 1:
                screen.blit(self.back3, (350,350))
                self.num = -3
            elif pic == 2:
                screen.blit(self.back5, (350,350))
                self.num = -5
            elif pic == 3:
                screen.blit(self.forward3, (350,350))
                self.num = 3
            elif pic == 4:
                screen.blit(self.forward5, (350,350))
            elif pic == 5:
                screen.blit(self.start, (350,350))
            elif pic == 6:
                screen.blit(self.stop, (350,350))
