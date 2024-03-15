import pygame, sys
from pygame.locals import *
from datetime import datetime

# Initialize Pygame
pygame.init()

# Clock settings
window_size = (1400, 1050)
fps = 30

# Load images
background = pygame.image.load(r'C:\Users\OmeN_HP\Desktop\mouse.png')
hand_minute = pygame.image.load(r'C:\Users\OmeN_HP\Desktop\right arm.png')
hand_second = pygame.image.load(r'C:\Users\OmeN_HP\Desktop\left arm.png')

# Set up the window
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Mickey Clock')

# Determine the center of the clock face
clock_center = (window_size[0] / 2, window_size[1] / 2)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Get current time
    now = datetime.now()
    minute = now.minute
    second = now.second

    # Calculate rotation angles
    # Note: Pygame rotates counterclockwise, subtracting from 360 to make it clockwise
    angle_minute = -((minute / 60) * 360)
    angle_second = -((second / 60) * 360)

    # Rotate images around their center
    rotated_minute_hand = pygame.transform.rotate(hand_minute, angle_minute)
    rotated_second_hand = pygame.transform.rotate(hand_second, angle_second)

    # Get the new rects and set their centers to the clock center
    minute_rect = rotated_minute_hand.get_rect(center=clock_center)
    second_rect = rotated_second_hand.get_rect(center=clock_center)

    # Drawing
    screen.blit(background, (0,0))  # Blit the clock background
    screen.blit(rotated_minute_hand, minute_rect.topleft)  # Blit the minute hand
    screen.blit(rotated_second_hand, second_rect.topleft)  # Blit the second hand

    pygame.display.flip()
    clock.tick(fps)  # Maintain the desired FPS
