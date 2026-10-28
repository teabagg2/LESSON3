
import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mini Sprite Adventure")

x = 375
y = 275
sprite_width = 50
sprite_height = 50
speed = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)
PURPLE = (150, 0, 200)

background_color = WHITE
sprite_color = BLUE

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    x = max(0, min(x, screen_width - sprite_width))
    y = max(0, min(y, screen_height - sprite_height))

    if x == 0:
        sprite_color = RED
    elif x == screen_width - sprite_width:
        sprite_color = GREEN
    elif y == 0:
        sprite_color = PURPLE
    elif y == screen_height - sprite_height:
        sprite_color = YELLOW
    else:
        sprite_color = BLUE

    screen.fill(background_color)

    pygame.draw.circle(screen, RED, (150, 150), 40)
    pygame.draw.circle(screen, BLACK, (300, 150), 40, 3)

    sprite = pygame.Rect(x, y, sprite_width, sprite_height)
    pygame.draw.rect(screen, sprite_color, sprite)

    pygame.display.update()
    clock.tick(60)

pygame.quit()

