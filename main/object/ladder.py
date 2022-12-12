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

class Card(object):
    def __init__(self):
        self.back3 = pygame.image.load(back3_path)
        self.back5 = pygame.image.load(back5_path)
        self.forward3 = pygame.image.load(forward5_path)
        self.forward5 = pygame.image.load(forward5_path)
        self.start = pygame.image.load(start_path)
        self.stop = pygame.image.load(stop_path)

    def show(self, screen):
        self.pic = random.randrange(1,7,1)
        if self.pic == 1:
            screen.blit(self.back3, (350,350))
            self.text = "back3"
        elif self.pic == 2:
            screen.blit(self.back5, (350,350))
            self.text = "back5"
        elif self.pic == 3:
            screen.blit(self.forward3, (350,350))
            self.text = "forward3"
        elif self.pic == 4:
            screen.blit(self.forward5, (350,350))
            self.text = "forward5"
        elif self.pic == 5:
            screen.blit(self.start, (350,350))
            self.text = "start"
        elif self.pic == 6:
            screen.blit(self.stop, (350,350))
            self.text = "stop"

