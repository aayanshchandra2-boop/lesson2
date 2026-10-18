import pygame

pygame.init()
screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Pygame Window")
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()


