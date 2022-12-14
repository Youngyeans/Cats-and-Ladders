import pygame

class Cat(object):
    def __init__(self,num):
        CAT_WIDTH, CAT_HEIGHT = 70, 62.55
        cat_path = 'Art/Cat_' + str(num) + '.png'
        cat_path_flip = 'Art/Cat_' + str(num) + '_Flip.png'
        self.image = pygame.image.load(cat_path)
        self.imageflip = pygame.image.load(cat_path_flip)
        self.size = pygame.transform.scale(self.image, (CAT_WIDTH, CAT_HEIGHT))
        self.sizeflip = pygame.transform.scale(self.imageflip, (CAT_WIDTH, CAT_HEIGHT))
        self.x = 0
        self.y = 623
        self.row = 1
        self.column = 1
        self.jumpCount = 12
        self.randomnum = 0
        self.checkmove = False

    def draw(self, screen):
        if self.row % 2 == 0:
            screen.blit(self.sizeflip, (self.x, self.y))
        else:
            screen.blit(self.size, (self.x, self.y))
