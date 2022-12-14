import pygame
import random

class Dice(object):
    def __init__(self):
        self.randonnum = 0
        self.isrolling = False
        self.dice_image_count = 0
        self.dice_images = []
        self.dice_rolling_images = []
        self.numplay = 0

        for num in range(1,10):
            self.dice_rolling_image = pygame.transform.scale(pygame.image.load('Art/dice_roll' + str(num) + '.png'), (128, 128))
            self.dice_rolling_images.append(self.dice_rolling_image)

        for num in range(1,7):
            self.dice_image = pygame.transform.scale(pygame.image.load('Art/' + str(num) + '_dots.png') , (128,128))
            self.dice_images.append(self.dice_image)

    def dicing(self,screen,cat,amount):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and not self.isrolling:
            self.isrolling = True
            self.randonnum = random.randint(1,6)
            screen.blit(self.dice_rolling_images[self.dice_image_count], (280, 280))
        else:
            if self.isrolling:
                pygame.time.delay(20)
                screen.blit(self.dice_rolling_images[self.dice_image_count], (280, 280))
                self.dice_image_count += 1
                if self.dice_image_count >= 8:
                    self.dice_image_count = 0
                    if not key[pygame.K_SPACE]:
                        screen.blit(self.dice_images[self.randonnum - 1], (280, 280))
                        for i in range(amount-1,-1,-1):
                            cat[i].draw(screen)
                        pygame.display.update()
                        pygame.time.delay(300)
                        for i in range(amount-1,-1,-1):
                            if cat[i].row == 10:
                                if cat[i].column + self.randonnum > 10:
                                    self.randonnum = 10 - cat[i].column
                        self.isrolling = False