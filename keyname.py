import pygame
pygame.init()
pl = True
screen = pygame.display.set_mode((1500, 760))
while pl:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pl = False
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
            print(event.key)