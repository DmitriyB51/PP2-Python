import pygame
pygame.init()

pl = True
sc = pygame.display.set_mode((1500, 760))
x = 750
y = 380
clock = pygame.time.Clock()

while pl:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pl = False
    pr = pygame.key.get_pressed()
    if pr[pygame.K_UP]:
        if y >= 27:
            y -= 2
    if pr[pygame.K_DOWN]:
        if y <= 733:
            y += 2
    if pr[pygame.K_LEFT]:
        if x >= 27:
            x -= 2
    if pr[pygame.K_RIGHT]:
        if x<=1473:
            x += 2
    sc.fill((0, 0, 0))
    pygame.draw.circle(sc, (255, 0, 0), (x, y), 25 )

    clock.tick(300)
    pygame.display.flip()



