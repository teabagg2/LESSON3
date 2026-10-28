
import pygame
import random

pygame.init()

screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Smart Traffic Signal Simulator")

CAR_EVENT = pygame.USEREVENT + 1
SIGNAL_EVENT = pygame.USEREVENT + 2

ROAD_COLOR = pygame.Color("gray")
LINE_COLOR = pygame.Color("white")
CAR_COLORS = [
    pygame.Color("blue"),
    pygame.Color("yellow"),
    pygame.Color("orange"),
    pygame.Color("purple"),
    pygame.Color("cyan")
]

RED = pygame.Color("red")
GREEN = pygame.Color("green")
BLACK = pygame.Color("black")
WHITE = pygame.Color("white")
GRAY = pygame.Color("gray")

signal_color = RED


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((60, 30))
        self.image.fill(random.choice(CAR_COLORS))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 250
        self.velocity = 4

    def update(self):
        self.rect.move_ip(self.velocity, 0)

        if self.rect.right >= screen_width:
            self.rect.right = screen_width
            self.velocity = -abs(self.velocity)
            pygame.event.post(pygame.event.Event(CAR_EVENT))
            pygame.event.post(pygame.event.Event(SIGNAL_EVENT))

        elif self.rect.left <= 0:
            self.rect.left = 0
            self.velocity = abs(self.velocity)
            pygame.event.post(pygame.event.Event(CAR_EVENT))
            pygame.event.post(pygame.event.Event(SIGNAL_EVENT))


car = Car()
all_sprites = pygame.sprite.Group()
all_sprites.add(car)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == CAR_EVENT:
            car.image.fill(random.choice(CAR_COLORS))

        elif event.type == SIGNAL_EVENT:
            if signal_color == RED:
                signal_color = GREEN
            else:
                signal_color = RED

    screen.fill(WHITE)

    pygame.draw.rect(
        screen,
        ROAD_COLOR,
        (0, 200, screen_width, 100)
    )

    for line_x in range(0, screen_width, 80):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (line_x, 250),
            (line_x + 40, 250),
            3
        )

    pygame.draw.rect(
        screen,
        BLACK,
        (500, 30, 60, 130)
    )

    pygame.draw.circle(
        screen,
        RED if signal_color == RED else GRAY,
        (530, 65),
        20
    )

    pygame.draw.circle(
        screen,
        GREEN if signal_color == GREEN else GRAY,
        (530, 120),
        20
    )

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
