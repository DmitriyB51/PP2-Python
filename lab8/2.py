import pygame
from random import randint

pygame.init()

WIDTH = 720
HEIGHT = 720


screen = pygame.display.set_mode((WIDTH, HEIGHT))

colorWHITE = (255, 255, 255)
colorGRAY = (70, 70, 70)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

FPS = 4

clock = pygame.time.Clock()

CELL = 60

level = 1
score = 0
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def generate():
        return Point(randint(0, WIDTH // CELL - 1) * CELL, randint(0, HEIGHT // CELL - 1) * CELL)


class Snake:
    def __init__(self):
        self.body = [Point.generate()]
        self.dx = 0
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        head = self.body[0]
        head.x += self.dx * CELL
        head.y += self.dy * CELL

        # check for collisions
        if head.x == WIDTH:
            head.x = 0
        if head.x < 0:
            head.x = (WIDTH // CELL - 1) * CELL
        if head.y == HEIGHT:
            head.y = 0
        if head.y < 0:
            head.y = (HEIGHT // CELL - 1) * CELL

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            print("Got food! Length is: ", len(self.body))
            return True

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x, head.y, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x, segment.y, CELL, CELL))


class Food:
    def __init__(self):
        self.pos = Point.generate()

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x, self.pos.y, CELL, CELL))

    # check if place for food is valid
    def regenerate(self):
        valid_pos = False
        while not valid_pos:
            new_pos = Point.generate()
            valid_pos = True
            for segment in snake.body:
                if new_pos.x == segment.x and new_pos.y == segment.y:
                    valid_pos = False
                    break
            if valid_pos:
                self.pos = new_pos

        self.pos = Point.generate()


def draw_grid():
    for i in range(0, HEIGHT, CELL):
        for j in range(0, WIDTH, CELL):
            pygame.draw.rect(screen, colorGRAY, (i, j, CELL, CELL), 1)


snake = Snake()
food = Food()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
    screen.fill(colorBLACK)

    snake.move()
    if snake.check_collision(food):
        food.regenerate()
        score += 1
        # level increases every 3 foods
        if score % 3 == 0:
            level += 1
            # score increases every level
            FPS += 1

    snake.draw()
    food.draw()
    draw_grid()

    # display score
    font = pygame.font.SysFont("Verdana", 36)
    text_score = font.render(f"Score: {score}", True, colorWHITE)
    screen.blit(text_score, (10, 5))

    # display level
    text_level = font.render(f"Level: {level}", True, colorWHITE)
    screen.blit(text_level, (WIDTH-160, 5))

    pygame.display.flip()
    clock.tick(FPS)