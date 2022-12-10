import pygame
import random

class Dice(object):
    def __init__(self):
        self.randonnum = 0
        self.isrolling = False
        self.dice_image_count = 0
        self.dice_images = []
        self.dice_rolling_images = []

        for num in range(1,10):
            self.dice_rolling_image = pygame.transform.scale(pygame.image.load('assets/dice_roll' + str(num) + '.png'), (128, 128))
            self.dice_rolling_images.append(self.dice_rolling_image)

        for num in range(1,7):
            self.dice_image = pygame.image.load('assets/' + str(num) + '_dots.png')
            self.dice_images.append(self.dice_image)

    def dicing(self, screen):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and not self.isrolling:
            self.isrolling = True
            self.randonnum = random.randint(0,5)
            screen.blit(self.dice_rolling_images[self.dice_image_count], (280, 280))
        else:
            if self.isrolling:
                pygame.time.delay(20)
                screen.blit(self.dice_rolling_images[self.dice_image_count], (280, 280))
                self.dice_image_count += 1
                if self.dice_image_count >= 8:
                    self.dice_image_count = 0
                    if not key[pygame.K_SPACE]:
                        screen.blit(self.dice_images[self.randonnum], (280, 280))
                        pygame.display.update()
                        pygame.time.delay(300)
                        self.isrolling = False