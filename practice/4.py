import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((1500, 760))
done = False
is_blue = True
x = 30
y = 30
clock = pygame.time.Clock()
surface = pygame.image.load("C:/Users/OmeN_HP/Pictures/Screenshots/Снимок экрана 2024-03-21 131402.png")
while not done:

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if is_blue:
        color = (0, 0, 255)
    else:
        color = (0, 255, 0)

    if pressed[pygame.K_UP]:
        y -= 2
    if pressed[pygame.K_DOWN]:
        y += 2
    if pressed[pygame.K_LEFT]:
        x -= 2
    if pressed[pygame.K_RIGHT]:
        x += 2


    screen.fill((0, 0, 0))
    # screen.blit(surface, (x, y))
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 100, 100))
    clock.tick(300)
    pygame.display.flip()

