import random
import sys
import time

import pygame
from pygame.locals import *

pygame.init()

# COLORS
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Display settings
height = 750
width = 600
display = pygame.display.set_mode((width, height))
display.fill(WHITE)
pygame.display.set_caption("Car Game")

FPS = pygame.time.Clock()

# Speed / score / coins
speed_enemy = 2
speed_player = 2
score = 0
coins_collected = 0


# Setting up Fonts
font = pygame.font.SysFont("Verdana", 30)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Background settings
background = pygame.image.load('C:/Users/OmeN_HP/Desktop/1672892636_grizly-club-p-tekstura-dorogi-s-razmetkoi-5.png')
background = pygame.transform.scale(background, (width, height))


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        # Enemy image settings
        self.image = pygame.image.load(
            'C:/Users/OmeN_HP/Downloads/1692222533_grizly-club-p-kartinki-mashina-2d-bez-fona-25.png')
        self.image = pygame.transform.scale(self.image, (70, 120))

        # Enemy hit-box settings
        self.rect = self.image.get_rect()

        # Appearing of enemy at a random top point
        self.rect.center = (random.randint(30, width - 30), 0)

    def move(self):
        global score
        # Moving down
        self.rect.move_ip(0, speed_enemy)

        # If Enemy touch the bottom
        if (self.rect.bottom > height):
            score += 1
            # Return to top
            self.rect.top = 0
            # Random coordinate on top
            self.rect.center = (random.randint(30, width - 30), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Player image settings
        self.image = pygame.image.load(
            "C:/Users/OmeN_HP/Downloads/1692222542_grizly-club-p-kartinki-mashina-2d-bez-fona-53.png")
        self.image = pygame.transform.scale(self.image, (70, 120))

        # Player hit-box
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # Identifying if to what direction player goes
        if self.rect.top > 4:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -speed_player)
        if self.rect.bottom < height - 3:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, speed_player)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-speed_player, 0)
        if self.rect.right < width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(speed_player, 0)

coin_size = 30
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Coin image settings
        self.coin_size = coin_size
        self.image = pygame.image.load('C:/Users/OmeN_HP/Downloads/pngimg.com - coin_PNG36887.png')
        self.image = pygame.transform.scale(self.image, (coin_size, coin_size))

        # Coin hit-box
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, width - 30), random.randint(30, height - 30))

    def move(self):
        global coins_collected
        if pygame.sprite.collide_rect(self, P1):
            # next coin will be with another weight
            self.coin_size = random.randint(15,45)
            self.image = pygame.transform.scale(self.image, (self.coin_size, self.coin_size))

            coins_collected += 1

            self.rect.center = (random.randint(30, width - 30), random.randint(30, height - 30))


P1 = Player()
E1 = Enemy()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(Coin())

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(coins)


# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


a = True
# Game loop
while True:

    for event in pygame.event.get():


        # every 10 second speed increases
        if event.type == INC_SPEED:
            speed_enemy += 0.1
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # every 3 coins speed increases
    if coins_collected % 3 == 0:
        if a:
            speed_enemy += 0.1
            a = False
    else:
        a = True



    # background pasting
    display.blit(background, (0, 0))

    # score and coins pasting
    scores = font_small.render(f"Score: {score}", True, BLACK)
    display.blit(scores, (10, 10))
    coins_collected_text = font_small.render(f"Coins: {coins_collected}", True, BLACK)
    display.blit(coins_collected_text, (width - 120, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        display.blit(entity.image, entity.rect)
        if isinstance(entity, Coin):
            entity.update()
        entity.move()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        # sound of crash settings
        pygame.mixer.Sound('C:/Users/OmeN_HP/Downloads/glass-hit-192119.mp3').play()
        time.sleep(0.5)

        # after-death settings
        display.fill(RED)
        display.blit(game_over, (width // 2 - 90, height // 2))

        pygame.display.update()

        # Removing all entities
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
        # asd
    pygame.display.update()
    FPS.tick(240)

