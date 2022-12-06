import pygame
from object.cat import Cat

WIDTH, HEIGHT =  700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("cats and Ladders")

WHITE = ((255, 255, 255))
FPS = 60

bg_image = pygame.image.load('fern_game/assets/ladders.png')
bg_size = pygame.transform.scale(bg_image, (700, 700))

cat = []

cat.append(Cat())

def draw2():
    screen.fill(WHITE)
    screen.blit(bg_size, (0, 0))
    cat[0].draw(screen)
    pygame.display.update()
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        cat[0].move()
        draw2()
    pygame.quit()

if __name__ == "__main__":
    main()