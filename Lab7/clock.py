import pygame, sys
from pygame.locals import *
from datetime import datetime


pygame.init()


window_size = (1400, 1050)
fps = 30


background = pygame.image.load(r'C:\Users\OmeN_HP\Desktop\mouse.png')
hand_minute = pygame.image.load(r'C:\Users\OmeN_HP\Desktop\right arm.png')
hand_second = pygame.image.load(r'C:\Users\OmeN_HP\Desktop\left arm.png')


screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Mickey Clock')


clock_center = (window_size[0] / 2, window_size[1] / 2)


clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    now = datetime.now()
    minute = now.minute
    second = now.second


    angle_minute = -((minute / 60) * 360)
    angle_second = -((second / 60) * 360)


    rotated_minute_hand = pygame.transform.rotate(hand_minute, angle_minute)
    rotated_second_hand = pygame.transform.rotate(hand_second, angle_second)


    minute_rect = rotated_minute_hand.get_rect(center=clock_center)
    second_rect = rotated_second_hand.get_rect(center=clock_center)


    screen.blit(background, (0, 0))
    screen.blit(rotated_minute_hand, minute_rect.topleft)
    screen.blit(rotated_second_hand, second_rect.topleft)

    pygame.display.flip()
    clock.tick(fps)
