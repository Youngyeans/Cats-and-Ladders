import pygame
pygame.init()
screen = pygame.display.set_mode((199,330))
pygame.display.set_caption("card random")

from randimage import get_random_image, show_array
import matplotlib
card_1 = pygame.image.load("Card_Back.png")
card_2 = pygame.image.load("Card_Forward.png")
card_3 = pygame.image.load("Card_Start.png")
card_4 = pygame.image.load("Card_Stop.png")

cardrandom = [card_1, card_2, card_3, card_4]
inrandom = get_random_image(cardrandom)

matplotlib.image.imsave("Card_Back", image)
matplotlib.image.imsave("Card_Forward", image)
matplotlib.image.imsave("Card_Start", image)
matplotlib.image.imsave("Card_Start", image)



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()

    screen.blit(cardrandom,(0,0))
    pygame.display.update()
